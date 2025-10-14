import unittest
from mainLR3 import gen_bin_tree, TreeHeightError


class TestBinaryTree(unittest.TestCase):

    def test_normal_case_height_1(self):
        """Тест 1: Нормальный случай с высотой 1"""
        result = gen_bin_tree(root=8, height=1)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['root'], 8)
        
        # Левый потомок = 8 + 8/2 = 12.0
        self.assertIsInstance(result['left'], float)
        self.assertEqual(result['left'], 12.0)

        # Правый потомок = 8**2 = 64
        self.assertIsInstance(result['right'], (int))
        self.assertEqual(result['right'], 64)

    def test_height_zero_returns_root(self):
        """Тест 2: Высота 0 возвращает только корень"""
        result = gen_bin_tree(height=0)
        self.assertEqual(result, 8)

    def test_negative_height_raises_exception(self): 
        """Тест 3: Отрицательная высота вызывает исключение""" 
        with self.assertRaises(TreeHeightError) as context: 
            gen_bin_tree(height=-1) 
        self.assertTrue('Высота дерева не может быть отрицательной' in str(context.exception))


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
