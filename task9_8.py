# 8.	Дан список. Необходимо его перевернуть. Использовать срезы, метод revers() и подобные встроенные механизмы, а так же
# оператор IF ЗАПРЕЩЕНО. Можно использовать только цикл и арифметические операторы!

from random import randint

count = int(input('Укажите длину списка: '))
if count <= 0:
    print('Неверное значение длины')
    exit()

lst = [randint(1, 100) for _ in range(count)]
print('Список: ', lst)

for i in range(len(lst) // 2):
    j = len(lst) - i - 1
    lst[i], lst[j] = lst[j], lst[i]

print('Перевернутый список: ', lst)