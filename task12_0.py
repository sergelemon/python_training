# raise = ВызватьИсключение
# assert - проверка на условие, если возвращает ложь, выводится исключение
# else: если исключение удалось избежать
# finally: обработчик финальных действий при любом раскладе

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except KeyboardInterrupt as ex: # проверка определенного исключения выполняется в первую очередь
#         print('bye-bye')
#         exit()
#     except ZeroDivisionError as ex:
#         print('Деление на 0')
#     except ValueError as ex:
#         print('Неверный тип значения')
#     except Exception as ex: # проверка базового исключения выполняется во вторую очередь
#         print('Не предусмотренное исключение', ex)
#     else: # если исключение удалось избежать
#         print('Ошибок не было')
#     finally: #выполняем в конце при любом раскладе
#         break

from random import randint
lst = [randint(1, 10) for _ in range(15)]
print(lst)

it = iter(lst)
try:
    while True:
        elem = next(it)
        print(elem)
except StopIteration as ex:
    print('Конец списка')
