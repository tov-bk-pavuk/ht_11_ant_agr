import requests
import re

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def notify(massage, email):
    from_email = 'mymail@gmail.com'
    subject = 'Notification'
    recipient_list = email
    send_mail(subject, massage, from_email, [recipient_list])


@shared_task
def scrap():
    url = 'https://quotes.toscrape.com/'  # Сайт для парсинга

    # Вспомогательная Функция сделать суп (URL)
    def cook_soup(url: str):
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        return soup
        # Возвращает объект - суп.

    # Функция получить текст тега по классу (URL, тег, имя_класса)
    def get_items(url: str, teg: str, clas: str):  # цитаты 'span', class_='text'
        soup = cook_soup(url)  # авторы 'small', class_='author'
        items = [i.text for i in soup.find_all(teg, class_=clas)]
        return items
    # Возвращает список с текстом тегов

    # Функция получить детали авторов (URL_страницы, тело_ссылки_содержит)
    def get_authors_det(url: str, part: str):  # /author/
        soup = cook_soup(url)

        def not_lacie(href):  # хреф содержит "/author/"
            return href and re.compile(part).search(href)

        url = 'https://quotes.toscrape.com'
        auth_link_text = soup.find_all(href=not_lacie)  # все href содержfobt "/author/"
        list_url = list()  # Будет список ссылок для деталей автора

        # Получаем список ссылок для автора
        for i in range(10):  # len(auth_link_text)
            list_url.append(url + auth_link_text[i].get('href'))  # Прикрyчиваем ссылки для авторов

        # Формируем список деталей по всем авторам на странице
        decriptions = list()  # Детали автора готовы
        for i in range(10):  # len(auth_link_text)
            soup_1 = cook_soup(list_url[i])  # получаем адрес деталей автора
            aut_desc = soup_1.find('div', class_='author-description').text  # получаем тест деталей
            decriptions.append(aut_desc)  # Добавляем тескт деталей в список
        return decriptions

    # Возвращает список деталей авторов
    # Функция получить страницу из пагинатора (URL_страницы)

    def get_page(url: str):

        quots = get_items(url, 'span', 'text')
        auth = get_items(url, 'small', 'author')
        det = get_authors_det(url, '/author/')

        for i, k, l in zip(quots, auth, det):
            print(i)
            print(k)
            print(l)
        try:
            soup = cook_soup(url)
            page_href_text = soup.find('li', class_='next').find('a').get('href')
            if page_href_text[:-3] not in url:
                url_page = url[:-1] + page_href_text
            else:
                url_page = url[:-8] + page_href_text
            print(url_page)
            return get_page(url_page)
        except AttributeError:
            print('Закончились страницы')

    get_page(url)