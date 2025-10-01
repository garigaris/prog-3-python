print("Введите количество элементов списка")
n = int(input())

array = []
for i in range (n):
    temp = int(input())
    array.append(temp)

print("Введите искомое число")
target = int(input())
result = []

print(array, target)
def findSum(array, target):
    for firstNum in range(0, len(array)):
        for secondNum in range(firstNum + 1, len(array)):
            if (array[firstNum] + array[secondNum]) == target:
                m = [firstNum, secondNum]
                result.append(m)
    return result  

print(findSum(array, target))


                
                