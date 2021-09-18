from book_store import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('books/<int:id>', views.detailed, name='detailed'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<int:id>', views.publishers_detailed, name='pub_det'),
    path('stores/', views.stores, name='stores'),
    path('authors/', views.authors, name='authors'),
]
