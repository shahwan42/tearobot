import requests
from bs4 import BeautifulSoup


def weather():
    page = requests.get(
        'https://www.google.com/search',
        params={'q': 'weather+zagazig', 'oq': 'weather', 'lang': 'en-GB'})

    return BeautifulSoup(page.content, 'html.parser').findAll('span', {'class': 'wob_t'})[0].text  # temperature


if __name__ == '__main__':
    print(weather())
