# Файл содержит сериализаторы для Django Rest

# default django
from store.models import Book

# django rest
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    # Meta позволяет работать с моделями(базами данных) django текущего проекта
    class Meta:
        # model обьединяем текущий сериализатор с моделью Books
        model = Book
        # fields указывает с какими полями из модели будет взаемодействовать сериализатор
        # fields = ("id", "name", "price")
        fields = "__all__"
