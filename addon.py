from xbmcswift2 import Plugin, xbmcgui
from resources.lib import archive

SITE_URL = 'https://archive.org'
PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid='

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('views'),
        }
    ]
    
    return items


@plugin.route('/views/')
def views():
    
    view_url = 'https://archive.org/details/movies?&sort=-downloads&page=1'
    
    items = []

    content = archive.get_views(view_url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('view_category', url=SITE_URL + i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/views/<url>/')
def view_category(url):

    items = []

    content = archive.get_category(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=SITE_URL + i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/views/view_category/play_content/<url>')
def play_content(url):

    items = []

    content = archive.play_content(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': SITE_URL + i['path'],
            'is_playable': True,
        })

    return items


if __name__ == '__main__':
    plugin.run()
