# Проводим Тестирование
# Используем Unittest

from django.test import TestCase
from store.logic import operations

# terminal -> python manage.py test store
class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, "+")
        # .assertEqual (my_value1 , my_value2)  # -> True(False) Проверяте на равенство == двох значений
        self.assertEqual(19, result)
        print("test_plus - test_plus - test_plus")

    def test_minus(self):
        result = operations(6, 13, "-")
        self.assertEqual(-7, result)
        print("test_minus - test_minus - test_minus")

    def test_multiply(self):
        result = operations(6, 13, "*")
        self.assertEqual(78, result)
        print("test_minus - test_minus - test_minus")
