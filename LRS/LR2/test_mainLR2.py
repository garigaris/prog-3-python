from FindSumTwo import findSum
import unittest


# Тесты
class TestMath(unittest.TestCase):
    def test_rigth_2el(self):
        self.assertEqual(findSum([2, 3], 5), [0, 1])
    def test_two_same_elements(self):
        self.assertEqual(findSum([3, 3], 6), [0, 1])
    
    def test_three_elements(self):
        self.assertEqual(findSum([1, 2, 3], 5), [1, 2])
    
    def test_four_elements(self):
        self.assertEqual(findSum([4, 5, 6, 7], 11), [0, 3])
    
    def test_duplicate_numbers(self):
        self.assertEqual(findSum([3, 3, 4], 6), [0, 1])
    
    def test_large_numbers(self):
        self.assertEqual(findSum([100, 200, 300], 500), [1, 2])
    
    def test_no_solution(self):
        self.assertEqual(findSum([1, 2, 3], 10), "Пара не найдена")
    
    def test_single_element(self):
        self.assertEqual(findSum([5], 5), "Неверные данные массива")
    
    def test_empty_array(self):
        self.assertEqual(findSum([], 5), "Неверные данные массива")
    
    def test_negative_target(self):
        self.assertEqual(findSum([1, 2, 3], -5), "Неверные данные target")
    
    def test_string_target(self):
        self.assertEqual(findSum([1, 2, 3], "5"), "Неверные данные target")
    
    def test_not_array(self):
        self.assertEqual(findSum("hello", 5), "Неверные данные массива")
    
    def test_float_target(self):
        self.assertEqual(findSum([1, 2, 3], 5.5), "Неверные данные target")


# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)