# Тестируем наш API из django rest

# default django
from django.urls import reverse

# django rest
from rest_framework.test import APITestCase
from rest_framework import status

# my_project
from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):

    # функция setUp будет запускаться каждый раз перед запуском всех остальных функций ниже
    def setUp(self):

        # добавление атрибутов для созданого класса
        # создание временных полей модели для тестирования выполнения views
        self.book_1 = Book.objects.create(
            name="Test book 1", price="25", author_name="Author 1"
        )
        self.book_2 = Book.objects.create(
            name="Test book 2", price="55", author_name="Author 5"
        )
        self.book_3 = Book.objects.create(
            name="Test book Author 1", price="55", author_name="Author 2"
        )

    # тестируем GET-запрос к серверу
    def test_get(self):

        # reverse возвращает целый url-путь по указаному его пути из
        # router.register(r"book", BookViewSet)   или   path('new-path/', views.new_view, name='book'),
        url = reverse(
            "book-list"
        )  # -list возвращет список из елементов, -detail возвращает один елемент
        # print(url)  # -> /book/

        # self.client.get(url) отпраляем get-запрос на сервер и даем етот ответ пользователю
        response = self.client.get(url)

        # BookSerializer([book_1, book_2]) передаем внутрь сериализатора список обьектов
        #  many=True указывает, что передаем список елементов, а не один елемент
        # .data возвращает только данные
        serializer_data = BookSerializer(
            [self.book_1, self.book_2, self.book_3], many=True
        ).data
        # status хранит все значения ответов от сервера
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        # print(response)  # -> <Response status_code=200, "application/json">
        # print(response.data)  # -> [{'id': 1, 'name': 'Test book 1', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2', 'price': '30.00'}]

    # тестируем выполнение функции фильтрации возвращаемых данных из модели через API
    # /book/?price=500
    def test_filter(self):

        url = reverse("book-list")

        response = self.client.get(
            url, data={"price": 55}
        )  # -> 127.0.0.1:8000/book/?price=500

        serializer_data = BookSerializer([self.book_2, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # book/?search=500
    def test_get_search(self):

        url = reverse("book-list")

        response = self.client.get(
            url, data={"search": "Author 1"}
        )  # -> 127.0.0.1:8000/book/?search=Hemingway

        serializer_data = BookSerializer([self.book_1, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
