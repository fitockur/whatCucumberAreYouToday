import requests
from bs4 import BeautifulSoup


def cucumber_scrapper(url='https://stroy-podskazka.ru/ogurec/sorta/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    alphabet_groups = soup.find_all('div', class_='alphabet__group')

    cucumbers = {}
    for alphabet_group in alphabet_groups:
        alphabet = alphabet_group.find('div', class_='hl').text
        cucumbers[alphabet] = {}
        for cucumber in alphabet_group.find_all('a', class_='perelink_gallery_item_sorta'):
            cucumbers[alphabet][cucumber.img['alt']] = cucumber.img['src']
    return cucumbers