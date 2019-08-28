# Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`, если оно простое, и
# `False` - иначе.

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

x = int(input('Введите число (2-1000): '))
print('is_prime: ', is_prime(x))