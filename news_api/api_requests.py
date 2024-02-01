import requests
from urllib.parse import urlencode
from pprint import pprint

from .config import API_KEY
from .const import URL_BASE, COUNTRIES


def get_articles(country: str) -> dict:
    """
        get articles from newsapi.org
    """
    if not country in COUNTRIES:
        raise ValueError(f"country '{country}' not a valid country code")

    params = {'apiKey':API_KEY, 'country':country}
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