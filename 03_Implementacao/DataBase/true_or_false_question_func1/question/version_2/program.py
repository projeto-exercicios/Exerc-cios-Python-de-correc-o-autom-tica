from random import randint
from random import seed
seed(1464336)
w = []
def func1():
    global w
    i = range(19954);
    for t in i:
        w.append(randint(538,3923))
        
func1()
