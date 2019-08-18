# 2.	Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего параметра функции.
# Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй параметр задаёт количество разрядов для
#  сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт направление сдвига (по умолчанию влево (False)).

def sdvig(number, step = 1, direction = False):
    s = step if direction else len(str(number)) - step
    return int(str(number % (10 ** s)) + str(number // (10 ** s)))

print(sdvig(123456789))           # 234567891
print(sdvig(123456789, 2))        # 345678912
print(sdvig(123456789, 2, True))  # 891234567