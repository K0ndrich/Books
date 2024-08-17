from django.shortcuts import render

# django


# django_rest
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# my_project
from store.serializers import BookSerializer
from store.models import Book


# API представление
class BookViewSet(ModelViewSet):

    # queryset указывает какие записи из таблици будет возвращать api
    queryset = Book.objects.all()

    # указываем какой сериализатор будем использовать
    serializer_class = BookSerializer

    # добавляем фильтрацию возвращаемых значений для django_rest
    filter_backends = (DjangoFilterBackend,)
    # указываем по каким полям будем фильтроватть значения в url адресе браузера
    filter_fields = ["price"]  # -> http://127.0.0.1:8000/book/?price=1000
