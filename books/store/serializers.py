# Внутри файла храняться сериализаторы

# django_rest
from rest_framework.serializers import ModelSerializer

# my_project
from store.models import Book


# сериализатор для роботы с моделью Django
class BookSerializer(ModelSerializer):
    class Meta:
        # указываем сериализатору с какой моделью django будем взаемодействовать
        model = Book
        # указываем поля модели с которыми будем работать
        # fields = ("id", "name" , "price") также может быть
        fields = "__all__"
