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

# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=Project's+description)](https://git.io/typing-svg)
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

# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=How+to+launch+the+project)](https://git.io/typing-svg)


lixxa [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=3A55F7FF&random=false&width=435&lines=ㅤ⋆˙⟡♡)](https://git.io/typing-svg)