month = int(input("Введите месяц цифрой: "))
if 1 <= month <= 12:
    if 3 <= month <= 5:
        print("Весна")
    if 6 <= month <= 8:
        print("Лето")
    if 9 <= month <= 11:
        print("Осень")
    if 1 <= month <= 2 or month == 12:
        print("Зима")
else:
    print("Некорректные данные")
