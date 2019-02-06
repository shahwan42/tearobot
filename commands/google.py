import requests
from bs4 import BeautifulSoup


def google_search(message):
    """google for ``message``"""
    page = requests.get('https://www.google.com/search', params={'q': message})
    soup = BeautifulSoup(page.content, 'html.parser')  # WebPage in HTML
    links = soup.findAll('cite')  # links list
    descriptions = soup.findAll('span', {'class': 'st'})  # descriptions list

    if len(links) == 0:  # if no results found
        return 'No results found for your search query. Try another meaningfull one.'

    result = []  # result to be returned link+description
    for idx, link in enumerate(links):  # loop over the links (whatever their length is)
        result.append(link.text)  # current link
        result.append(descriptions[idx].text)  # current link description
        result.append('\n')  # new line

    return '\n'.join(result)


if __name__ == '__main__':
    print(google_search('google me please'))
