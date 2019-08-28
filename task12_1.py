# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(y):
    return (y != 0) and (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))

y = int(input('Введите год: '))
print('is_year_leap =', is_year_leap(y))