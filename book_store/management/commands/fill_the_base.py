from django.core.management.base import BaseCommand
from django.utils import timezone

from book_store.models import Author, Publisher, Book, Store

from faker import Faker
from random import randrange, uniform, choice

fake = Faker()


class Command(BaseCommand):
    data = timezone.datetime

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, choices=range(1, 1000),
                            help=u'amount - от 1 до 1000')

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
            rating=round(uniform(1, 5), 2),
            publisher=Publisher.objects.get(pk=(randrange(last, amount + last - 1))),
            # authors=Author.objects.get(pk=(randrange(1, amount))),
            pubdate=f'{randrange(1920, 2020)}-{choice(seq)}-{choice(seq_1)}') for i in range(amount)]
        Book.objects.bulk_create(book)
'''
        authors_5 = Author.objects.filter(pk__range=(1, 5))
        books = Book.objects.all()
        for i, k in zip(books, authors_5):
            i.authors.add(k)
        # books.authors.add(authors_5)

        # Entry.objects.bulk_update(objs, ['headline'])
        # Book.objects.bulk_update(books, ['authors'])
'''
