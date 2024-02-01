import requests
from urllib.parse import urlencode
from pprint import pprint
from tqdm import tqdm
from time import sleep

from .config import API_KEY
from .const import URL_BASE, COUNTRIES


def get_articles(country: str) -> list:
    """
        get articles from newsapi.org for a given country.
    """
    if not country in COUNTRIES:
        raise ValueError(f"country '{country}' not a valid country code")

    params = {'apiKey':API_KEY, 'country':country}
    url = URL_BASE + urlencode(params)

    response = requests.get(url).json()
    articles = response.get('articles')
    return articles

def get_all_articles() -> dict:
    """
        get articles for all countries.
    """
    all_articles = {}
    for country_code in tqdm(COUNTRIES):
        try:
            articles = get_articles(country_code)
        except Exception as err:
            articles = []
            print(f'{country_code} failed:'+str(err))
            
        all_articles[country_code] = articles
        sleep(1)
    return all_articles