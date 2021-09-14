from django.contrib import admin

from .models import Author, Book, Publisher, Store


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'age']
    list_filter = ('age',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [
        BookInline,
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('name', ('pages', 'price', 'rating'), 'authors', 'publisher', 'pubdate')
    date_hierarchy = 'pubdate'
    list_filter = ('rating',)
    filter_horizontal = ['authors']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['name', 'books']
    list_filter = ('name',)
    filter_horizontal = ['books']
