a = [int(input('-> ')) for _ in range(int(input('Введите количество чисел:  ')))]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])
