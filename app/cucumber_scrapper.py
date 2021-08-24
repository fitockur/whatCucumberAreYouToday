from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


url = 'https://stroy-podskazka.ru'

def get_cucumber(cucumber):
        href_cucumber = cucumber['href']
        response = requests.get(url + href_cucumber)
        soup = BeautifulSoup(response.text, 'lxml').find('div', {'class': 'tabs-item', 'id': 'tab-description'})
        text = 'Огуречик без описания'
        if soup.find('div', class_='text') is not None:
            text = soup.find('div', class_='text').text
        name = cucumber.img['alt']
        img_link = cucumber.img['src']
        description = str(soup.find(text='Основные характеристики сорта:').parent.parent.find_next().find_next())
        return text, name, img_link, description

def cucumber_scrapper():
    href_sorts = '/ogurec/sorta/'
    response = requests.get(url + href_sorts)
    soup = BeautifulSoup(response.text, 'lxml')

    cucumbers = []
    for alphabet_group in soup.find_all('div', class_='alphabet__group'):
        cucumbers.extend(alphabet_group.find_all('a', class_='perelink_gallery_item_sorta'))
    with ThreadPoolExecutor(16) as executor:
        cucumbers = list(executor.map(get_cucumber, cucumbers))
    return cucumbers