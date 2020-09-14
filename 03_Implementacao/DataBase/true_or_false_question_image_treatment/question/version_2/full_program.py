import numpy as np
from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1367614)

b = []
i = []
d = []

for r in range(19017):
    pixel = [randint(0,255), randint(0,255), randint(0,255)]
    b.append(pixel)
answer_1_true = b[1]
answer_2_true = b[2]
answer_3_true = b[3]
answer_4_true = b[4]
answer_5_true = b[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
