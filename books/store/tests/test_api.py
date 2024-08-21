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

    # функция запускаеться каждый раз перед запуском одного из наших тестов test_get снизу
    def setUp(self):
        self.book1 = Book.objects.create(
            name="Test book 1 ", price=25, author_name="Author 1"
        )
        self.book2 = Book.objects.create(
            name="Test book 2 ", price=55, author_name="Author 5"
        )
        self.book3 = Book.objects.create(
            name="Test book Author 1", price=55, author_name="Author 2"
        )

    # проверяем GET запрос для нашего api
    def test_get(self):

        # reverse(basename_from_router , args=[]) генерирует url запрос с указаными в нем параметрами
        # "book" к basename нужно добавлять ->
        # -list    если хотим получить список
        # -detail  если хотим получить одну запись
        url = reverse("book-list")  # -> /book/

        # self.client дает APITestCase
        response = self.client.get(url)  # -> 127.0.0.1:8000/book/

        # возвращает ответ на наш get запрос
        print(
            response.data
        )  # -> [{'id': 1, 'name': 'Test book 1 ', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2 ', 'price': '30.00'}]

        # many=True указывает что мы передаем список обьектов [self.book1, self.book2]
        serializer_data = BookSerializer(
            [self.book1, self.book2, self.book3], many=True
        ).data

        # status.HTTP_200_OK хранит просто код ответ 200
        # response.status_code хранит код статуса ответа от сервера на наш текущий get-запрос
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # print(f"{status.HTTP_200_OK}  1111")
        # print(f"{response.status_code}  222")
        self.assertEqual(serializer_data, response.data)

    # проводит тестирование поиска search в url
    def test_get_search(self):

        url = reverse("book-list")
        response = self.client.get(
            url, data={"search": "Author 1"}
        )  # -> 127.0.0.1:8000/book/?search=Author 1
        serializer_data = BookSerializer([self.book1, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
