# Лабораторная работа: "Сумма двух"

## Описание задачи

Дан массив целых чисел nums и целочисленное значение переменной target , верните индексы двух чисел таким образом, чтобы они в сумме давали target. У каждого входного набора может не быть решений и может быть только одно решение, если есть элементы дающие в сумме target. Вы не можете  использовать один и тот же элемент дважды (и соответственно индекс тоже). Вы можете вернуть ответ в любом порядке нахождения индексов.

## Требования

- Вернуть индексы двух чисел, сумма которых равна `target`
- Не использовать один и тот же элемент дважды
- Учесть, что решения может не существовать
- Решение должно быть только одно (если существует)


## Реализация

### Функция `findSum`

```python
def findSum(array, target):
    if len(array) < 2 or type(array) != list:
        return "Неверные данные массива"
    if type(target) != int or target < 0:
        return "Неверные данные target"
    for firstNum in range(0, len(array)):
        for secondNum in range(firstNum + 1, len(array)):
            if (array[firstNum] + array[secondNum]) == target:
                result = [firstNum, secondNum]
                return result 
    return "Пара не найдена"
```

## Тестирование
Было реализовано 13 тестов, которые прошли успешно.

```python
test_duplicate_numbers (__main__.TestMath.test_duplicate_numbers) ... ok
test_empty_array (__main__.TestMath.test_empty_array) ... ok
test_float_target (__main__.TestMath.test_float_target) ... ok
test_four_elements (__main__.TestMath.test_four_elements) ... ok
test_large_numbers (__main__.TestMath.test_large_numbers) ... ok
test_negative_target (__main__.TestMath.test_negative_target) ... ok
test_no_solution (__main__.TestMath.test_no_solution) ... ok
test_not_array (__main__.TestMath.test_not_array) ... ok
test_rigth_2el (__main__.TestMath.test_rigth_2el) ... ok
test_single_element (__main__.TestMath.test_single_element) ... ok
test_string_target (__main__.TestMath.test_string_target) ... ok
test_three_elements (__main__.TestMath.test_three_elements) ... ok
test_two_same_elements (__main__.TestMath.test_two_same_elements) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```
# 📂 Структура программы

Программа разделена на несколько файлов:

FindSumTwo — функция поиска \
test_LR2 — тесты \
mainLR2 — основной запуск программы \
GetValueFromInput — получение данных от пользователя
