def getValueFromInput():
    try:
        print("Введите количество элементов списка:")
        n = int(input())
        array = []
        for i in range(n):
            print(f"Введите элемент {i+1}:")
            temp = int(input())
            array.append(temp)
        print("Введите target:")
        target = int(input())
        return array, target
    except ValueError:
        print("Ошибка: введите целое число!")
        return getValueFromInput()