from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1120117)

o = []
l = []
def random_string_generator():
    v = ""
    for b in range(randint(1,15)):
        v += choice(ascii_letters)
    return v


for t in range(18354):
    o.append(randint(0, 104))
    l.append(random_string_generator())


k = o

for t in range(55062):
    o[t%len(o)] =  o[t%len(o)] * 3
