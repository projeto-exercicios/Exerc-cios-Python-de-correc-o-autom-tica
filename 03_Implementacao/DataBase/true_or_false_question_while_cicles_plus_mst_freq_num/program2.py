import random
from random import randint
from random import seed

seed(135)


a = []
for n in range(13):
    a.append(randint(3,33))

c = 0

def while_1():
    while c < 5:
        print(c + 1)

def while_2():
    while c < 5:
        if c == 4:
            c = 0
        print(c)
        c += 1

def while_3():
    global c
    while c < 5:
        print(c)
        c += 1


def most_frequent_num(nums, max_num):
