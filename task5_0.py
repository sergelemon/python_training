# Строки

# s = input('Введите строку\n')
'''
s = 'Hello World!'
print("Your string is '{}'".format(s))

s *= 3 # строка будет клонирована втрое
print(s)

length = len(s) # длина строки
print(length)

# Индекс
print(s[0])
print(s[length-1])
print(s[-1])
print(s[-length])
# print(s[-50]) вернет ошибку
'''

# Срезы
'''
s = 'test string'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
'''

# find()
'''
s = 'Hello World!'
print("Your string is '{}'".format(s))

idx = s.find('a')
print("idx = '{}'".format(idx)) # вернет -1 если ничего не найдено

idx = s.find('l')
print("idx = '{}'".format(idx))

idx = s.find('l', idx+1) # ищем следующее вхождение буквы l
print("idx = '{}'".format(idx))
'''
# rfind аналогично но справа налево

# replace замена строик

'''
s1 = s.replace('W', 'w')
print(s1)

# count количество вхождений подстроки в строке

print('Abracadabra'.count('a'))
print(('a'*10).count('aa'))

s1 = s.capitalize()
print(s1)

txt = 'one two three four five six seven'
txt = txt.split()
print(txt)

txt = ','.join(txt)
print(txt)

txt1 = txt.upper()  # верхний регистр
print(txt1)

txt1 = txt.lower() # нижний регистр
print(txt1)

txt1 = txt.title() # слова начинаются с заглавных букв
print(txt1)

txt = '  56456   '
txt = txt.strip()
print(txt)

txt = '!!56456!!!'
txt = txt.strip('!')
print(txt)
'''

# Вложенная конструкция

'''
rows = 6
cols = 5

for i in range(rows):
    print(i, end='\t')
    for _ in range(cols):
        print('*', end='')
    print()
print()
'''

# Использование отладчика

# ГСЧ

import random
for _ in range(11):
    print(random.randint(1,100))