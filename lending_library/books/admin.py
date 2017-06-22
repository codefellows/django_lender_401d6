from django.contrib import admin
from books.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'isbn')
    list_filter = ('title', )


admin.site.register(Book, BookAdmin)
