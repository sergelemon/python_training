#10. Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные
#часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
#Учтите, что число n может быть больше, чем количество минут в сутках.

n = int(input("Введите число\n"))
n = n % 86400
hh = n // 60
mm = n - hh * 60
print(hh, ':', mm)