# Найти наибольшую степень двойки, не превышающую введенное число

N = int(input("Введите целое число N:"))
i, tmp = 0, 1
while True:
    tmp *= 2
    if tmp > N:
        print("\nНаибольшая степень двойки, не превышающая N: ", int(tmp/2))
        print("Показатель степени: ", i)
        break
    i += 1

# Таблица умножения

print("\nТаблица умножения: \n")

for row in range(2):
    for n in range(2,10):
        s = ''
        for col in range(2 + 4*row, 6 + 4*row):
            s = s + str(col) + ' x ' + str(n) + ' = ' + str(col*n) + '\t\t'
        print(s)
    print('')