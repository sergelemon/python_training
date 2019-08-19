# 7.	Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу
# от -1 до 1, причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например,
# последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]

from random import randint

lst = [randint(-100, 100) for _ in range(10)]
print('Список: ', lst)

maximum, minimum = max(lst), min(lst)
norma = maximum if maximum ** 2 > minimum ** 2 else minimum
if norma < 0:
    norma *= -1
print('Норма: ', norma)

lst = list(map(lambda x: round(x/norma, 3), lst))
print('Нормированный список: ', lst)
