from book_store import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
]
