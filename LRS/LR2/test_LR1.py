from FindSumTwo import findSum
import unittest


# Тесты
class TestMath(unittest.TestCase):
    def test_rigth_2el(self):
        self.assertEqual(findSum([2, 3], 5), [0, 1])
    



# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)