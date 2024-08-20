from django.shortcuts import render

# django


# django_rest
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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
    filter_backends = [DjangoFilterBackend, SearchFilter]

    # указываем по каким полям будем фильтроватть значения в url адресе браузера
    filterset_fields = ["price"]  # -> 127.0.0.1:8000/book/?price=1000

    # указываем поля для поисковой фильтрации сразу по нескольким параметрам
    # ищет указаное значение my_value во всех указаных колонках в search_fields = ["name", "author_name"]
    search_fields = ["name", "author_name"]  # -> 127.0.0.1:8000/book/?search=my_value
