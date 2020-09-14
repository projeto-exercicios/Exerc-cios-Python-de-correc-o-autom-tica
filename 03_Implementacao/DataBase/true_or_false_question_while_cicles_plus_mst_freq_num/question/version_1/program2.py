import random
from random import randint
from random import seed

seed(1918616)


o = []
for e in range(19824):
    o.append(randint(0,357))

g = 0

def while_1():
    while g < 5:
        print(g + 1)

def while_2():
    while g < 5:
        if g == 4:
            g = 0
        print(g)
        g += 1

def while_3():
    global g
    while g < 5:
        print(g)
        g += 1


def most_frequent_num(nums, max_num):
