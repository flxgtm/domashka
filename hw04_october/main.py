from my_math import (
    factorial,
    permutations,
    combinations,
    variations,
    rectangle_area,
    square_area,
    triangle_area,
    sphere_area,
)


def main():
    while True:
        print("выберите модуль:")
        print("1. комбинаторика")
        print("2. геометрия")
        print("3. выйти")
        
        choice = input("введите номер: ")

        if choice == "1":
            print("доступные функции комбинаторики: факториал, перестановки, сочетания, размещения")
            func_choice = input("введите название функции: ")
        
            if func_choice == "факториал":
                n = int(input("введите n: "))
                print(f"факториал {n} равен {factorial(n)}")
        
            elif func_choice == "перестановки":
                n = int(input("введите n: "))
                k = int(input("введите k: "))
                print(f"число перестановок C({n}, {k}) равно {permutations(n, k)}")
        
            elif func_choice == "сочетания":
                n = int(input("введите n: "))
                k = int(input("введите k: "))
                print(f"число  сочетаний A({n}, {k}) равно {combinations(n, k)}")

            elif func_choice == "размещения":
                n = int(input("введите n: "))
                k = int(input("введите k: "))
                print(f"число размещений A({n}, {k}) равно {variations(n, k)}")
        
            else:
                print("функция не найдена")

        elif choice == "2":
            print("доступные функции геометрии: площадь прямоугольника, площадь квадрата, площадь треугольника, площадь поверхности шара")
            func_choice = input("введите название функции: ")
        
            if func_choice == "площадь прямоугольника":
                width = float(input("введите ширину: "))
                height = float(input("введите высоту: "))
                print(f"площадь прямоугольника: {rectangle_area(width, height)}")
        
            elif func_choice == "площадь квадрата":
                side = float(input("введите сторону квадрата: "))
                print(f"площадь квадрата: {square_area(side)}")
        
            elif func_choice == "площадь треугольника":
                base = float(input("введите основание треугольника: "))
                height = float(input("введите высоту треугольника: "))
                print(f"площадь треугольника: {triangle_area(base, height)}")
        
            elif func_choice == "площадь поверхности шара":
                radius = float(input("введите радиус шара: "))
                print(f"площадь поверхности шара: {sphere_area(radius)}")
        
            else:   
                print("функция не найдена")
                
        elif choice == "3":
            print("выход из программы")
            break
        
        else:
            print("неверный выбор")
        print()
        
if __name__ == "__main__":
    main()