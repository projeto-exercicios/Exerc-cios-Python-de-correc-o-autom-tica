from random import randint
from random import seed
seed(1623537)
a = []
def func1():
    global a
    x = range(19294);
    for j in x:
        a.append(randint(718,1552))
        
func1()
