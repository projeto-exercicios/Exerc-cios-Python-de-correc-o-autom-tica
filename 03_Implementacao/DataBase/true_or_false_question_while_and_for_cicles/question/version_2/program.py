from random import randint
from random import seed

seed(1292246)

r = 19092
p = []
def while_cicle(i):
    r = i
    while(True):
        if r == 0: break
        print("function: while_sicle")
        r -= 1




def for_cicle(l):
    decision1 = randint(0, round(l / 2))
    decision2 = decision1 + 2
    decision3 = randint(decision2, l)
    values = []
    for idx in range(l):
        if idx < decision1:
            continue
        if idx == decision2:
            pass
        if idx >= decision3:
            break
        values.append(idx)
    return values


def print_indexes(num):
    for idx in range(num):
        print(idx)

p = for_cicle(261)

