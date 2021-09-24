from django.contrib import admin

from .models import Author, Book, Publisher, Quote, QuoteAuthor, Store


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'age']
    search_fields = ['name']
    list_display = ['name', 'age']
    list_filter = ('age',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']
    inlines = [
        BookInline,
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('rating',)
    list_display = ['name', 'rating', 'price', 'pubdate']
    fields = ('name', ('pages', 'price', 'rating'), 'authors', 'publisher', 'pubdate')
    search_fields = ['name']
    # raw_id_fields = ['authors']
    date_hierarchy = 'pubdate'
    filter_horizontal = ['authors']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['name', 'books']
    search_fields = ['name']
    list_filter = ('name',)
    filter_horizontal = ['books']


@admin.register(Quote)
class Quote(admin.ModelAdmin):
    fields = ['quote', 'author']
    search_fields = ['quote']
    list_filter = ('author',)


@admin.register(QuoteAuthor)
class QuoteAuthor(admin.ModelAdmin):
    fields = ['name', 'description']
    search_fields = ['name']
    list_filter = ('name',)
