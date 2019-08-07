'''
# тема урока - множества и словари

# множество хранит данные в произвольном порядке
# одинаковые данные записываются в множество только единожды
# можно хранить только значения неизменяемых типов данных: числа, строки, кортежи
# множество имеет свой уникальный хеш, рассчитанный от содержимого

# создание множества на основании списка (с убиранием дублей), и обратное преобразование

lst = ['foo', 'bar', 'baz', 'foo', 'qux']
print(lst) # ['foo', 'bar', 'baz', 'foo', 'qux']

x = set(lst)
print(x) # {'baz', 'foo', 'qux', 'bar'}

lst = list(x)
print(lst) # ['foo', 'qux', 'baz', 'bar']

# другой способ создания множества - через фигурные скобки.
# нельзя использовать пустое содержимое, потому что будет создано не множество, а словарь
x = {1, 2, 3}

# эти множества будут равны
A = {1, 2, 3}
B = {3, 2, 3, 1}
print(A == B)

# можно использовать оператор in
# можно использовать циклы для перебора множества
# функции удаления discard() И remove(); отличие второго метода в том, что при отсутствии элемента будет вызвано исключение
# pop() возвращает значение и сразу же удаляет его из множества; если множество пустое, будет вызвано исключение


# операции над множествами

A = {'foo', 'bar', 'baz', 'foo', 'qux'}
B = {'foo', 'bar', 'baz', 'foo'}

print(A.isdisjoint(B)) # Имеются неодинаковые элементы?
A = A.difference(B) # Вычесть второе множество из первого
print(A.isdisjoint(B)) # Имеются неодинаковые элементы?

A | B объединение
A |= B добавить B в A
и много других операторов - ВСТАВИТЬ из учебных материалов


# frozenset - аналогично set, только неизменяемый

a = set('qwerty')
b = frozenset('qwerty')
print(a == b)
print(type(a - b)) # <class 'set'>
print(type(a | b)) # <class 'set'>
print(type(b - a)) # <class 'frozenset'>

print(hash(b))

# словари
# каждый ключ словаря должен быть неизменяемого типа - число, строка, кортеж

mlb_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins'
}

# Можно создать словарь на основании списка кортежей с помощью функции dict:
mlb_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins')
])

# другой способ
mlb_team = dict(
    Colorado = 'Rockies',
    Boston = 'Red Sox',
    Minnesota = 'Twins'
)

print(mlb_team)
print(mlb_team['Minnesota'])

# можно добавить новый ключ и добавить/переопределить значение
mlb_team['Seattle'] = 'Seahawks'
print(mlb_team)

# mlb_team[1] не будет искать по индексу :) оно просто будет искать ключ 1
# срезы не разрешены
# append тоже не разрешен

person = {}
person['fname'] = 'Joe'
person['age'] = 51
person['children'] = ['Ralph', 'Betty']
person['pets'] = {'dog': 'Fido', 'cat' : 'Sox'}
print(person)

# модуль для более "красивой" печати словаря
from pprint import pprint as p
p(person)

# обращение к элементам дочернего списка или словаря
print(person['children'][1])
print(person['pets']['cat'])

# длина словаря
p(len(person))

# очистка словаря
# person.clear()

# получение данных по ключу без исключения, если ключа не нашлось

answer = person.get('something')
print(answer) # None

answer = person.get('something', 'shit!')
print(answer) # shit!

# создание словаря из списка ключей
lst = ['a', 'b', 'c']
d = dict.fromkeys(lst)

# получение списка пар ключ-значение для перебора в цикле
# каждая пара является кортежем ключ/значение

for key, value in person.items():
    # здесь данные кортежа можно сразу же помещать в две переменные
    print(key, value)

print(person.keys())
print(person.values())

person.pop('pets') # берет значение и удаляет пару
p(person)

# обновляет словарь данными из другого словаря

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 200, 'b': 400}
print(d1)
d1.update(d2)
print(d1)

a = {'Hello':'Hi','Bye':'Goodbye','List':'Array','Goodbye':''}
for key, value in a.items():
    if value == '':
        print(key)
for key1, value1 in a.items():
    if value1 == key:
        print(key1)
        a[key] = key1
print(a)

'''

