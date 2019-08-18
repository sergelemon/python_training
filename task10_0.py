# Двоичный поиск элемента

# Рекурсия

# # Описать возведение в степень как рекурсивное умножение основания степени в течение n раз
# def pow(num, exp):
#     return num * pow(num, exp - 1) if exp > 0 else 1
#
# print(pow(2, 10))

# # Факториал
# def fuct(num):
#     return num * fuct(num - 1) if num > 1 else 1
#
# print(fuct(5))

# # рекурсивные структуры данных
# def attach2head(new_element, lst):
#     return [new_element] + lst
#
# lst = []
# print(lst)
# lst = attach2head('hello', lst)
# print(lst)
# lst = attach2head(-31, lst)
# print(lst)
# lst = attach2head(46, lst)
# print(lst)
#
# lst = []
# lst = attach2head(46, attach2head(-31, attach2head('hello', lst)))
# print(lst)
#
# def recursive_list_sum(lst):
#     if not lst:
#         return 0
#     return lst[0] + recursive_list_sum(lst[1:])

# # Наивная рекурсия
# # осторожно - этот код неэффективен на больших числах!
# def fibo(n):
#     return n if n < 2 else fibo(n-1) + fibo(n-2)
#
# for i in range(1, 10):
#     print(i, fibo(i))

# разобрать пример использования рекурсии для иерархической печати файлов и директорий
# изучить мануал

# быстрая сортировка Хоара
# изучить мануал
# переделать представленный алгоритм для обратной сортировки

# Функции sorted() и sort()
# изучить мануал
