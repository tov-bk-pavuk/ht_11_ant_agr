from django.shortcuts import render

from .models import Author, Book, Publisher, Store


def home(request):
    return render(request, "book_store/book_store_index.html")


def book_list(request):
    books_query = Book.objects.prefetch_related('authors').filter(pk__range=(5, 10))
    books_count = Book.objects.all().count()
    return render(request, "book_store/books.html",
                  context={'books': books_query,
                           'amount': books_count})


def publishers(request):
    publishers_query = Publisher.objects.filter(pk__range=(10, 20))
    return render(request, "book_store/publishers.html",
                  context={'publishers': publishers_query})


def stores(request):
    stores_query = Store.objects.filter(pk__range=(10, 20))
    return render(request, "book_store/stores.html",
                  context={'stores': stores_query})


def authors(request):
    authors_query = Author.objects.filter(pk__range=(10, 20))
    return render(request, "book_store/authors.html",
                  context={'authors': authors_query})
