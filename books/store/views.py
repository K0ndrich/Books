# default django
from django.shortcuts import render

# django rest
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# my_project
from store.models import Book
from store.serializers import BookSerializer


# API представления для работы сериализаторов с моделями django
class BookViewSet(ModelViewSet):
    # queryset указывает какие данные будем возвращать из модели django
    queryset = Book.objects.all()
    # serializer_class указывает каким сериализатором будем обрабатывать данные
    serializer_class = BookSerializer

    # фильтрация данных которые будут возвращаться сервером через API
    # указываем какой фильтр будем использовать
    filter_backends = [DjangoFilterBackend]
    # указывает по каким полям модели будем фильтровать данные
    filter_fields = ["price"]
