# Написать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов типа
# класса `Student` также реализуется с помощью соответствующего класса.
# В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
# `grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def properties(self):
        print('Студент ', self.name, ', ', self.age, ' лет', ', ', self.grade, ' курс')

class Group():
    def __init__(self, *args):
        self.list = []
        for _ in args:
            self.list.append(_)
    def properties(self):
        for student in self.list:
            student.properties()

a = Student('Сережа', 43, 5)
b = Student('Маша', 19, 1)

c = Group(a, b)
c.properties()

