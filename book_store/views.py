from django.shortcuts import render

from .models import Author, Book, Publisher, Store


def home(request):
    return render(request, "book_store/book_store_index.html")


def book_list(request):
    # books_query = Book.objects.prefetch_related('authors').filter(pk__range=(5, 10))
    # books_query = Book.objects.prefetch_related('authors').all()
    books_query = Book.objects.all()
    books_count = books_query.count()
    return render(request, "book_store/books.html",
                  context={'books': books_query,
                           'amount': books_count,
                           })


def detailed(request, id):
    pk = Book.objects.prefetch_related('authors').get(pk=id)
    return render(request, 'book_store/detailed_book.html', context={
        'pk': pk,
    })


def publishers(request):
    publishers_query = Publisher.objects.prefetch_related('book_set').all()
    return render(request, "book_store/publishers.html",
                  context={'publishers': publishers_query,
                           })


def publishers_detailed(request, id):
    pk = Publisher.objects.prefetch_related('book_set').get(pk=id)
    return render(request, 'book_store/detailed_publisher.html', context={
        'pk': pk,
    })


def stores(request):
    stores_query = Store.objects.prefetch_related('books').all()
    return render(request, "book_store/stores.html",
                  context={'stores': stores_query})


def stores_detailed(request, id):
    pk = Store.objects.prefetch_related('books').get(pk=id)
    return render(request, 'book_store/detailed_store.html', context={
        'pk': pk,
    })


def authors(request):
    authors_query = Author.objects.filter(pk__range=(10, 20))
    return render(request, "book_store/authors.html",  # authors_detailed, name='aut_det'),
                  context={'authors': authors_query})  # stores_detailed, name='sto_det'),


def authors_detailed(request, id):
    pk = Author.objects.prefetch_related('book_set').get(pk=id)
    return render(request, 'book_store/detailed_authors.html', context={
        'pk': pk,
    })
