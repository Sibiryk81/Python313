in_s = input("Введите по порядку, без пробелов, элементы кортежа: ")

t1 = []

for i in in_s:
    t1.append(i)

print(tuple(in_s))

s = {}

print("Статистика частотности символов: ")
for i in t1:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1

for i, j in s.items():
    print(f"Символ '{i}' встречается {j} раз")
