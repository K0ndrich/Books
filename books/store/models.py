from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    # DecimalField ето числа с плавающей точкой
    # max_digits определяет общее количество цифр в числе
    # decimal_places определяет количество цифр после запятой
    price = models.DecimalField(max_digits=7, decimal_places=2)

    author_name = models.CharField(max_length=255)

    # указывает отображение в админ панели
    def __str__(self):
        return f"ID {self.id} : {self.name}"
