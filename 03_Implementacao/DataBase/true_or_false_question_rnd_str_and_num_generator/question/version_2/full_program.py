from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1437282)

v = []

def random_string_generator():
    b = ""
    for x in range(randint(1,30)):
        b += choice(ascii_letters)
    return b

def random_number_generator():
    h = ""
    for o in range(randint(1,30)):
        h += str(randint(0,9))
    return h

for r in range(18277):
    n = random_string_generator()
    if len(n) < 15:
        n = random_number_generator()
    v.append(n)
answer_1_true = v[1]
answer_2_true = v[2]
answer_3_true = v[3].isdigit()
answer_4_true = v[4]
answer_5_true = v[5].isdigit()

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
