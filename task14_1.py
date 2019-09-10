# Реализовать класс цифрового счетчика. Обеспечьте возможность установления максимального и минимального значений,
# увеличения счетчика на 1, возвращения текущего значения.

class Counter():

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.num = minimum

    @property
    def number(self):
        return self.num

    @number.setter
    def number(self, value):
        if value > self.maximum:
            self.num = self.maximum
        elif value < self.minimum:
            self.num = self.minimum
        else:
            self.num = value

    def bigger(self):
        if self.num != self.maximum:
            self.num += 1

a = Counter(1, 100)
print(a.number) #1

a.number = 50
print(a.number)  # 50

a.bigger()
print(a.number) #51

a.number = 100
print(a.number) #100

a.bigger()
print(a.number) #100 - не выше максимума

a.number = 1000
print(a.number) #100 - не выше максимума

a.number = 0
print(a.number) #1 - не ниже минимума

