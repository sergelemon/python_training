'''По данному натуральному `n ≤ 9` выведите лесенку из `n` ступенек,
`i`-я ступенька состоит из чисел от 1 до `i` без пробелов.
    1
    12
    123
    1234
    12345'''

N = int(input("Введите число (1-9):"))
if not (1 <= N <= 9):
    print("Натуральное число N должно быть в диапазоне от 1 до 9")
    exit()

for line_number in range(1, N+1):
    line_text = ''
    for symbol_number in range(1, line_number+1):
        line_text += str(symbol_number)
    print(line_text)