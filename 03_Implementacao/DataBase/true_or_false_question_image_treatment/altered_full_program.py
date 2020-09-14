import numpy as np
from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1338344)

n = []
o = []
k = []

for s in range(19054):
    pixel = [randint(0,255), randint(0,255), randint(0,255)]
    n.append(pixel)
answer_1_true = n[1]
answer_2_true = n[2]
answer_3_true = n[3]
answer_4_true = n[4]
answer_5_true = n[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
