from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(135)

a = []

def random_string_generator():
    l = ""
    my_str = ""
    for i in range(0,3):
        my_str += choice(ascii_letters).lower()
    for k in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        l += choice(my_str)
    return l


for i in range(6):
    s = random_string_generator()
    m = message_optimizer(s)
    a.append(m)
