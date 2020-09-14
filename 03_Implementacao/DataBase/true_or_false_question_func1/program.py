from random import randint
from random import seed
seed(135)
c = []
def func1():
    global c
    d = range(55);
    for o in d:
        c.append(randint(11,333))
        
func1()
