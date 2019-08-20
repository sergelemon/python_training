# 10.	Используя циклы и оператор IF написать функции для построения фигур изображённых на рисунке ниже. Функции принимают
# в качестве аргумента высоту фигуры в символах и на основании этого строят фигуры.

h = int(input('Введите высоту фигуры (нечетное число): '))
if h <= 0 or h % 2 == 0:
    print('Неверное значение высоты!')
    exit()

center = h//2
for y in range(h):
    y2 = h - y - 1
    s = ''
    for x in range(h):
        if (y <= center) * ((center - y) <= x <= (center + y)):
            s += '*'
        elif (y > center) * ((center - y2 == x) + (center + y2 == x)):
            s += '*'
        else:
            s += ' '
    print(s)

print('')

for y in range(h):
    y2 = h - y - 1
    s = ''
    for x in range(h):
        if (y <= center) * ((center - y) <= x <= (center + y)):
            s += '*'
        elif (y > center) * ((center - y2 == x) + (center + y2 == x) + (center == x)):
            s += '*'
        else:
            s += ' '
    print(s)