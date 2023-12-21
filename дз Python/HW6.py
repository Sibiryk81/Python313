
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []
print(a)
for i in a:
    if a.count(i) == 1 and i not in b:
        b.append(i)
print(b)
