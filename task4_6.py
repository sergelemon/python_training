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
