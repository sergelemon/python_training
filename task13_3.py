# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов

file = open('grade.txt', encoding='utf-8')
lst = file.readlines()
print("Количество строк:", len(lst))

count = 0
for s in lst:
    count += 1
    slova = s.split()
    print('Строка', count, ': количество слов =', len(slova), ', количество символов =', len(s))