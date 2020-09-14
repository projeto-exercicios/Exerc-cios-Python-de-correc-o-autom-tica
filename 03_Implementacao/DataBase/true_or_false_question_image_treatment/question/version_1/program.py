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
