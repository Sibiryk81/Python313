import random

num = []
while len(num) < 10:
    i = random.randint(0, 9)
    if i not in num:
        num.append(i)
print(num)
