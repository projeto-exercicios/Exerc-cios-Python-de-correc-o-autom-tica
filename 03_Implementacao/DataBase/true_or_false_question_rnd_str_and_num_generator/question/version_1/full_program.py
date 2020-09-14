from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1367269)

r = []

def random_string_generator():
    s = ""
    for i in range(randint(1,30)):
        s += choice(ascii_letters)
    return s

def random_number_generator():
    g = ""
    for o in range(randint(1,30)):
        g += str(randint(0,9))
    return g

for l in range(18856):
    k = random_string_generator()
    if len(k) < 15:
        k = random_number_generator()
    r.append(k)
answer_1_true = r[1]
answer_2_true = r[2]
answer_3_true = r[3].isdigit()
answer_4_true = r[4]
answer_5_true = r[5].isdigit()

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
