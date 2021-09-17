from book_store import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('publishers/', views.publishers, name='publishers'),
    path('stores/', views.stores, name='stores'),
    path('authors/', views.authors, name='authors'),
]
