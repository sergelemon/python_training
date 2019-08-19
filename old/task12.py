#12.Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере(пробелы важны!).
#Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного числа

n = int(input('Please enter an integer number:'))
print(f'The next number for the number {n} is {n+1}')
print(f'The previous number for the number {n} is {n-1}')

