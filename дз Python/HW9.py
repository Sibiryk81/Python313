import random


def all_tuples(a):
    tup_one = tuple(random.randint(0, 5) for i in range(a))
    tup_two = tuple(random.randint(-5, 0) for i in range(a))
    return tup_one, tup_two


tup_one, tup_two = all_tuples(10)
print(tup_one)
print(tup_two)
c = tup_one + tup_two
print(c)
print("Кол-во 0 -> ", c.count(0))
