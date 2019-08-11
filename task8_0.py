# Функции

# 1. Именованные

# def function_name(<list of parameters>):
#     body

# def print_some_text():
#     print('Hello World')
#     return 4
#
# # функция с пустым телом
# def empty_function():
#     pass
#
# print_some_text()
# print(print_some_text())

# def draw_rect(x, y=5):
#     for _ in range(y):
#         for _ in range(x):
#             print('*', end='')
#         print()
#
# # draw_rect(10, 4)
# draw_rect(10)

# параметры по умолчанию надо ставить в конец списка аргументов!

# x = 10
# print(x)
#
# def func():
#     global x
#     x = 3
#     print('local ', x)
#
# func()
# print('global ', x)

# Вложение функций
# для использования глобальной переменной используем слово global
# для переменной из верхнего уровня используем слово nonlocal

# def func_outer():
#     x = 2
#     print(x)
#
#     def func_inner():
#         nonlocal x
#         x = 5
#
#     func_inner()
#     print(x)
#
# func_outer()

# Функция с переменным числом аргументов
# здесь из *args формируется кортеж

# def multi_var(r, *args):
#     print(r, args)
#     for value in args:
#         print(value, end='')
#     print()
#
# multi_var(1, 2, 3, 'ads')

# из **args формируется словарь

# def multi_kw(**kwargs):
#     print(kwargs)
#
# multi_kw(name = 'Ivan', job = 'Worker', salary = 500)

# Можно использовать ссылку на функцию

# def comare(a, b)
#     ...
#
# x = comare
# x(a, b)

# Возврат значения из функции
# def my_pow(a, b):
#     return a ** b
#
# a, b = 10, 5
# x = my_pow(a, b)
# print(x)

# Для возврата нескольких значений рекомендуется использовать ИМЕНОВАННЫЕ КОРТЕЖИ (см. примеры из мануала)

# анонимные функции (lambda)

# lambda [arg1 [, arg2...]]:expression
#
# func = lambda x, y: x + y
# func(4, 5) # 9
# func('x', 'y') # 'xy'

# map

# def fahrenheit(T):
#     return round((float(9)/5)*(T+32), 2)
#
# temperatures = (36.5, 37, 38)
# F = list(map(fahrenheit, temperatures))
# print(F)
#
# # или проще, через лямбду
# C = (36.5, 37, 38)
# F = list(map(lambda x: round((float(9)/5)*(x+32), 2), C))
# print(F)

# можно применять map к нескольким спискам, см примеры в мануале. также есть ВИДЕО.

# filter отбирает элементы списка по критерию соответствия элемента лямбда-функции, которая должна возвращать результат, который можно конвертировать в булево

from random import randint
lst = [randint(0, 100) for _ in range(20)]
print(lst)

odd_numbers = list(filter(lambda x: x % 2, lst))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)