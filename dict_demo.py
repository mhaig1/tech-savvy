import random

def histogram(s):
    """
    returns a dictionary of the number of each character in given string

    s: a string
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


word = 'bookkeeper'
h = histogram(word)
# print(h)




roster ='''Melissa
Mezue
Matthew
Ran
Andrea
Jinyi
Ivory
Smit
Adrianna
Mingqi
Meixi
Nicholas
Frantzia
Yu
Shiyu
Yiwen
Junxi
'''

roster = roster.split()
# print(roster)



grades = {}

random.seed(42)

for name in roster:
    grades[name] = random.randint(50, 100)


import pprint


# pprint.pprint(grades)

for name, score in grades.items():
    if score>80:
        print(name, score)


for name in grades.keys():
    if name.startswith('M'):
        print(name)


for score in grades.values():
    if score <60:
        print(score)



called = dict()

for name in roster:
    called[name] = 0

pprint.pprint(called)

random_name = random.choice(roster)


