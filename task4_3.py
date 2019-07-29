'''Даны два целых числа `A` и `В`. Выведите все числа от `A` до `B` включительно, в порядке возрастания, если `A < B`,
или в порядке убывания в противном случае.'''

A = int(input('A:'))
B = int(input('B:'))

delta = (A-B) if A>B else (B-A)
delta += 1

for i in range(delta):
    n = (A-i) if A>B else (A+i)
    print(n)
