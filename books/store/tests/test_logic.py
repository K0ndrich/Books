# Проводим Тестирование
# Используем Unittest

from django.test import TestCase
from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, "+")
        # .assertEqual (my_value1 , my_value2)  # -> True(False) Проверяте на равенство == двох значений
        self.assertEqual(19, result)
        print("-123-1-3-1-31-23-13-12-3")
