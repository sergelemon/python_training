# # 2.	Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

n = int(input('Введите пятизначное число:'))
lst = list(str(n))

even_numbers = list(filter(lambda x: int(x) % 2 != 0, lst))

m = 0
if len(even_numbers) > 0:
    m = 1
    for x in even_numbers:
        m *= int(x)

print('Произведение нечетных цифр:', m)