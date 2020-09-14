from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1120117)

o = []
l = []
def random_string_generator():
    v = ""
    for b in range(randint(1,15)):
        v += choice(ascii_letters)
    return v


for t in range(18354):
    o.append(randint(0, 104))
    l.append(random_string_generator())


k = o

for t in range(55062):
    o[t%len(o)] =  o[t%len(o)] * 3
answer_1_true = o[1]
answer_2_true = o[2]
answer_3_true = o[3]
answer_4_true = o[4]
answer_5_true = o[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
