# Заполните список случайными числами и выполните реверс для части списка между элементами с индексами `a` и `b` (включая эти элементы)

from random import randint

a = int(input('Введите первый индекс (0-14): '))
b = int(input('Введите второй индекс ({}-14): '.format(a)))

lst = [randint(1, 100) for _ in range(15)]
print(lst)

while a < b:
    lst[a], lst[b] = lst[b], lst[a]
    a += 1
    b -= 1
print(lst)