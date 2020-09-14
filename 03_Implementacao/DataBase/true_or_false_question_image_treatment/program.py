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
