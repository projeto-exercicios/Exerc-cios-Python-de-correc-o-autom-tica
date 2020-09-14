from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1367269)

r = []

def random_string_generator():
    s = ""
    for i in range(randint(1,30)):
        s += choice(ascii_letters)
    return s

def random_number_generator():
    g = ""
    for o in range(randint(1,30)):
        g += str(randint(0,9))
    return g

for l in range(18856):
    k = random_string_generator()
    if len(k) < 15:
        k = random_number_generator()
    r.append(k)
