import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    
    food = [
        {'title': 'burger',
        'url':'http://docs.python.org/3/tutorial/', "views": 128, "likes": 64},
        {'title':'salad',
        'url':'http://www.greenteapress.com/thinkpython/', "views": 128},
        {'title':'bread',
        'url':'http://www.korokithakis.net/tutorials/python/', "views": 128, "likes": 16} ]
    
    place = [
        {'title':'school',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', "views": 128, "likes": 32},
        {'title':'park',
        'url':'http://www.djangorocks.com/', "views": 128, "likes": 32},
        {'title':'museum',
        'url':'http://www.tangowithdjango.com/', "views": 128, "likes": 16} ]

    cats = {'Food': {'pages': food, "views": 128},
        'Place': {'pages': place, "views": 64}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'], p["likes"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name, views=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()