# ООП

# class Human:
#     type = 'mammal'
#
# class Odessit(Human):
#     adress = 'Odessa'
#
# p = Odessit()
# print(p.type)
# print(p.adress)
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def print_point(self):
#         print(self.x, self.y)
#
# pt = Point(3, 4)
# print(pt.x)
# print(pt.y)
#

# print(p.__class__.__dict__)
# print(p.__class__.__bases__)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_biggest_number(*args):
    if len(args) == 0:
        return ''
    name = args[0].name
    age = args[0].age
    for h in args:
        if h.age > age:
            age = h.age
            name = h.name
    return name

humans = [Human('Sergey', 43), Human('Olga', 25), Human('Ivan', 50)]
print(get_biggest_number(*humans))

class SomeClass:
    @classmethod
    def hello(cls):
        print('Привет из класса: {}'.format(cls.__name__))
    @staticmethod
    def is_adult(age):
        return age > 18

SomeClass.hello()
print(SomeClass.is_adult(20))