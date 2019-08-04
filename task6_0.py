# # встроенные коллекции - списки и кортежи
#
# # список может хранить объекты разных типов
#
# # Создание списка
# a = []
# print(a)
# a = list()
# print(a)
# a = list('Hello World!')
# print(a)
# a = [1, 2, 3, 4, 5]
# print(a)
# a = ['a', 'b', 'c', 'd', 'e']
# print(a)

# # можно в элемент списка помещать функцию и использовать ее в дальнейшем
#
# a = ['a', 1.45, 'Hello World', True, sum]
# b = [1, 2, 3, 4, 5]
#
# print(a)
# list_len = len(a)
# idx = list_len - 1
# func = a[idx]
# result = func(b)
# print(result)
# '''
#
# # добавление в список
#
# '''
# b = []
# print('b = ', b)
# b.append(45)
# print('b = ', b)
# b.append('New string')
# print('b = ', b)
# b.append(sum)
# print('b = ', b)
#
# a = []
# for i in range(10):
#     a.append(i)
# print(a)
#
# # списки можно складывать
# a = [1,2,3,4]
# b = [5,6,7]
# c = a + b
# print(c)
#
# # списки можно умножать
# a = [1,2,3,4]
# print(a * 3)
#
# a = [0]
# a *= 10
# print(a)
#
# # len() возвращает кво элементов списка
#
# # использование for
#
# a = ['a', 'b', 'c', 'd']
# # for element in a:
# #     print(element, end=', ')
#
# for idx, element in enumerate(a):
#     print(idx, element)


# можно использовать срезы
#
# a = list('Hello World')
# print(a)
# print(a[2])
# print(a[2:])
# print(a[2:8])
# print(a[::2])
# print(a[::-1])

# # Удаление элемента по индексу
# a = list('Hello World')
# del a[5]
# print(a)
#
# # Другой вариант удаления - по значению
# a.remove('H')
# print(a)
# a.remove('l') # Удалит только первый встреченный
# print(a)
#
# # Теперь можем например склеить данные списка обратно в строку
# print(''.join(a))
#
# # Можно легко искать вхождение значения в список, получая булев ответ
# print('t' in a)
# print('l' in a)

# # Получение минимума, максимума, суммы
# a = [1,20,35,44,5]
# print(min(a))
# print(max(a))
# print(sum(a))
#
# # Получение индекса элемента по значению элемента
# print(a.index(35))
# print(a.index(34)) # вернет исключение

# Подсчет числа вхождений
# a = list('Hello World')
# print(a.count('l'))

# Получаем значение последнего элемента и одновременно удаляем его из списка
# a = list('Hello World')
# print(a)
# print(a.pop())
# print(a)
# print(a.pop(6))
# print(a)

# # Вставка элемента в список по индексу
# a = [1,20,35,44,5]
# a.insert(2, 54)
# print(a)

# # Очистка
# a = [1,2,3]
# a.clear()
# print(a)

# Копирование
# # некорректный вариант - создает две ссылки на один и тот же список
# a = list('Hello World')
# b = a
# print(a)
# print(b)
# a.pop()
# print(a)
# print(b)

# # корректный вариант - создается два полностью независимых списка
# a = list('Hello World')
# b = a.copy()
# print(a)
# print(b)
# a.pop()
# print(a)
# print(b)

# extend работает как суммирование
# revers переворачивает список наоборот
# sort сортирует список (рассмотрим позже)


# List Comprehension - генератор списка

# from random import randint
#
# lst1 = []
# for _ in range(15):
#     lst1.append(randint(1, 10))
# print(lst1)
#
# # или, более кратко теперь:
# lst2 = [randint(1, 10) for _ in range(15)]
# print(lst2)
#
# # получение только четных значений из списка
#
# lst3 = [x for x in lst2 if x % 2 == 0]
# print(lst3)
#
# # то же, но полученные данные еще и возводим в квадрат
#
# lst3 = [x ** 2 for x in lst2 if x % 2 == 0]
# print(lst3)
#
# # способ перевода символов строки в верхний регистр
# s = 'lower case string'
# s = ''.join(ch.upper() for ch in s)
# print(s)

# # более сложный алгоритм, изменение только четных символов в строке в верхний регистр
# s = 'lower case string'
# s = ''.join([ch.upper() if idx % 2 == 0 else ch for idx, ch in enumerate(s)])
# print(s)

# Кортежи
# Отличается от списка тем, что не подлежит изменению

# tup1 = ('physics', 'chemistry')
# tup2 = () # пустой кортеж
# tup3 = tuple() # пустой кортеж
# tup4 = 'a', 'b', 'c'
# print(tup1, tup2, tup3, tup4)
#
# # но если будет так:
# tup6 = (100) # будет создан не кортеж, а просто переменная
# tup6 = (100,) # таки будет создан кортеж

# можно делать срезы и получать элементы по индексу
# можно создавать новый кортеж, как сумму двух других кортежей
# a = ()
# b = (1, 2)
# c = a + b
# print(c)

# Можно использовать поиск вхождения через in
# Можно перебирать элементы циклом

# Методы работы с кортежами:

# index
# count
# max()
# min()
# sum()
# len()