'''
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
одним ходом.
'''
msg = ('положение коня по горизонтали:', 'положение коня по вертикали:', 'номер клетки по горизонтали:', 'номер клетки по вертикали:')
KnightX, KnightY, X, Y = (int(input(msg[i])) for i in range(4))

deltaX = KnightX - X
deltaX = deltaX if deltaX > 0 else -deltaX

deltaY = KnightY - Y
deltaY = deltaY if deltaY > 0 else -deltaY

answer = 'YES' if deltaX == 1 and deltaY == 2 or deltaX == 2 and deltaY == 1 else 'NO'
print(answer)