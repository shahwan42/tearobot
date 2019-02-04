from bs4 import BeautifulSoup
import requests


def latest_news():
    url = 'https://www.bbc.com'
    page = requests.get(url)

    # parse the whole page in html
    soup = BeautifulSoup(page.content, 'html.parser')
    # get all  news links (tag 'a') in class "media__link"
    news = soup.findAll('a', {'class': 'media__link'})

    result = []
    for el in news:
        if not str(el['href']).startswith('https://'):
            result.append(url + el['href'])
        result.append(el.text.strip())

    return '\n'.join(result[:10])


# for development
if __name__ == '__main__':
    print(latest_news())
