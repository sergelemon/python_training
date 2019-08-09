# Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов. Необходимо развеннуть
# словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве
# ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.
#     ```
#     apple - malum, pomum, popula
#     fruit - baca, bacca, popum
#     punishment - malum, multa

from pprint import pprint as p

d1 = {}
d1['apple'] = ['malum', 'pomum', 'popula']
d1['fruit'] = ['baca', 'bacca', 'popum']
d1['punishment'] = ['malum', 'multa']
p(d1)

print('')

d2 = {}
for key, item in d1.items():
    for item2 in item:
        d2[item2] = key
p(d2)
