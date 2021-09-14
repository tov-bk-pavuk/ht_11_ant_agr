from random import choice, randrange, uniform

from book_store.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, choices=range(10, 1000),
                            help=u'amount - от 10 до 1000')

    def handle(self, *args, **options):
        amount = options['amount']

        author = [Author(name=fake.name(), age=randrange(18, 85)) for i in range(amount)]
        Author.objects.bulk_create(author)

        publisher = [Publisher(name=fake.company()) for i in range(amount)]
        Publisher.objects.bulk_create(publisher)

        store = [Store(name=fake.company()) for i in range(amount)]
        Store.objects.bulk_create(store)

        last = Publisher.objects.latest('pk')  # Блок для решения проблем с идентификатором
        last = last.id - amount + 1

        seq = [('0' + str(i)) for i in range(1, 10)]  # Блок генерации данных для дат
        seq += '11', '12'  # Месяцы
        seq_1 = seq + [str(i) for i in range(13, 29)]  # Числа месяца

        book = [Book(
            name=fake.job(),
            pages=randrange(50, 900),
            price=round(uniform(150, 1500), 2),
            rating=round(uniform(1, 5), 1),
            publisher=Publisher.objects.get(pk=(randrange(last, amount + last - 1))),
            pubdate=f'{randrange(1920, 2020)}-{choice(seq)}-{choice(seq_1)}') for i in range(amount)]
        Book.objects.bulk_create(book)

        authors = Author.objects.all()
        length = len(authors)
        team = list()
        for i in range(1, 6):
            team.append(authors[randrange(length)])

        books = Book.objects.filter(pk__range=(last, amount + last - 1))
        for i in books:
            for k in team:
                i.authors.add(k)

        book_set = books[1:11]
        stores = Store.objects.filter(pk__range=(last, amount + last - 1))
        for i in stores:
            for k in book_set:
                i.books.add(k)
