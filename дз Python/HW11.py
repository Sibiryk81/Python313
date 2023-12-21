a = input("Введите строку: ")

b = "уеыаоэяиюУЕЫАОЭЯИЮ"

count = 0
for char in a:
    if char in b:
        count += 1

print("Количество гласных букв в строке:", count)