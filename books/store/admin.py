# default django 
from django.contrib import admin
from django.contrib.admin import ModelAdmin
# my_project
from store.models import Book

# регистрация и настройка модели Book в админ панели сайта
@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass