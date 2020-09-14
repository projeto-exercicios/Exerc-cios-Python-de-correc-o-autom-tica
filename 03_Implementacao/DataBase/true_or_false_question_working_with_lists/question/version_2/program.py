from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1121105)

w = []
l = []
def random_string_generator():
    s = ""
    for u in range(randint(1,15)):
        s += choice(ascii_letters)
    return s


for v in range(18241):
    w.append(randint(0, 83))
    l.append(random_string_generator())


t = w

for v in range(36482):
    w[v%len(w)] =  w[v%len(w)] * 3
