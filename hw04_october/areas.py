import math

def rectangle_area(length: float, width: float) -> float:
    """
    вычисление площади прямоугольника.
    :param length: длина прямоугольника.
    :param width: ширина прямоугольника.
    :return: площадь прямоугольника.
    """
    if length < 0 or width < 0:
        raise ValueError("длина и/или ширина должны быть неотрицательными")
    return length * width

def square_area(side: float) -> float:
    """
    вычисление площади квадрата.
    :param side: сторона квадрата.
    :return: площадь квадрата.
    """
    if side < 0:
        raise ValueError("сторона квадрата должна быть неотрицательной")
    return side * side

def triangle_area(base: float, height: float) -> float:
    """
    вычисление площади треугольника.
    :param base: основание треугольника.
    :param height: высота треугольника.
    :return: площадь треугольника.
    """
    if base < 0 or height < 0:
        raise ValueError("основание и высота должны быть неотрицательными")
    return 0.5 * base * height

def sphere_area(radius: float) -> float:
    """
    вычисление площади поверхности шара.
    :param radius: радиус шара.
    :return: площадь поверхности шара.
    """
    if radius < 0:
        raise ValueError("радиус должен быть неотрицательным")
    return 4 * math.pi * radius ** 2

if __name__ == "__main__":
    print("запустите файл main.py для выбора функций")
