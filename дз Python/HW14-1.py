# def average_score(scores):
#     return sum(scores) / len(scores)
#
#
# num_students = int(input("Введите количество студентов: "))
#
# last_names = []
# first_names = []
# scores = []
#
# for _ in range(num_students):
#     last_name = input("Введите фамилию студента: ")
#     first_name = input("Введите имя студента: ")
#     score = float(input("Введите балл студента: "))
#     last_names.append(last_name)
#     first_names.append(first_name)
#     scores.append(score)
#
# avg_score = average_score(scores)
#
# print("Средний балл:", avg_score)
#
# print("Студенты с баллом выше среднего:")
# for i in range(num_students):
#     if scores[i] > avg_score:
#         print(last_names[i], first_names[i])