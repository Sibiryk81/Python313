a = [int(input('-> ')) for _ in range(int(input('Введите количество знаков:  ')))]
s = k = 0
for i in a:
    if i != 0:
        s += i
        k += 1
        if k > 0:
            a = s / k
print("Среднее арифметическое ненулевых элементов: ", a)
