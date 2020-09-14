import random
from random import randint
from random import seed

seed(1941706)


i = []
for s in range(19601):
    i.append(randint(1,35))

x = 0

def while_1():
    while x < 5:
        print(x + 1)

def while_2():
    while x < 5:
        if x == 4:
            x = 0
        print(x)
        x += 1

def while_3():
    global x
    while x < 5:
        print(x)
        x += 1


def most_frequent_num(nums, max_num):
