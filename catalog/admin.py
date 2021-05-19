from django.contrib import admin
from .models import *

# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksInline(admin.TabularInline):
    model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #list_display = ('id','book','status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
    (None, {
        'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back')
    }),
)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines=[BooksInline]

    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

