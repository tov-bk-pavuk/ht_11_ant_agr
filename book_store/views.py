from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, IntegerField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AuthorForm, Notification, StoreForm
from .models import Author, Book, Publisher, Store
from .tasks import notify


def notification(request):
    now = timezone.now()
    if request.method == 'POST':
        form = Notification(request.POST)
        if form.is_valid():
            massage = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            datetime = form.cleaned_data['datetime']
            # команда создать задачу для селери:
            if datetime < now:
                return HttpResponse('Дата в прошлом')
            elif datetime > now + timedelta(days=2):
                return HttpResponse('Слишком далёкое будущее')
            notify.apply_async((massage, email), eta=datetime)
            return HttpResponseRedirect('/thanks/')
    else:
        form = Notification()
    return render(request, 'book_store/form.html', {'form': form})


def thanks(request):
    return render(request, "book_store/thanks.html")


def home(request):
    return render(request, "book_store/book_store_index.html")


class BookListView(ListView):
    model = Book
    template_name = "book_store/books.html"
    queryset = Book.objects.all().annotate(Count('authors'))
    paginate_by = 25


'''
def book_list(request):
    books_query_ant = Book.objects.all().annotate(Count('authors'))
    books_count = books_query_ant.count()
    return render(request, "book_store/books.html",
                  context={'books': books_query_ant,
                           'amount': books_count,
                           })
'''

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


class StoreListView(ListView):
    model = Store
    template_name = "book_store/stores.html"
    queryset = Store.objects.prefetch_related('books'). \
        all().annotate(sred=Avg('books__price', output_field=IntegerField()))
    paginate_by = 50


def stores_detailed(request, pp):
    pk = Store.objects.prefetch_related('books').get(pk=pp)
    return render(request, 'book_store/detailed_store.html', context={
        'pk': pk,
    })


class AuthorListView(ListView):
    model = Author
    template_name = "book_store/authors.html"
    queryset = Author.objects.prefetch_related('book_set').all()
    paginate_by = 50


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'book_store/detailed_author.html'
    pk_url_kwarg = 'pp'


class AuthorCreateView(CreateView):
    form_class = AuthorForm
    template_name = 'book_store/create_obj.html'
    success_url = '/thanks/'


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'book_store/create_obj.html'
    pk_url_kwarg = 'pp'
    form_class = AuthorForm
    success_url = '/thanks/'


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'book_store/del_obj.html'
    pk_url_kwarg = 'pp'
    success_url = '/thanks/'


class StoreCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    form_class = StoreForm
    template_name = 'book_store/create_obj.html'
    success_url = '/thanks/'


class StoreUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'
    model = Store
    template_name = 'book_store/create_obj.html'
    pk_url_kwarg = 'pp'
    form_class = StoreForm
    success_url = '/thanks/'


class StoreDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/'
    model = Store
    template_name = 'book_store/del_obj.html'
    pk_url_kwarg = 'pp'
    success_url = '/thanks/'
