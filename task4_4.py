'''Даны два целых числа `A` и `В`, `A > B`. Выведите все нечётные числа от `A` до `B` включительно, в порядке убывания.
В этой задаче можно обойтись без инструкции **if**.'''

A = int(input('A:'))
B = int(input('B:'))
delta = (A-B)+1

for i in range(delta):
    n = A-i
    if n%2 != 0:
        print(n)