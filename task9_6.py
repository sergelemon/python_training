# 6.	В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
# Новый список создавать нельзя!

from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)

x, y = lst.index(max(lst)), lst.index(min(lst))
lst[x], lst[y] = lst[y], lst[x]
print(lst)