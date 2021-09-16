from django.shortcuts import render

from .models import Book


def home(request):
    return render(request, "book_store/book_store_index.html")


def book_list(request):
    books_query = Book.objects.filter(pk__range=(10, 20))
    return render(request, "book_store/books.html",
                  context={'books': books_query})
