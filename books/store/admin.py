
# django
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# my_project
from store.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
