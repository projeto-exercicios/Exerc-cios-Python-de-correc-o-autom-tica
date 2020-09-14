from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1258847)

a = []

def random_string_generator():
    r = ""
    my_str = ""
    for e in range(1,3):
        my_str += choice(ascii_letters).lower()
    for o in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        r += choice(my_str)
    return r


for e in range(19075):
    v = random_string_generator()
    m = message_optimizer(v)
    a.append(m)
