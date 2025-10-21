import unittest
from GenerateBinaryTree import gen_bin_tree, ValidationError, _gen_bin_tree_without_validation


class TestBinaryTree(unittest.TestCase):

    def test_normal_case_height_2(self):
        """Тест 1: Нормальный случай с высотой 2"""
        result = gen_bin_tree(root=8, height=2)
        self.assertEqual(result, {8: [{12: [{18: []}, {144: []}]}, {64: [{96: []}, {4096: []}]}]})
        
    def test_zhukov_normal_case(self):
        """Тест 2: Специфические функции как у Жукова"""
        result = gen_bin_tree(
            root=5, 
            height=3, 
            left_leaf=lambda x: x + 1,
            right_leaf=lambda x: x ** 2
        )
        expected = {
            5: [
                {6: [
                    {7: [
                        {8: []},
                        {49: []}
                    ]},
                    {36: [
                        {37: []},
                        {1296: []}
                    ]}
                ]},
                {25: [
                    {26: [
                        {27: []},
                        {676: []}
                    ]},
                    {625: [
                        {626: []},
                        {390625: []}
                    ]}
                ]}
            ]
        }
        self.assertEqual(result, expected)

    def test_height_not_int(self):
        """Тест 3: height не целое число вызывает ValidationError"""
        result = gen_bin_tree(height="5")
        self.assertEqual(result, None)

    def test_root_not_int(self):
        """Тест 4: root не число вызывает ValidationError"""
        result = gen_bin_tree(root='12')
        self.assertEqual(result, None)
    def test_negative_height(self):
        """Тест 5: отрицательная height вызывает ValidationError"""
        with self.assertRaises(ValidationError) as context:
            _gen_bin_tree_without_validation(height=-1)
        self.assertEqual(str(context.exception), "height дерева не может быть отрицательной")
    def test_is_left_and_right_function(self):
        with self.assertRaises(ValidationError) as context:
            _gen_bin_tree_without_validation(left_leaf=2, right_leaf={})
        self.assertEqual(str(context.exception), "left_leaf и right_leaf должны быть функциями")

    
        
       

   
        

if __name__ == '__main__':
    unittest.main()