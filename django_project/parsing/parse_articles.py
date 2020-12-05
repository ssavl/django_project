import requests
from bs4 import BeautifulSoup as bs
import json
from pprint import pprint
import re


list_of_article = []
url_test = 'https://theblueprint.ru/fashion/industry'
URL = "https://theblueprint.ru/fashion/industry/logotip"
req = requests.get(url_test).text
soup = bs(req, 'html.parser')
a = soup('a', class_='title')
print(a[3])
# main_tags = soup.find_all('div', class_='editor')  # Я указал более конкретный html тег, вложеность сократилась
# print(main_tags[0].find('span'))
# print('_' * 200)



def get_article():
    for i in main_tags:
        if 'uppercase' in str(i):
            list_of_article.append(i.find('span').get_text().upper())
        list_of_article.append(i.find('span').get_text())
    print(list_of_article)
    print('_' * 200)
    print(''.join(list_of_article))




"""Даша,привет! Хотел попросить помощи у тебя, есть несколько тем вопросы по которым возникают по мере учебы))) можешь мне в зуме обьяснить одну тему по парсингу, типа одного урока/занятия, к примеру на коммерческой основе """

