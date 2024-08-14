from django.shortcuts import render

# импортируем представление для нашего api
from rest_framework.viewsets import ModelViewSet

# импортируем свой сериализатор
from store.serializers import BookSerializer

# импортируем свою модель
from store.models import Book


# API представление
class BookViewSet(ModelViewSet):
    # queryset указывает какие записи из таблици будет возвращать api
    queryset = Book.objects.all()
    # указываем какой сериализатор будем использовать
    serializer_class = BookSerializer
