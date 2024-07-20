from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author',)
    search_fields = ('title', 'author', 'description')
    ordering = ('updated_at', 'created_at', 'title', 'price')
admin.site.register(Book, BookAdmin)