from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1142344)

t = []

def random_string_generator():
    w = ""
    my_str = ""
    for e in range(1,3):
        my_str += choice(ascii_letters).lower()
    for f in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        w += choice(my_str)
    return w


for e in range(19782):
    p = random_string_generator()
    m = message_optimizer(p)
    t.append(m)
