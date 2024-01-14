import math

trap_sq = lambda a, b, h: 0.5 * (a + b) * h

circle_sq = lambda r: math.pi * r ** 2

rec_sq = lambda l, w: l * w

print("Площадь трапеции для a=7,b=5,h=3: ", trap_sq(7, 5, 3))
print("Площадь прямоугольника 10*13: ", rec_sq(10, 13))
print("Площадь окружности с радиусом 2: ", circle_sq(2))
