from book_store import views
from book_store.views import (
    AuthorCreateView,
    AuthorDeleteView,
    AuthorDetailView,
    AuthorListView,
    AuthorUpdateView)


from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('ntfc/', views.notification, name='ntfc'),
    path('thanks/', views.thanks, name='thanks'),
    path('books/', views.book_list, name='books'),
    path('books/<int:pp>', views.detailed, name='detailed'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<int:pp>', views.publishers_detailed, name='pub_det'),
    path('stores/', views.stores, name='stores'),
    path('stores/<int:pp>', views.stores_detailed, name='sto_det'),
    path('stores/create', views.StoreCreateView.as_view()),
    path('stores/<int:pp>/update', views.StoreUpdateView.as_view(), name='str_upt'),
    path('stores/<int:pp>/del', views.StoreDeleteView.as_view(), name='str_del'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pp>', AuthorDetailView.as_view(), name='aut_det'),
    path('authors/create', AuthorCreateView.as_view(), name='aut_crt'),
    path('authors/<int:pp>/update', AuthorUpdateView.as_view(), name='aut_upd'),
    path('authors/<int:pp>/del', AuthorDeleteView.as_view(), name='del_upd'),
]
