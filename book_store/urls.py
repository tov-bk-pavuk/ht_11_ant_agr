from book_store import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('books/<int:pp>', views.detailed, name='detailed'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<int:pp>', views.publishers_detailed, name='pub_det'),
    path('stores/', views.stores, name='stores'),
    path('stores/<int:pp>', views.stores_detailed, name='sto_det'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:pp>', views.authors_detailed, name='aut_det'),
]
