# Написать функцию `is_date`, принимающую 3 аргумента — день, месяц и год. Вернуть `True`, если дата корректная (надо
# учитывать число месяца. Например 30.02 - дата не корректная, так же 31.06 или 32.07 и т.д.), и `False` иначе.

def is_date(dd, mm, yy):
    if (yy == 0) or not (0 < mm < 13) or not (0 < dd < 32):
        # заведомо неправильное число дня, месяца, года
        return False
    elif (dd == 31) and (mm in [2, 4, 6, 9, 11]):
        # в месяце не допускается более 30 дней
        return False
    elif (dd > 29) and (mm == 2):
        # в феврале не допускается более 29 дней
        return False
    elif (dd == 29) and (mm == 2) and (yy % 4 > 0):
        # в феврале не допускается более 28 дней, если год не високосный по юлианскому и григорианскому календарю
        return False
    elif (dd == 29) and (mm == 2) and (yy % 400 > 0) and (yy % 100 == 0):
        # в феврале не допускается более 28 дней, если год не високосный по григорианскому календарю
        return False
    else:
        return True

dd = int(input('Введите день: '))
mm = int(input('Введите месяц: '))
yy = int(input('Введите год: '))
print('is_date: ', is_date(dd, mm, yy))