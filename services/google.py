import requests
from bs4 import BeautifulSoup   

def google_search(message):
    '''google for ``message``'''
    page = requests.get('https://www.google.com/search', params={'q': message})
    soup = BeautifulSoup(page.content, "html.parser")  # WebPage in HTML Format.
    links = soup.findAll("cite")  # links list
    descriptions = soup.findAll("span", {"class":"st"})  # descriptions list

    result = []  # result to be returned link+description
    for i in range(9):
        result.append(links[i].text)
        result.append(descriptions[i].text)

    return result


if __name__ == '__main__':
    print(google_search('how are you'))