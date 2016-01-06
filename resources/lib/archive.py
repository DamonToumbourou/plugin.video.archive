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

    output = []

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

        items = {
            'label': label,
            'path': path,
            'thumbnail': thumb,
        }
        
        output.append(items)

    return output
#get_views('https://archive.org/details/movies?&sort=-downloads&page=1')


def get_category(url):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'item-ttl'})

    output = []

    for i in content:
        label = i.get_text().strip()

        path = i.find('a').get('href')

        try:
            thumb = str(i.img)
            thumb = re.search('/services(.*)(?=" s)', thumb).group(0)

        except AttributeError:
            continue

        items = { 
            'label': label,
            'path': path,
            'thumbnail': thumb,
        }

        output.append(items)

    return output
get_category('https://archive.org/details/opensource_movies')


def play_content(url):
    DOWNLOAD_CHOICE = 'MPEG4'
    VIDEO_LABEL = 'play video'

    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'format-group'})
   
    output = []

    for i in content:
        download_type = i.get_text()
        if DOWNLOAD_CHOICE in download_type:
            path = i.find('a').get('href')
            label = 'Play Video'

            items = { 
                'path': path,
                'label': VIDEO_LABEL,
            }

            output.append(items)

    return output
#play_content('https://archive.org/details/20151212-08277s')
