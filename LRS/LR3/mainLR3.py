from typing import Callable, Union, Dict, Any


class TreeHeightError(Exception):
    """Ошибка высоты дерева"""
    pass


def gen_bin_tree(
    root: int = 8,
    height: int = 4,
    left_leaf: Callable[[float], float] = lambda x: x + x/2,  
    right_leaf: Callable[[float], float] = lambda y: y**2
) -> Union[Dict[str, Any], int]:
    
    """ Генерация бинарного  дерева

    Args:
    root: Корень дерева. Default 8.
    height: Высота дерева. Default 4.
    left_leaf: Функция левого поддерева. Default lambda x: x + x/2.
    right_leaf: Функция правого поддерева. Default lambda y: y**2.

    """

    
    if height < 0:
        raise TreeHeightError("Высота дерева не может быть отрицательной")
    

    if height == 0:
        return root

    left_child = left_leaf(root)
    right_child = right_leaf(root)

    return {
        'root': root,
        'left': gen_bin_tree(left_child, height-1, left_leaf, right_leaf),
        'right': gen_bin_tree(right_child, height-1, left_leaf, right_leaf)
    }
