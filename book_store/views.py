from django.db.models import Avg, Count, IntegerField
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .tasks import notify

from .models import Author, Book, Publisher, Store

from .forms import Notification


def notification(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Notification(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            datetime = form.cleaned_data['datetime']
            # команда создать задачу для селери:
            notify(subject, email, datetime)
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Notification()
    return render(request, 'book_store/form.html', {'form': form})


def thanks(request):
    return render(request, "book_store/thanks.html")


def home(request):
    return render(request, "book_store/book_store_index.html")


def book_list(request):
    books_query_ant = Book.objects.all().annotate(Count('authors'))
    books_count = books_query_ant.count()
    return render(request, "book_store/books.html",
                  context={'books': books_query_ant,
                           'amount': books_count,
                           })


def detailed(request, pp):
    pk = Book.objects.prefetch_related('authors').get(pk=pp)
    return render(request, 'book_store/detailed_book.html', context={
        'pk': pk,
    })


def publishers(request):
    publishers_query = Publisher.objects.prefetch_related('book_set').all()
    return render(request, "book_store/publishers.html",
                  context={'publishers': publishers_query,
                           })


def publishers_detailed(request, pp):
    pk = Publisher.objects.prefetch_related('book_set').get(pk=pp)
    return render(request, 'book_store/detailed_publisher.html', context={
        'pk': pk,
    })


def stores(request):
    # .annotate(Avg(''))
    # <td align="center">{{ store.books.count  }}</td>
    stores_query = Store.objects.prefetch_related('books').\
        all().annotate(sred=Avg('books__price', output_field=IntegerField()))
    return render(request, "book_store/stores.html",
                  context={'stores': stores_query})


def stores_detailed(request, pp):
    pk = Store.objects.prefetch_related('books').get(pk=pp)
    return render(request, 'book_store/detailed_store.html', context={
        'pk': pk,
    })


def authors(request):
    authors_query = Author.objects.prefetch_related('book_set').all()
    return render(request, "book_store/authors.html",  # authors_detailed, name='aut_det'),
                  context={'authors': authors_query})  # stores_detailed, name='sto_det'),


def authors_detailed(request, pp):
    pk = Author.objects.prefetch_related('book_set').get(pk=pp)
    return render(request, 'book_store/detailed_author.html', context={
        'pk': pk,
    })
