# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите все,
# которые подходять по условию задачи.
# Задачу необходимо решить с использованием словаря.

s = ' антошка  антошка идем копать картошку \nантошка антошка идем копать картошку'
print(s, '\n')

words = {}
word = ''

for i in range(len(s)):
    if s[i] == ' ' or s[i] == '\n':
        if word != '':
            if not word in words:
                words[word] = 0
            words[word] += 1
            word = ''
    else:
        word += s[i]
if word != '':
    if not word in words:
        words[word] = 0
    words[word] += 1

m = max(list(words.values()))
for key, value in words.items():
    if value == m:
        print(key)
