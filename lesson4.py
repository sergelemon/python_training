#циклы

#квадраты натуральных чисел от 1 до 10

'''
i = 1
while i < 11:
    print(i ** 2)
    i += 1
'''

#определение количества цифр натурального числа n
'''
n = int(input('Введите N:'))
length = 0
while n > 0:
    n //= 10
    length += 1
print(length)
'''

# стандарты использования имен переменных и классов:
# рекомендуемое для переменных - snake-case: this_info_1
# рекомендуемое для классов - camel-case: ThisInfo1

#оператор break
'''
a = b = 1
while a != 0 and b != 0:
    a = int(input('Введите делимое:'))
    b = int(input('Введите делитель:'))
    if b == 0:
        print('Делить на 0 нельзя:', a)
        break
    print(a / b)
'''

# оператор continue, в отличие от break, не прерывает цикл, а только прерывает итерацию
'''
while True:
    a = int(input('Введите делимое:'))
    b = int(input('Введите делитель:'))
    if a == 0:
        break
    elif b == 0:
        print('Делить на 0 нельзя:', a)
        continue
    print(a / b)
'''

# оператор else
'''
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('цикл окончен, i = ', i)
'''
'''
a = int(input('Введите целое число:'))
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число:')
        break
    a = int(input('Введите целое число:'))
else:
    print('Ни одного отрицательного числа не встретилось')
'''

# оператор for

# последовательный вывод цветов радуги

'''
i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='', end=';\n')
    i += 1
'''
# range()

# range(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 10, 2) #1, 3, 5, 7, 9

# сумма чисел от 1 до 5
'''
sum = 0
n = 5
for i in range(1, n+1):
    sum += i
print(sum)
'''

# Найти наибольшую степень двойки, меньшее введенного числа
'''
N = int(input('Введите целое число N:'))
i, tmp = 0, 1
while True:
    tmp *= 2
    if tmp > N:
        print(int(tmp/2), i)
        break
    i += 1
'''

# таблица умножения
'''
N = int(input('Введите число (1-9):'))
for i in range(2,10):
    print(N, ' x ', i, ' = ', N*i)
'''
for n in range(2,10):
    s = ''
    for m in range(2, 6):
        s = s + str(m) + ' x ' + str(n) + ' = ' + str(n*m) + '\t\t'
    print(s)
print('')
for n in range(2,10):
    s = ''
    for m in range(6, 10):
        s = s + str(m) + ' x ' + str(n) + ' = ' + str(n*m) + '\t\t'
    print(s)
