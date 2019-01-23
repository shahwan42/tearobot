
import requests
from bs4 import BeautifulSoup   
import html


def weather() :
    page = requests.get(
    	'https://www.google.com/search',
    	params={'q': 'weather+zagazig', 'oq':'weather'})

    soup = BeautifulSoup(page.content , 'html.parser')
    temp = soup.findAll('span', {'class': 'wob_t'})
    temperature = temp[0].text
    return temperature


