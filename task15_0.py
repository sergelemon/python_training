# class Person:
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#
# print('__doc__: {}'.format(Person.__doc__))
# print('__name__: {}'.format(Person.__name__))
# print('__module__: {}'.format(Person.__module__))
# print('__bases__: {}'.format(Person.__bases__))
# print('__dict__:')
#
# for key, value in Person.__dict__.items():
#     print('\t', key, ':', value)

class Mine(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @x.deleter
    def x(self):
        self.__x = 0

    @y.deleter
    def y(self):
        self.__y = 0

mine = Mine(4, 8)
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
mine.x = 3
mine.y = 5
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
del mine.x
del mine.y
print('x =', mine.x)
print('y =', mine.y)
print('----------------')