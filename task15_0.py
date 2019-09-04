class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

print('__doc__: {}'.format(Person.__doc__))
print('__name__: {}'.format(Person.__name__))
print('__module__: {}'.format(Person.__module__))
print('__bases__: {}'.format(Person.__bases__))
print('__dict__:')

for key, value in Person.__dict__.items():
    print('\t', key, ':', value)