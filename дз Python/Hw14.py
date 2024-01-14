num_stud = int(input("Введите количество студентов: "))

names = []
scores = []

for _ in range(num_stud):
    name = input("Введите фамилию или имя студента: ")
    score = float(input("Введите балл студента: "))
    names.append(name)
    scores.append(score)

average_score = sum(scores) / len(scores)

print("Средний балл:", average_score)

print("Студенты с баллом выше среднего:")
for i in range(num_stud):
    if scores[i] > average_score:
        print(names[i])
