# name = "Aleks"  # инициализация переменной
# print("Hello,", name)
# age = 20, 4
# print(age)
# text = "Hello"
# print(text + str(age))
# print(type(age))  # int-20, tuple - 20,4
# print(type(text))  # str - Hello
# a = True
# print(a)
# print(type(a))  # bool True False
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# import random
# import random
# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)

# c = a  # 1
# a = b  # 2
# b = c  # 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка\
#       символов")
# print('строка \n символов \n file.txt')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1,",", s2, "!")
# print(s3 * 3)

# print(2.439523948529348592345932485)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  #3.0
# print(6 // 2)  #3
# print(6 // 4)  #1
# print(6 ** 4)
# print(6 % 4)

# num = 10
# num += 5
# print(num)


# num = 4325
# print("Исходное число :", num)
# res = num % 10 * 1000
# num // 10
# res += num % 10 * 1
# print(res)

# num1 = 2.5
# num2 = 0
# # res = num1 + str(num2)   #20
# # res = int(num1) + num2   #2
# res = (int)num1 + num2
# print(res)

# print(int(3.8))
# print(round(3.8444, 2))
# print(type(round(3.893, 2)))

# name = "Виктор"
# age = 20
# print("Меня зовут: " + name + " мне " + str(age) + " лет")
# print("Меня зовут:", name, "мне", age, "лет", sep="11111", end=" \n\n")
# print("Я учу  Python")

# name = int(input("Введите число: "))
# # name = int(name)
# power = int(input("Введите степень: "))
# res = name ** power
# print(res)
# print(type(name))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))
# print(bool(0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == 7)
# print(2+5 == 7)
# print(2+5 != 10-3)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)  # True && True/True
# print(2 * 5 > 7 >= 4 + 3)  # True && True/True
# print(2 * 5 < 7 >= 4 + 3)  # False && True/False

# a = 20
# b = 5
# c = a == b
# print(a,b,c)   # 20,5,False

# print(5 - 3 == 2 and 1 + 4 == 5)  # True,True/True
# print(5 - 3 == 2 and 1 + 4 < 5)  # True, Falsr/False
# print(5 - 3 == 2 or 1 + 4 == 5)  # True, Falsr/True
# print(5 - 3 == 2 or 1 + 4 < 5)  # True, Falsr/True

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cut = 5
# if cut < 10:
#     cut +=2
#     print(cut)


# age = int(input("Введите возраст "))
# if age >= 18:
#    print("доступ разрешен")
# else:
#     print("доступ запрещен")

# a = 150
# b = 50
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# a = int(input("Первая сторона трекгольникаЖ "))
# b = int(input("Вторая сторона трекгольникаЖ "))
# c = int(input("Третья сторона трекгольникаЖ "))
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# day = int(input("Введите день недели цифрой: "))
# if day == 6 or day == 7:
#     print("Выходной", end=" ")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# elif 1 <= day <= 5:
#     print("Рабочий: ", end=" ")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# else:
#     print("Такого дня нет")

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
#     print("\nЦикл завершен")


# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break
# i += 1

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
#
# print(res)

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл закончен, i =", i)

# i = 1
# j = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, '*')
#     i += 1

# for i in range(9, 0, -1):
#     print(i, end=" ")
#
# print()
#
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число "))
# for i in range(11, 99 + 1, 11):
# if a % 11 == 0:
# print(i, end=" ")

# for i in range(1, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# a = int(input("Введите кол-во символов: "))
# s = input("Тип символа: ")
# b = int(input("0 - горизонт\n1 - вертикаль\n ориентация линий: "))
# i = 0
# while i < a:
#     if b == 0:
#         print(s, end=" ")
#     if b == 1:
#         print(s)
#     i += 1

# num = 57
# a = 0
# b = None
# while b != num and b != 0:
#     b = int(input("Введите целое число от 1 до 100: "))
#     if b == 0:
#         break
#     elif b < num:
#         print("Загаданное число больше")
#     elif b > num:
#         print("Загаданное число меньше")
#     a += 1
# if b == num:
#     print("Угадали за:", a, "попыток")

# for i in range(3):
#       print(i)
#       if i == 1:
#            break
# else:
#     print('done')


# for i in range(3):
#     print("+++ i=", i)
#     for j in range(2):
#         print("----- j =", j)

# w = int(input("Введите ширину"))
# h = int(input("Введите высоту"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

# nums = [letter for letter in "Banana"]
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# Список (list)
# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
# # print(nums[6]) #IndexError
# print(nums[-1])
# print(nums[-2])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums)
#
# #print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)

# s = []
# print(s)
#
# b = list("Hello")
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 11, 2)))

# (выражение for переменная in последовательность)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)
# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input('Введите количество элементов списка '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")  # a[i] = 10 20 30 40 50 60 70 80 90
# print()
#
# for i in a:
#      print(i + 2, end=" ")

# a = list(range(21, 41))
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         k += 1
#     else:
#         s += a[i]
# for i in a:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print(s)
# print(k)

# n = list(range(21, 41))
# print(n)
# a = 0
# print(n[a])
# print(n[a+1])
# print(n[a+2])

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)
# for i in range(len(a)):
#     # print(a[i], "-> ", end="")
#     # print(a[i - 1])
#     if a[i] < a[i + 1]:
#         print(a[i], end=" ")

# a = [int(input('-> ')) for _ in range(int(input('Введите количество знаков:  ')))]
# s = k = 0
# for i in a:
#     if i != 0:
#         s += i
#         k += 1
#         if k > 0:
#             a = s / k
# print("Среднее арифметическое ненулевых элементов: ", a)


# a = [int(input('-> ')) for _ in range(int(input('Введите количество знаков:  ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print([i])

# Срез
# Список[start:stop:step]

# a = [7, 8, 2, 1, 17]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# # print(a[1:4])
# # print(a[1:])
# # print(a[:3])
# print(a[5:2:-1])
# b = a[10:20]
# print(b)

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1:6:2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[-3:-6:-1])
# print(a[2:5])


# s[1:3] = [0, 0, 0, 0]
# print(s)
# #s[1:2] = [20]
# s[1] = 20
# print(s)
# #s[2:5] = []
# #del s[1]
# del s[:]
#
# print(s)

# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 5, 3])  # добавляет несколько элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100) # добавляет элемент в заданный индекс(кроме последнего)
# print(s)
# s.insert(20, 200)
# print(s)


# a = [5, 9, 7, 3, 2]
# b = [4, 3, 6, 2, 9]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c)


# a = [7, 6, 8, 9, 2]
# b = [4, 3, 6]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])


# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [5, 9, 3, 7, 1, 8, 9, 9]
# print(s)
# s.remove(9)  # удаляет по значению первое попавшееся
# print(s)
# s.pop()  # удаляет последний элемент из списка если без параметров
# a = s.pop(-1)  # передаем индекс для удаления элемента
# # print(s.pop(1))
# print(s)
# s.clear()  # очистка всех элементов списка
# print(s)


# numbers = [int(input('-> ')) for _ in range(int(input('n =')))]
#
# index = int(input('Введите индекс удаляемого элемента: '))
# numbers.pop(index)
# print(numbers)

# s = [5, 9, 3, 7, 1, 8, 9, 9]
# print(s)
# num = s.count(9)  # считает кол-во элементов
# print(num)
# if -9 in s:
#     ind = s.index(9)  # возвращает индекс первого попавшегося искомого элемента
#     print(ind)
# else:
#     print("не существует")
# ind = s.index(9, 2)
# print(ind)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# print(a)
#
# for i in a:
#     if a.count(i) == 1 and i not in b:
#         b.append(i)
# print(b)

# a = [1, 2, 3]
# b = a.copy()    #  копия списка
# print("a = ", a)
# print("b = ", b)
# a.append(20)
# print("a = ", a)
# print("b = ", b)
# b.append(120)
# print("a = ", a)
# print("b = ", b)


# a = [1, 2, 4, 6, 3]
# print(a)
# # a.reverse()     # перестраивает список в обратном порядке
# # # print(a.revers())
# # print(a)
#
# # a.sort()   # метод сортировки
# # print(a)
# a.sort(reverse=True)
# print(a)

# a = ["Виталий", "Андрей", "Коля", "Михаил", "Аня"]
# a.sort(key=len, reverse=True)
# print(a)
# a = [1, 2, 4, 6, 3]
# print(a)
# # a.sort()
# # print(a)
#
# sort = sorted(a)
# print(sort)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(1, 9))  # от 1 до 9 включительно
# print(random.randrange(1, 9, 2))  # от 1 до 9 не включая 9
# print(round(random.uniform(10.5, 25.5), 2))
#
# city = ["Mockow", "Novosibirsk", "Omsk", "Tumen", "Ekaterinburg"]
# print(random.choice(city))
# print(random.choices(city, k=3))
#
# s = [55, 66, 77, 88, 99, 44, 33, 22, 11]
# # print(random.choices(s, k=5))
# random.shuffle(city)
# print(city)

# lst = [5, 3, 4, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))


# a = 5
# print(a)
#
# s = [55, 66, 77, 88, 99, 44, 33, 22, 11]
# print(sum(s))


# import random
# mas = [random.randint(0,100) for i in range(10)]
# print(mas)
# m = max(mas)
# mas.remove(m)
# mas.insert(0, m)
# print(mas)


# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# lst[0] = max(lst)
# print(lst)


# ____________________________


# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
# # del lst[0: ind_min]
# print(lst[ind_min])

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)

# lst = [1]
# print(bool(lst))
# # if len(lst) == 0:

# if not lst:
#     print("Список пустой")
# else:
#     b = 5
#     print("есть элементы")
#
# print(b)

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# # a.extend(b)
# # print("Третий список: ", c)
#
# # c = []
# # d = []
# # for element in a:
# #     if element not in b and element not in d:
# #         d.append(element)
# # print('Элементы обоих списков без повторений:', d)
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print('Элементы обоих списков без повторений:', d)
#
# c = []
# for element in a:
#     if element in b and element not in c:
#         c.append(element)
#
# print('Элементы общие для двух списков:', c)
#
# min_max = [min(a), min(b), max(a),max(b)]
# print("Минимальные и максимальные значения обоих списков: ",min_max)

# n = [
#     [1, 2, 3, 4],
#     [9, 6, 7, 8],
#     [9, 11, 18, 13],
# ]

# n = ["Hello", "World"]
# print(n)
# print(len(n))
# print(n[1][2])
# print()
# for row in range(len(n)):
#     # print(n[row])
#     for cal in range(len(n[row])):
#         print(n[row][cal], end="\t")
#     print()
# for row in n:
#     for x in row:
#         print(x, end="\t")
#     print()

# row = [
#     [1, 2, 3, 4]
#     [5, 6, 7, 8]
#     [9, 7, 5, 10, 11]
# ]


# import random
# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)] for y in range(h)]

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# import random
# w, h = 4, 3
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# h = 0
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             h +=1
#     print()
# print(h)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import random

# w, h = 4, 3
# matrix = [[input("-> ") for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)


# import math as n
# from math import sqrt, ceil
# from math import *

# num1 = sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)

# import time
# import locale

# locale.setlocale(locale.LC_ALL,"")
#
# seconds = time.time()
# print("Кол-во секунд: ", seconds)
#
# local_time = time.ctime()
# print("Местное время", local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("сегодня: %B.%d.%Y"))
# print(time.strftime("%d.%m.%y, %H.%M.%S", time.localtime()))

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):   # аргументы
#     print("Hello", name)
#
#
# hello("Irina")   # параметры
# hello("Igor")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 6
# y = 5
# get_sum(x, y)
# get_sum("aaaa", "bbbbb")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "x", "0")

# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
#
# x = 6
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if a > b:
#         return one - two
#     else:
#         return one + two
#
#
# a = int(input("->: "))
# b = int(input("->: "))
# print(maximum(a, b))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе = ", cube(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     # print(lst)
#     # symbol1 = lst.pop(0)
#     # symbol2 = lst.pop()
#     # lst.append(symbol1)
#     # lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['s', 'l', 'o', 'n']))


# def is_great(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 5
# b = 10
# print(is_great(a, b))
# print(is_great(5, 10))
#
# if is_great(a, b):
#     print(a, ">", b)
# else:
#     print(b, ">", a)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный")
# else:
#     print("Ненадежный")


# __________


# def sum_of_even_or_odd(number, even=False):
#     additional = 0
#     if even:
#         while (number):
#             digit = number % 10
#             if digit % 2:
#                 additional += digit
#             number //= 10
#         return additional
#     else:
#         while (number):
#             digit = number % 10
#             if not (digit % 2):
#                 additional += digit
#             number //= 10
#         return additional
#
#
# print('Сумма чётных цифр для числа', 9874023, '=', sum_of_even_or_odd(9874023))
# print('Сумма нечётных цифр для числа', 9874023, '=', sum_of_even_or_odd(9874023, True))
# print()
# print('Сумма чётных цифр для числа', 38271, '=', sum_of_even_or_odd(38271))
# print('Сумма нечётных цифр для числа', 38271, '=', sum_of_even_or_odd(38271, True))
# print()
# print('Сумма чётных цифр для числа', 123456789, '=', sum_of_even_or_odd(123456789))
# print('Сумма нечётных цифр для числа', 123456789, '=', sum_of_even_or_odd(123456789, True))
# [13: 36] Губин
# Егор
# Вячеславович
#
#
# def sum_of_even_or_odd(number, even=False):
#     additional = 0
#     while (number):
#         digit = number % 10
#         if digit % 2 and even:
#             additional += digit
#         if not (digit % 2) and not (even):
#             additional += digit
#         number //= 10
#     return additional
#
#
# print('Сумма чётных цифр для числа', 9874023, '=', sum_of_even_or_odd(9874023))
# print('Сумма нечётных цифр для числа', 9874023, '=', sum_of_even_or_odd(9874023, True))
# print()
# print('Сумма чётных цифр для числа', 38271, '=', sum_of_even_or_odd(38271))
# print('Сумма нечётных цифр для числа', 38271, '=', sum_of_even_or_odd(38271, True))
# print()
# print('Сумма чётных цифр для числа', 123456789, '=', sum_of_even_or_odd(123456789))
# print('Сумма нечётных цифр для числа', 123456789, '=', sum_of_even_or_odd(123456789, True))


# def display_info(name, age):
#     print("Name", name, '\nAge:', age)
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23,name="Ira")
# display_info("Igor", age=23, name="Ira") #Typeerror


# Изменяемые и не изменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]

# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
#
# print(a == b)  # True
# print(a is b)  # True

# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)  # True
# print(n is m)  # True

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(id(n))
# print(n)


# Кортеж (tuple)


# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst. __sizeof__())   # 72
# print(tpl. __sizeof__())   # 48


# a = (8,)
# print(type(a))
# print(a)

# n = "Hello", "Python"
# b = tuple(("Hello", "Python"))
# print(type(b))
#
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])   # 4
# print(a[1:3])  # (2, 3)
# # a[1] = 3  # TipeError

# from random import randint
#
# # s = tuple(int(input("-> ")) for i in range(5))
# s = tuple(2 ** i for i in range(1, 13))
#
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("World")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t3.count('l'))
# # if 'l' in t3:
# #     print(t3.index('e'))
#
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, al):
#     if al in tpl:
#         if tpl.count(al) > 1:
#             # a = tpl.index(al)  # 1
#             # b = tpl.index(al, a + 1) + 1  # 4
#             # return tpl[a:b + 1]
#             return tpl[tpl.index(al):tpl.index(al), tpl.index(al) + 1) + 1]
#         else:
#             return tpl[tpl.index(al):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# print(first_name, year, married)


# a = tuple()
# for i in range(10):
#     a += (random.randint(0, 5), )
# print(a)
# b = tuple()
# for i in range(10):
#     b += (random.randint(-5, 0), )
# print(b)

# from random import randint


# def all_tuples(a):
#     t1 = tuple(random.randint(0, 5) for i in range(a))
#     t2 = tuple(random.randint(-5, 0) for i in range(a))
#     return t1, t2
#
#
# t1, t2 = all_tuples(10)
# print(t1)
# print(t2)
# c = t1 + t2
# print(c)
# print(c.count(0))


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 3.710))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end='\n\n')
# for countries in countries:
#     country_name, country_population, cities = countries
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("Город:", city_name, "население =", city_population)


#  Множества (Set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("Hello")
# print(a, type(a))

# c = ["red", "blue", "green", "black"]
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x * x for x in mas if x % 2 == 0}
#
# print(s)

# def to_set(a):
#     st = set(a)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "black"}
# # print("green" not in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in r if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {"Tom", "Bob", "Alice"}
# print(a)
# a.add("Ann")
# print(a)
# a.remove("Ann")  # при обращении к несуществующему элементу получаем ошибку KeyError
# print(a)
# user = "Ann"
# if user in a:
#     a.remove(user)
# print(a)

# a.discard("Ann")
# print(a)

# n = a.pop()
# print(n)
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = a - b
# a -= b
# c = a ^ b
# a ^= b


# print(c)
# print(a)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}


# # s = a.union(b, c, d, e, f, g)
# s = a | b | c | d | e | f | g
# print(s)
# count = len(s)
# print("Count", count)
# print("Min", min(s))
# print("Max", max(s))
# print(sum(s))

# s1 = "Hello"
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Света", "Женя", "Марина"}
# music = {"Илья", "Женя", "Костя"}
#
# one_hobby = drawing ^ music
# print("Один кружок", one_hobby)
#
# both_hobbies = drawing & music
# print("Два кружка", both_hobbies)
#
# drawing = drawing - both_hobbies
# print("Кружок рисования", drawing)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
#
# print(a >= b)


# Тип frozenset

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"Hello", "world"})
# print(a)


# a = [1, 2, 3, 4, 5, 67, 5, 3, 7, 4, 3, 21, 1, 5]
# print(a)
# b = set(a)
# print(b)
# a = list(b)
# print(a)

# Словарь

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: "four"}
# lst[0] = 10
# print(lst[0])
# d['one'] = 10
# print(d['one'])

# d = {'one': 1, 'two': 2, 'three': 3, 4: "four"}
# print(d)
# print(type(d))
#
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

d = {'one': 1, 'two': 2, 'three': 3, (1, 2, 3): "кортеж", True: [1, 2, 3, 4, 5]}
print(d)



# text = input("Введите строку: ")
#
# b = "уеыаоэяиюУЕЫАОЭЯИЮ"
#
# count = 0
# for char in text:
#     if char in b:
#         count += 1
#
# print("Количество гласных букв в строке:", count)


# _______________________________-

# dict_origin = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# dict_new = {'name': dict_origin['name'], 'salary': dict_origin['salary']}
# del dict_origin['name']
# del dict_origin['salary']
#
# print(dict_origin)
# print("Новый словарь:", dict_new)
