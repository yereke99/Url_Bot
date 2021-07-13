import requests
from lxml import html
from collections import Counter
import cssselect

def parse(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]
    c = Counter(all_tags)
    print(c)
    print(type(c))

    global tag
    for e in c:
        if e == 'div':
            tag = c[e]

        # print('{}: {}'.format(e, c[e]))
    print(tag)
    return tag

urls = 'https://www.cyberforum.ru/python-web/thread1966556.html'

#parse(urls)