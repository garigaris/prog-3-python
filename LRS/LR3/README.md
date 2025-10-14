
# Лабораторная работа №3  
## Тема: Рекурсивная генерация бинарного дерева  

### Цель работы  
Реализовать программу для рекурсивного построения бинарного дерева с настраиваемыми параметрами.  





---

## Основной модуль:

```python
class TreeHeightError(Exception):
    """Ошибка высоты дерева"""
    pass


def gen_bin_tree(
    root: int = 8,
    height: int = 4,
    left_leaf: Callable[[float], float] = lambda x: x + x/2,  
    right_leaf: Callable[[float], float] = lambda y: y**2
) -> Union[Dict[str, Any], int]:
    
    """ Генерация бинарного дерева

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
````

---

## Тесты: 

```python
test_height_zero_returns_root (__main__.TestBinaryTree.test_height_zero_returns_root)
Тест 2: Высота 0 возвращает только корень ... ok

test_negative_height_raises_exception (__main__.TestBinaryTree.test_negative_height_raises_exception)
Тест 3: Отрицательная высота вызывает исключение ... ok

test_normal_case_height_1 (__main__.TestBinaryTree.test_normal_case_height_1)
Тест 1: Нормальный случай с высотой 1 ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## Пример вывода

Вызов:

```python
gen_bin_tree(root=8, height=2)
```

Результат:

```python
{
    "root": 8,
    "left": {
        "root": 12.0,
        "left": 18.0,
        "right": 144
    },
    "right": {
        "root": 64,
        "left": 96.0,
        "right": 4096
    }
}
```

---




