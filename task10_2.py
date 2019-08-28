# Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество

from random import randint
lst = [randint(1, 100) for _ in range(10)]
print(lst)
k = 0
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        lst[i] = 0
        k += 1
print(lst)
print(k)