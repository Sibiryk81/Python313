import math


def sq_fig():
    fig = int(input(" 1 - прямоугольник,\n 2 - треугольник,\n 3 - круг\nВыберите фигуру: "))
    print(fig)
    if fig == 1:
        h = int(input("Ширина: "))
        w = int(input("Высота: "))
        area = h * w
        print("Площадь прямоугольника = ", area)
    elif fig == 2:
        h = int(input("Основание: "))
        w = int(input("Высота: "))
        area = h * w * 0.5
        print("Площадь треугольника = ", area)
    elif fig == 3:
        h = int(input("Радиус: "))
        area = math.pi * h ** 2
        print("Площадь круга = ", round(area, 2))
    else:
        print("Не корректный ввод")
    return


sq_fig()
