
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
    
