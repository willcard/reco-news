import pytest

from sys import path
from news_api import api_requests

def test_get_articles():
    # return type
    fr_request = api_requests.get_articles('fr')
    assert isinstance(fr_request, list)
    assert len(fr_request) > 0
    assert isinstance(fr_request[0], dict)

    # fake country
    notacountry =  'notacountry'
    with pytest.raises(ValueError, match=f"country '{notacountry}' not a valid country code"):
            api_requests.get_articles(notacountry)