# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в
# строку и выведите получившуюся строку.
# При решении этой задачи посторайтесь не пользоваться циклами и инструкцией `if`.

s1 = input('Введите строку:\n')
s2 = s1.split()
s3 = s2[1] + ' ' + s2[0]
print(s3)