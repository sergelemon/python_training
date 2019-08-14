# Линейный поиск

# # поиск первого вхождения
# from random import randint
#
# def line_search(collection, key):
#     for idx, value in enumerate(collection):
#         if key == value:
#             return idx
#     else: # если цикл завершился успешно
#         return -1
#
# lst = [randint(0,9) for _ in range(15)]
# print(lst)
#
# key = 6
# result = line_search(lst, key)
#
# print(result)

# # поиск мин и макс
# from random import randint
#
# def search_min_max(collection):
#     minimum = collection[0]
#     maximum = collection[0]
#     for value in collection:
#         if minimum > value:
#             minimum = value
#         elif maximum < value:
#             maximum = value
#     return minimum, maximum
#
# lst = [randint(0,9) for _ in range(10)]
# print(lst)
# print(search_min_max(lst))

# # Сортировка пузырьком
#
# from random import randint
# def bubble_sort(collection, dir = True)
#     count_of_iteration = 0 # добавлено для удобства отладки
#     for i in range(len(collection)-1):
#         for j in range(len(collection) - i -1):
#             if collection[j] > collection[j+1] if dir else collection[j] < collection[j+1]:
#                 collection[j], collection[j+1] = collection[j+1], collection[j]
#         count_of_iteration += 1
#     return count_of_iteration
#
# # можно оптимизировать этот код
#
# from random import randint
# def bubble_sort(collection, dir = True)
#     count_of_iteration = 0 # добавлено для удобства отладки
#     for i in range(len(collection)-1):
#         flag = True
#         for j in range(len(collection) - i -1):
#             if collection[j] > collection[j+1] if dir else collection[j] < collection[j+1]:
#                 collection[j], collection[j+1] = collection[j+1], collection[j]
#                 flag = False
#         if flag:
#             break
#         count_of_iteration += 1
#     return count_of_iteration

# сортировка выбором

# сортировка вставками
# попробовать написать устойчивый алгоритм сортировки