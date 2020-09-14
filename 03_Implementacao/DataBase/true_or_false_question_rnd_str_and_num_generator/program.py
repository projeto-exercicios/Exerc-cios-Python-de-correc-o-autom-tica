from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(135)

a = []

def random_string_generator():
    l = ""
    for k in range(randint(1,30)):
        l += choice(ascii_letters)
    return l

def random_number_generator():
    n = ""
    for c in range(randint(1,30)):
        n += str(randint(0,9))
    return n

for g in range(20):
    g1 = random_string_generator()
    if len(g1) < 15:
        g1 = random_number_generator()
    a.append(g1)
