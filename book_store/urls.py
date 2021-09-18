from book_store import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('books/<int:id>', views.detailed, name='detailed'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<int:id>', views.publishers_detailed, name='pub_det'),
    path('stores/', views.stores, name='stores'),
    path('stores/<int:id>', views.stores_detailed, name='sto_det'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:id>', views.authors_detailed, name='aut_det'),
]
