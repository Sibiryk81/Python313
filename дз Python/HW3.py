a = int(input("Введите кол-во символов: "))
s = input("Тип символа: ")
b = int(input("0 - горизонт\n1 - вертикаль\n ориентация линий: "))
i = 0
while i < a:
    if b == 0:
        print(s, end=" ")
    if b == 1:
        print(s)
    i += 1