import numpy as np
from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(135)

la = []
lb = []
lc = []

for i in range(10):
    pixel = [randint(0,255), randint(0,255), randint(0,255)]
    la.append(pixel)
answer_1_true = la[1]
answer_2_true = la[2]
answer_3_true = la[3]
answer_4_true = la[4]
answer_5_true = la[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
