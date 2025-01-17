# default django
from django.shortcuts import render

# django rest
from rest_framework.viewsets import ModelViewSet

# my_project
from store.models import Book
from store.serializers import BookSerializer


# API представления для работы сериализаторов с моделями django
class BookViewSet(ModelViewSet):
    # queryset указывает какие данные будем возвращать из модели django
    queryset = Book.objects.all()
    # serializer_class указывает каким сериализатором будем обрабатывать данные
    serializer_class = BookSerializer
