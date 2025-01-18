# Проводим тестирование кода из файла logic.py
# Используем встроенных в Django модуль UnitTest
# В терминале -> python manage.py test store.tests.test_logic

# default django
from unittest import TestCase

# my_project
from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, "+")
        # assertEqual проверка на равенство 19 == result
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(6, 13, "-")
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operations(6, 13, "*")
        self.assertEqual(78, result)
