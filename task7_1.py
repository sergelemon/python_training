# 2. Даны два списка чисел. Показать,
#     - числа содержащиеся одновременно как в первом списке, так и во втором
#     - числа содержащиеся в первом, но отсутствуют во втором
#     - молько уникальный для первого и второго списков

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7, 8}

print('A =', A)
print('B =', B)
print('содержащиеся одновременно как в A, так и в B:', A & B)
print('содержащиеся в A, но отсутствуют в B:', A - B)
print('уникальныe для A и B:', A ^ B)