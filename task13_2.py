# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
# пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.

file = open('result2.txt', 'w', encoding='utf-8')
print('Вводите текст построчно. После ввода пустой строки будет сформирован файл с введенным текстом:')
while True:
    s = input()
    if s == '':
        break
    file.write(s)
    file.write('\n')
file.close()
