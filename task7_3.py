# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите все,
# которые подходять по условию задачи.
# Задачу необходимо решить с использованием словаря.

s = 'антошка  антошка идем копать картошку \nантошка антошка идем копать картошку'
print(s, '\n')
sp = s.split()

words = {}
word = ''

for word in sp:
    if not word in words:
        words[word] = 0
    words[word] += 1

m = max(list(words.values()))
for key, value in words.items():
    if value == m:
        print(key)
