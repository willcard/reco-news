import requests
from urllib.parse import urlencode
from pprint import pprint

from config import API_KEY

URL_BASE = 'https://newsapi.org/v2/top-headlines?'
PARAMS_BASE = {'apiKey':API_KEY}


def get_articles(country: str) -> dict:
    """
        get articles from newsapi.org
    """ 
    params = PARAMS_BASE.copy()
    params['country'] = country
    url = URL_BASE + urlencode(params)

    response = requests.get(url).json()
    articles = response.get('articles')
    return articles


def insert_news():
    """
        insert news in postgres
    """
    pass


if __name__ == '__main__':
    articles = get_articles('fr')
    pprint(articles)