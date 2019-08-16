# Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
# # Небольшая подсказка. В этой задаче вам понадобится, список, метод revers() (или срез [::-1]), чтоб развернуть список,
# # метод join() и строка ascii_uppercase из модуля string (её можно получить если сделать импорт from string import ascii_uppercase),
# # она содержит все буквы латинского алфавита.

from string import  ascii_uppercase

def numeral(decimal_number, base_number):

    if base_number > 36 or base_number < 2:
        return 'Неверное основание!'
    elif decimal_number = 0:
        return '0'

    dec, l = decimal_number, []

    while dec > 0:
        rest = dec % base_number
        l.append(str(rest) if rest < 10 else ascii_uppercase[rest - 10])
        dec = int((dec - rest) / base_number)
    l.reverse()

    return ''.join(l)

decimal_number = int(input('Введите десятичное число: '))
base_number    = int(input('Введите новое основание числа (2 - 36): '))

print(numeral(decimal_number, base_number))


