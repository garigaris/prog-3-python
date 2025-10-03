
def findSum(array, target):
    for firstNum in range(0, len(array)):
        for secondNum in range(firstNum + 1, len(array)):
            if (array[firstNum] + array[secondNum]) == target:
                result = [firstNum, secondNum]
                return result 
    
