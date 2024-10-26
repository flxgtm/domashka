import math

def factorial(n: int) -> int:
    """
    вычисление факториала числа n.
    :param n: целое число, для которого вычисляется факториал.
    :return: факториал числа n.
    """
    if n < 0:
        raise ValueError("факториал для отрицательных чисел не определен")
    return math.factorial(n)

def permutations(n: int, k: int) -> int:
    """
    вычисление количества перестановок P(n, k) из n элементов по k.
    :param n: общее количество элементов.
    :param k: количество элементов в каждой перестановке.
    :return: количество перестановок.
    """
    if k > n:
        raise ValueError("количество выбранных элементов не может превышать количество элементов множества")
    return factorial(n) // factorial(n - k)

def combinations(n: int, k: int) -> int:
    """
    вычисление количества сочетаний C(n, k) из n элементов по k.
    :param n: общее количество элементов.
    :param k: количество элементов в каждом сочетании.
    :return: количество сочетаний.
    """
    if k > n:
        raise ValueError("количество выбираемых элементов не может превышать количество элементов в множестве")
    return factorial(n) // (factorial(k) * factorial(n - k))

def variations(n: int, k: int) -> int:
    """
    вычисление количества размещений A(n, k) из n элементов по k.
    :param n: общее количество элементов.
    :param k: количество элементов в каждом размещении.
    :return: количество размещений.
    """
    if k > n:
        raise ValueError("количество выбираемых элементов не может превышать количество элементов в множестве")
    return factorial(n) // factorial(n - k)

if __name__ == "__main__":
    print("запустите файл main.py для выбора функций")
