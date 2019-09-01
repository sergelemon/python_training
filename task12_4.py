# 4. Дана база данных о продажах некоторого интернет-магазина.
#
# Каждая строка входных данных представляет собой запись вида Покупатель Товар Количество,
# где Покупатель — имя покупателя (строка без пробелов),
# Товар — название товара (строка без пробелов),
# Количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
#
# Например:
#
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5
#
#
# Ivanov:
# 	envelope 5
# 	marker 3
# 	paper 17
# Petrov:
# 	envelope 20
# 	pens 5

from pprint import pprint as pp

d = {}
l = ['Ivanov paper 10',
      'Petrov pens 5',
      'Ivanov marker 3',
      'Ivanov paper 7',
      'Petrov envelope 20',
      'Ivanov envelope 5']

pp(l)
print()

for s in l:

    r = s.split()
    family = r[0]
    sku = r[1]
    count = r[2]

    d2 = d.get(family)
    d2 = {} if d2 == None else d2

    n = d2.get(sku)
    n = 0 if n == None else n
    n += int(count)

    d2[sku] = n
    d[family] = d2

pp(d, None, 1, 30)
# последний параметр позволяет сузить область вывода текста
# и получить требуемое форматирование
