![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
# *ੈ✩‧˚PEP parser *ੈ✩.˚
## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Project's+goal)](https://git.io/typing-svg)
~ *bs4_parser_pep project was created in order to get aquaired with:* ~
- Зarsing by usung bs4([BeautifulSoup](https://pypi.org/project/beautifulsoup4/)) library
- HTTP caching([requests_cache](https://pypi.org/project/requests-cache/))
- Configuring the parser through terminal([argparser](https://docs.python.org/3/library/argparse.html))

### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Technologies)](https://git.io/typing-svg)
- Python 3.10
- BeautifulSoup4 4.9
- requests-cache 1.0
###### *The rest of the technologies can be found in the requirements.txt file*

### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Project's+description)](https://git.io/typing-svg)
#### ~ *The parser processes:* ~
- [Python documentation's main page](https://docs.python.org/3/)
- [Main page of PEP documentation](https://peps.python.org/)
- Download Python's documentation
#### ~ *Parser's modes* ~
####  pep
Parser compares PEP's status  displayed on the main page in the general table of all PEPs with status displayed  on each PEP's page . Then it
calculates the number of PEPs in each status and the total number of PEPs and saves studied data into csv file.
```
Статус / Количество
```
#### whats-new
Parser finds all the links to articles that contain information about available Python versions and then collects information from each page.

```
Ссылка на статью о версии Python / Название статьи / Информация об авторе
```
#### latest_versions
Parser find information about all Python's versions from [Python documentation's main page](https://docs.python.org/3/) 
```
Ссылка на статью о версии Python / Верия / Статус
```
- **download**  
Parser downloads archieve containing documentation of the latest Python version https://docs.python.org/3/download.html and saves it into ``/src/downloads/`` directory

#### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=96D1D5&random=false&width=435&lines=Ways+to+output+the+collected+data:)](https://git.io/typing-svg)
- General output (stdout);
- Output to the console in tabular form ``-o pretty``;
- - Saving data into csv file ``-o file`` that will be saved into ``/src/results/`` folder;
###### *Logs are saved into ``/src/logs/`` folder.*

### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=How+to+launch+the+project)](https://git.io/typing-svg)
*Do following steps by using terminal.*

Выполните следующие команды в терминале:

1. Clone project on local machine
```
git clone git@github.com:SemenovaLiza/bs4_parser_pep.git
```
2. Create and activate virtual environment in root directory:
```
python -m venv venv
```
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&pause=1000&color=5FADF7&random=false&width=435&lines=for+OS:)](https://git.io/typing-svg)
```
source venv/bin/activate
```
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&pause=1000&color=5FADF7&random=false&width=435&lines=for+Windows:)](https://git.io/typing-svg)
```
source venv/Scripts/activate
```
3. Isnatll all the dependencies listed in requirements.txt file
```
pip install -r requirements.txt 
```
3. Run parser in terminal:
```
python src/main.py pep -o file
```

### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Command+line+available+arguments)](https://git.io/typing-svg)
*To get aquired with available parser modes use named argument ``-h`` or ``--help``:*

```
python src/main.py -h
```
Output:
```
Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

options:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Output)](https://git.io/typing-svg)
1. To output the results to the terminal in a standard format, run the parser with the positional argument ```whats-new```, ```latest-versions``` or ```pep```:
```
python src/main.py latest-versions
```  
```
$ python src/main.py latest-versions
"28.01.2023 03:53:47 - [INFO] - Парсер запущен!"
Ссылка на документацию Версия Статус
https://docs.python.org/3.12/ 3.12 in development
https://docs.python.org/3.11/ 3.11 stable
https://docs.python.org/3.10/ 3.10 stable
https://docs.python.org/3.9/ 3.9 security-fixes
...
https://www.python.org/doc/versions/ All versions
```
2. To get output in table format ```-o pretty```:
- latest-version:
```
python src/main.py latest-versions -o pretty
```
```
$ python src/main.py latest-versions -o pretty
"28.01.2023 03:57:56 - [INFO] - Парсер запущен!"
+--------------------------------------+--------------+----------------+
| Ссылка на документацию               | Версия       | Статус         |
+--------------------------------------+--------------+----------------+
| https://docs.python.org/3.12/        | 3.12         | in development |
| https://docs.python.org/3.11/        | 3.11         | stable         |
| https://docs.python.org/3.9/         | 3.9          | security-fixes |
|                ...                   |     ...      |       ...      |
| https://www.python.org/doc/versions/ | All versions |                |
+--------------------------------------+--------------+----------------+
```
- pep:
```
python src/main.py pep -o pretty
```
```
+----------------------+------------+
| Статус               | Количество |
+----------------------+------------+
| Active               | 74         |
| Accepted             | 84         |
| Final                | 526        |
| Draft                | 58         |
| Superseded           | 40         |
| Deferred             | 72         |
| Withdrawn            | 110        |
| Rejected             | 240        |
| April Fool!          | 2          |
| Общее количество PEP | 1206       |
+----------------------+------------+
```

3. Download
- To download Python documentation run parser WITHOUT arguments:
```
python src/main.py download
```
###### *zip archieve that contains Python documentation in PDF (A4 paper size) format wiil be saved into ``src/downloads/`` folder that created after running command.*
----
- To save output into csv file run parser with 
``-o file`` argument:  
```
python src/main.py latest-versions -o file
```
csv files will be saved into ``src/results`` folder.


### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Addition+arguments:)](https://git.io/typing-svg)
- To clear cache after creating session: ``-с`` or ``--clear-cache``:
```
python src/main.py latest-versions -c -o pretty
```
### [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Author:)](https://git.io/typing-svg)

Semenova Elizaveta

~ [Other projects](https://github.com/SemenovaLiza) ~


[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=98D0F7FF&random=false&width=435&lines=⋆⋅☆⋅⋆☆⋆⋅☆⋅⋆)](https://git.io/typing-svg)