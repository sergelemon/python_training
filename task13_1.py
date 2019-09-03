# 1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
#
#     Андрей Говорухи               6  6  1  4  9  9  10 4  8  2  3  8
#     Василий Петров                2  9  4  7  6  6  3  6  5  5  2  4
#     Гавриил Варфаломеев           10 10 4  10 7  9  4  6  8  1  1  1
#     Игнат Тюльпанов               8  1  4  1  1  5  2  5  2  2  10 8
#     Илья Муромцев                 1  6  4  7  10 9  5  3  7  4  7  2
#     Кощей Бессмертный             3  10 1  4  1  8  10 6  2  10 7  4
#     Максим Мухин                  10 8  9  9  5  8  6  5  7  2  4  10
#     Маргарита Мартынова           9  1  5  1  10 10 2  4  4  9  8  10
#     Петр Николаев                 2  9  5  9  1  2  8  7  8  1  9  1
#     Полина Гусева                 9  2  8  7  3  9  9  5  1  9  2  6
#     Спиридов Тереньтьев           4  7  7  3  10 9  7  2  10 9  8  1
#     Станислав Трердолобов         8  1  6  1  4  1  10 8  8  1  8  8
#
#     Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
#     записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":
#
#     Говорухи А.         5.83
#     Петров В.           4.92
#     Варфаломеев Г.      5.92
#     Тюльпанов И.        4.08
#     Муромцев И.         5.42
#     Бессмертный К.      5.5
#     Мухин М.            6.92
#     Мартынова М.        6.08
#     Николаев П.         5.17
#     Гусева Г.           5.83
#     Тереньтьев С.       6.42
#     Трердолобов С.      5.33
#
#     Выравнивание колонок - желательно!

import string

students = {}
file = open('grade.txt', encoding='utf-8')
lst = file.readlines()

for s in lst:
    student_data = s.split()
    family, name = '', ''
    sum, amount = 0, 0
    for idx, ch in enumerate(student_data):
        if idx == 0:
            name = ch
        elif idx == 1:
            family = ch
        else:
            sum += int(ch)
            amount += 1
    short_name = family + ' ' + name[0] + '.'
    students[short_name] = sum / amount

sum, amount = 0, 0
print('Средний балл ниже 5:')
for key, value in students.items():
    sum += value
    amount += 1
    if value < 5:
        print(key, round(value, 2))

print('Средний балл по классу:', round(sum / amount, 2))

file = open('result.txt', 'w', encoding='utf-8')
for key, value in students.items():
    file.write(key.ljust(18) + str(round(value, 2)))
    file.write('\n')
file.close()






