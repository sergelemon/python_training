# Найдите произведение самого большого и самого маленького элементов списка. Так же, отобразате найденые элементы.

from random import randint
lst = [randint(1, 100) for _ in range(10)]
print(lst)
a, b = max(lst), min(lst)
c = a*b
print('Наименьшее: ', a)
print('Наибольшее: ', b)
print('Произведение: ', c)