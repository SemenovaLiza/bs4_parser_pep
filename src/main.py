import re
import logging
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

from constants import BASE_DIR, MAIN_DOC_URL, PEP_DOC_URL, EXPECTED_STATUS
from configs import configure_argument_parser, configure_logging
from outputs import control_output
from utils import get_response, find_tag


def whats_new(session):
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    response = get_response(session, whats_new_url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, features='lxml')
    main_div = find_tag(soup, 'section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = find_tag(main_div, 'div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all(
        'li', attrs={'class': 'toctree-l1'}
    )
    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]

    for section in tqdm(sections_by_python):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(whats_new_url, href)
        response = get_response(session, version_link)

        if response is None:
            continue

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')
        h1 = find_tag(soup, 'h1')
        dl = find_tag(soup, 'dl')
        dl_text = dl.text.replace('\n', ' ')
        results.append((version_link, h1.text, dl_text))

    return results


def latest_versions(session):
    response = get_response(session, MAIN_DOC_URL)

    if response is None:
        return

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    sidebar = find_tag(soup, 'div', attrs={'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')

    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break

    else:
        raise Exception('There is nothing')

    results = [('Documentation link', 'Version', 'Status')]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

    for a_tag in a_tags:
        link = a_tag['href']
        text_match = re.search(pattern, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append((link, version, status))

    return results


def download(session):
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    response = get_response(session, downloads_url)

    if response is None:
        return

    soup = BeautifulSoup(response.text, features='lxml')
    main_tag = find_tag(soup, 'div', attrs={'role': 'main'})
    table_tag = find_tag(main_tag, 'table', {'class': 'docutils'})
    pdf_a4_tag = find_tag(
        table_tag, 'a',
        attrs={'href': re.compile(r'.+pdf-a4\.zip$')}
    )
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(downloads_url, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    hh = BASE_DIR / 'downloads'
    hh.mkdir(exist_ok=True)
    archive_path = hh / filename
    response = session.get(archive_url)

    with open(archive_path, 'wb') as file:
        file.write(response.content)

    logging.info(f'Архив был загружен и сохранен: {archive_path}')


def pep(session):
    response = get_response(session, PEP_DOC_URL)
    results = [('Статус', 'Количество')]
    pep_statuses = {}
    total_pep = 0

    if response is None:
        return

    soup = BeautifulSoup(response.text, features='lxml')
    main_tag = find_tag(soup, 'section', attrs={'id': 'numerical-index'})
    main_tag_body = find_tag(main_tag, 'tbody')
    every_pep_link_tag = main_tag_body.find_all('tr')

    for pep in tqdm(every_pep_link_tag):
        total_pep += 1
        pep_table_status_tag = find_tag(pep, 'abbr')
        pep_table_status = pep_table_status_tag.text[1:]

        try:
            expected_status = EXPECTED_STATUS[pep_table_status]
        except KeyError:
            logging.error
            (
                f'Статус {pep_table_status} не найден'
            )

        link_tag = find_tag(pep, 'a')
        pep_link = urljoin(PEP_DOC_URL, link_tag['href'])
        response = get_response(session, pep_link)
        soup = BeautifulSoup(response.text, features='lxml')
        pep_status_tag = find_tag(
            soup, 'dl',
            attrs={'class': 'rfc2822 field-list simple'}
        )
        pep_status = pep_status_tag.find(
            string='Status'
        ).parent.find_next_sibling('dd').string

        pep_statuses[pep_status] = pep_statuses.get(pep_status, 0) + 1

        if pep_status not in expected_status:
            logging.warning
            (
                f'Несовпадающие статусы:'
                f'{pep_link}'
                f'Статус в карточке: {pep_status}'
                f'Ожидаемые статусы: {expected_status}'
            )

    results.extend((pep_statuses.items()))
    results.append(('Общее количество', total_pep))

    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep
}


def main():
    configure_logging()
    logging.info('Парсер запущен.')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы команной строки: {args}')

    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()

    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)

    if results is not None:
        control_output(results, args)

    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    main()
