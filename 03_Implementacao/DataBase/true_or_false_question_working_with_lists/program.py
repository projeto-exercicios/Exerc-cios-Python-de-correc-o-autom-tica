from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(135)

a = []
b = []
def random_string_generator():
    l = ""
    for k in range(randint(1,15)):
        l += choice(ascii_letters)
    return l


for i in range(10):
    a.append(randint(0, 50))
    b.append(random_string_generator())


d = a

for i in range(20):
    a[i%len(a)] =  a[i%len(a)] * 3
