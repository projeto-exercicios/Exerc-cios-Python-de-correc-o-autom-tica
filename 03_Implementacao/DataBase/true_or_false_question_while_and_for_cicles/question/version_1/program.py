from random import randint
from random import seed

seed(1916894)

n = 19553
y = []
def while_cicle(m):
    n = m
    while(True):
        if n == 0: break
        print("function: while_sicle")
        n -= 1




def for_cicle(b):
    decision1 = randint(0, round(b / 2))
    decision2 = decision1 + 2
    decision3 = randint(decision2, b)
    values = []
    for idx in range(b):
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

y = for_cicle(257)

