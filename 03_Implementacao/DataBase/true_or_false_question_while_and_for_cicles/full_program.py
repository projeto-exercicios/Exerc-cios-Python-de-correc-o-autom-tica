from random import randint
from random import seed

seed(135)

counter = 7
d = []
def while_cicle(a):
    counter = a
    while(True):
        if counter == 0: break
        print("function: while_sicle")
        counter -= 1




def for_cicle(c):
    decision1 = randint(0, round(c / 2))
    decision2 = decision1 + 2
    decision3 = randint(decision2, c)
    values = []
    for idx in range(c):
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

d = for_cicle(15)

answer_1_true = while_cicle(3)
answer_2_true = d
answer_3_true = print_indexes(5)



print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
