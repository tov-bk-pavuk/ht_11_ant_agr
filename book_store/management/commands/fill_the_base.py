from django.core.management.base import BaseCommand
from django.utils import timezone

from book_store.models import Author, Publisher, Book, Store

from faker import Faker
from random import randrange, uniform

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

        book = [Book(name=fake.job(), pages=randrange(50, 900), price=round(uniform(150, 2500), 2),
                     rating=round(uniform(1, 5), 2), publisher=Publisher.objects.get(pk=1), pubdate=f'{randrange(1920, 2020)}-'
                                                             f'{randrange(10, 12)}-{randrange(10, 28)}')
                for i in range(amount)]
        Book.objects.bulk_create(book)

        store = [Store(name=fake.company()) for i in range(amount)]
        Store.objects.bulk_create(store)
