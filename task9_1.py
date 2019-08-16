# 1.	Написать следующие выражения:
#
# - (a + b * c)2
# - a - 4 * b / c
# - (a * b + 4) / (c - 1)

from random import randint

lst = [randint(1, 9) for _ in range(3)]
print('a, b, c =', lst)

funk1 = lambda a, b, c: (a + b * c) ** 2
funk2 = lambda a, b, c: a - 4 * b / c
funk3 = lambda a, b, c: (a * b + 4) / (c - 1)

try:
    print('(a + b * c) ** 2 =', funk1(*lst))
    print('a - 4 * b / c =', funk2(*lst))
    print('(a * b + 4) / (c - 1) =', funk3(*lst))
except:
    print('Деление на ноль')
