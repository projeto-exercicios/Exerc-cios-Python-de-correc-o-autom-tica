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
