import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
from config import client


db = client.testdb
list_of_article = []

URL = "https://theblueprint.ru/fashion/industry/logotip"
base_url = 'https://theblueprint.ru'
#db.blueprint.insert_one(data)


def get_list_articles():
    url_test = 'https://theblueprint.ru/fashion/industry'
    req = requests.get(url_test).text
    soup = bs(req, 'html.parser')
    titles = soup('a', class_='title')
    for i in titles:
        list_a = str(i).split('>', 1)
        href = list_a[0][42:-1]
        title = list_a[1][13:-12]
        # data = {base_url+href: title}
        print(f"'{base_url+href}' = '{title}'")
        print('-' * 200)


# db.blueprint.insert_one({1: 'qwer'})



def get_article(url):
    request = requests.get(url).text
    soup = bs(request, 'html.parser')
    main_tags = soup.find_all('div', class_='editor')  # Я указал более конкретный html тег, вложеность сократилась
    for i in main_tags:
        if 'uppercase' in str(i):
            list_of_article.append(i.find('span').get_text().upper())
        list_of_article.append(i.find('span').get_text())
        final = ''.join(list_of_article)
    print(final, type(final))


get_article('https://theblueprint.ru/fashion/industry/raf-simons-ss21')



"""Даша,привет! Хотел попросить помощи у тебя, есть несколько тем вопросы по которым возникают по мере учебы))) можешь мне в зуме обьяснить одну тему по парсингу, типа одного урока/занятия, к примеру на коммерческой основе """

# main_tags = soup.find_all('div', class_='editor')  # Я указал более конкретный html тег, вложеность сократилась
# print(main_tags[0].find('span'))
# print('_' * 200)

