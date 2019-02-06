import requests
from bs4 import BeautifulSoup


def weather():
    """Returns weather in zagazig now"""
    page = requests.get('https://www.google.com/search?q=weather+zagazig&oq=weather&lang=en-GB')
    temperature = BeautifulSoup(page.content, 'html.parser').findAll('span', {'class': 'wob_t'})[0].text
    return f'The temperature in Zagazig now is: {temperature}'


if __name__ == '__main__':
    print(weather())
