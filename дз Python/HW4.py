num = 57
a = 0
b = None
while b != num and b != 0:
    b = int(input("Введите целое число от 1 до 100: "))
    if b == 0:
        break
    elif b < num:
        print("Загаданное число больше")
    elif b > num:
        print("Загаданное число меньше")
    a += 1
if b == num:
    print("Угадали за:", a, "попыток")