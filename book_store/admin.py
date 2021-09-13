from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorInline(admin.ModelAdmin):
    fields = ['name', 'age']


@admin.register(Publisher)
class PublisherInline(admin.ModelAdmin):
    fields = ['name']


@admin.register(Book)
class BookInline(admin.ModelAdmin):
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']


@admin.register(Store)
class StoreInline(admin.ModelAdmin):
    fields = ['name', 'books']
