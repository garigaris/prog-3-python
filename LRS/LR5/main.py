import timeit
import matplotlib.pyplot as plt
from factorial_iterative import factorial_iterative
from factorial_recursive import factorial_recursive



def benchmark(func, data, number=1, repeat=5):
    """Возвращает среднее время выполнения func на наборе data"""
    total = 0
    for n in data:
        times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
        total += min(times)  # берём минимальное время из серии
    return total / len(data)


def main():
    # фиксированный набор данных
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []

    for n in test_data:
        res_recursive.append(benchmark(factorial_recursive, [n], number=10000, repeat=5))
        res_iterative.append(benchmark(factorial_iterative, [n], number=10000, repeat=5))

    # Визуализация
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала без кэширования")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
