import requests
from bs4 import BeautifulSoup

def scrape(url, selector=None):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    
    if selector:
        elements = soup.select(selector)
        return {'data': [element.get_text() for element in elements]}
    else:
        return {'data': soup.get_text()}
