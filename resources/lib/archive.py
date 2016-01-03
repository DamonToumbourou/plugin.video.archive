from bs4 import BeautifulSoup as bs
import requests
import re


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    return soup


def get_views(url):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'item-ia collection-ia'})

    for i in content:
        data = i.find('a')

        label = data.get_text().strip()
        print 'label: '
        print label

        path = data.get('href')
        print 'path: '
        print path
        
        try:
            thumb = str(i.img)
            thumb = re.search('/services(.*)(?=">)', thumb).group(0)
            print 'thumb: '
            print thumb

        except AttributeError:
            continue

#get_views('https://archive.org/details/movies?sort=-downloads')
