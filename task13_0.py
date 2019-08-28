# Файлы

# import os
# print(os.sep) # \ то есть корень

# file = open('C:/Users/Сlass9-PC10/Documents/GitHub/python_training/lesson_12.txt')
# file.close()

# file = ''
# try:
#     file = open('C:/Users/Сlass9-PC10/Documents/GitHub/python_training/lesson_12.txt')
# except FileNotFoundError as ex:
#     print('Файл не найден!', ex)
# finally:
#     if not file.closed:
#         file.close()


# Запись файла

from pprint import pprint as pp
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pp(lst)

file = open('example_file.txt', 'w')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()

# Чтение файла целиком

print()
lst = []
file = open('example_file.txt')
lst = file.read()
file.close()
pp(lst)
print()

# Чтение файла как списка с обработкой результата

print()
lst = []
file = open('example_file.txt')
lst = file.readlines()
file.close()
pp(list(map(lambda x: x.strip('\n'), lst)))
print()

# Чтение и запись байтовой информации

size_buff = 20
src = open('dog1.jpg', 'rb')
dst = open('dog2.jpg', 'wb')
while True:
    data = src.read(size_buff)
    if data:
        dst.write(data)
    else:
        break
src.close()
dst.close()

# Красивее так:

size_buff = 20
with open('dog1.jpg', 'rb') as src, open('dog2.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break