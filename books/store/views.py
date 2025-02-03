# default django
from django.shortcuts import render

# django rest
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated


# my_project
from store.models import Book
from store.serializers import BookSerializer


# API представления для работы сериализаторов с моделями django
class BookViewSet(ModelViewSet):
    # queryset указывает какие данные будем возвращать из модели django
    queryset = Book.objects.all()
    # serializer_class указывает каким сериализатором будем обрабатывать данные
    serializer_class = BookSerializer

    # разрешения для показа текущего views только для аутентифицированых пользователей
    # {"detail":"Authentication credentials were not provided."}
    permission_classes = [IsAuthenticated]

    # фильтрация данных которые будут возвращаться сервером через API
    # указываем какой фильтр будем использовать
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # указывает по каким полям модели будем фильтровать данные
    filterset_fields = ["price"]  # -> 127.0.0.1:8000/book/?price=500
    # указывает по каким полям будет осуществляться поиск елементов модели
    search_fields = ["name", "author_name"]  # -> 127.0.0.1:8000/book/?search=Hemingway
    ordering_fields = ["price", "author_name"]  # -> 127.0.0.1:8000/book/?ordering=price
    # -> 127.0.0.1:8000/book/?ordering=-price
    # -> 127.0.0.1:8000/book/?ordering=+price


def auth(request):
    return render(request, "oauth.html")
