# Внутри файла храняться сериализаторы

# подключем родительский класс сериализатора
from rest_framework.serializers import ModelSerializer

# подключем свою модель django
from store.models import Book


# сериализатор для роботы с моделью Django
class BookSerializer(ModelSerializer):
    class Meta:
        # указываем сериализатору с какой моделью django будем взаемодействовать
        model = Book
        # указываем поля модели с которыми будем работать
        fields = "__all__"
