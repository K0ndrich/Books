# Создание моделей(таблиц для базы данных)


# django
from django.db import models


class Book(models.Model):
    # создаем поля для таблици c именем Book
    # models.CharField символьное значение
    name = models.CharField(max_length=255)
    # models.DecimalField число с плавающей запятой от + до - , max_digits - максимальная длина числа , decimal_places - сколько чисел после запятой
    price = models.DecimalField(max_digits=7, decimal_places=2)

    author_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"id : {self.id} / {self.name}"
