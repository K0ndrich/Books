# Проводим тестирование API


# django
from django.urls import reverse

# django_rest
from rest_framework.test import APITestCase
from rest_framework import status

# my_project
from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):

    # проверяем GET запрос для нашего api
    def test_get(self):

        book1 = Book.objects.create(name="Test book 1 ", price=25)
        book2 = Book.objects.create(name="Test book 2 ", price=30)

        # reverse(basename_from_router , args=[]) генерирует url запрос с указаными в нем параметрами
        # "book" к basename нужно добавлять ->
        # -list    если хотим получить список
        # -detail  если хотим получить одну запись
        url = reverse("book-list")  # -> /book/

        # self.client дает APITestCase
        response = self.client.get(
            url
        )  # -> <Response status_code=200, "application/json">

        # возвращает ответ на наш get запрос
        print(
            response.data
        )  # -> [{'id': 1, 'name': 'Test book 1 ', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2 ', 'price': '30.00'}]

        # many=True указывает что мы передаем список обьектов [book1, book2]
        serializer_data = BookSerializer([book1, book2], many=True).data

        # status.HTTP_200_OK хранит просто код ответ 200
        # response.status_code хранит код статуса ответа от сервера на наш текущий get-запрос
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print(f"{status.HTTP_200_OK}  1111")
        print(f"{response.status_code}  222")
        self.assertEqual(serializer_data, response.data)
