from typing import Callable, Dict, List

class ValidationError(Exception):
    pass


BinaryTreeType = Dict[int, List["BinaryTreeType"]]


def _gen_bin_tree_without_validation(root: int = 8,
                                     height: int = 4,
                                     left_leaf: Callable[[int], int] = lambda x: x + x // 2,
                                     right_leaf: Callable[[int], int] = lambda y: y ** 2) -> BinaryTreeType:

    """
    Генерирует бинарное дерево в виде словаря.

    Args:
        root: Корень дерева. По умолчанию 8.
        height: Высота дерева. По умолчанию 3.
        left_leaf: Функция для вычисления значения левого потомка. 
                  По умолчанию lambda x: x * 2.
        right_leaf: Функция для вычисления значения правого потомка. 
                   По умолчанию lambda y: y + 1.

    Returns:
        Tree: Бинарное дерево в формате {value: [left_child, right_child]}, 
              где left_child и right_child имеют такую же структуру.

    Raises:
        ValidationError: Если параметры не проходят валидацию.
    """

    if not isinstance(height, int):
        raise ValidationError("height должна быть целым числом")
    if not isinstance(root, int):
        raise ValidationError("root должен быть числом")
    if height < 0:
        raise ValidationError("height дерева не может быть отрицательной")
    if not callable(left_leaf) or not callable(right_leaf):
        raise ValidationError("left_leaf и right_leaf должны быть функциями")
    if height == 0:
        return {root: []}

    lst = [[] for _ in range(height + 1)]
    lst[0].append(str(root))
    for level in range(1, height + 1):
        countOfChildren = 2 ** level
        for i in range(0, countOfChildren, 2):
            stringLeft = str(left_leaf(int(lst[level - 1][i // 2])))
            stringRight = str(right_leaf(int(lst[level - 1][i // 2])))
            lst[level].append(stringLeft)
            lst[level].append(stringRight)

    

    res = [[] for _ in range(len(lst))]  
    res[0] = [{lst[0][0]: []}] 
    for level in range(1, len(lst)): # пробегаемся по уровням/level'ам  начиная с 1 
        for i in range(0, len(lst[level]), 2):  # будем на каждом level'e брать по 2 элемента (i, i + 1)
            
            parent_index = i // 2 # находим индекс родителя для 0 и 1 это будет 0 (0 // 2 = 0, 1 // 2 = 0) для 2 и 3 это будет 1 (2 // 2 = 1, 3 // 2 = 1) и т.д.
            parent_root = res[level-1][parent_index] # {8: []}
            
            parent_key = list(parent_root.keys())[0] # 8 / 8
        
            child_node_l = {lst[level][i]: []} 
            child_node_r = {lst[level][i+1]: []} 
            
            parent_root[parent_key] = [child_node_l] # создаем сначала список и помещаем туда child_node_l = {l(root): []}
            parent_root[parent_key].append(child_node_r) # потом добавляем child_node_r = {r(root): []}
                
            res[level].append(child_node_l) 
            res[level].append(child_node_r)

    return res[0][0]




def gen_bin_tree(root: int = 8,
                 height: int = 4,
                 left_leaf: Callable[[int], int] = lambda x: x + x // 2,
                 right_leaf: Callable[[int], int] = lambda y: y ** 2):
    try:
        result = _gen_bin_tree_without_validation(root, height, left_leaf, right_leaf) 
        return result
    except ValidationError as e:
        print(e)
        return None


