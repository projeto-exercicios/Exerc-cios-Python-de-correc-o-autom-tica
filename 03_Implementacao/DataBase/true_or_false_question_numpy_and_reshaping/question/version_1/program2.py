import numpy as np
from random import choice
from random import shuffle
from numpy.random import seed
from numpy.random import randint
from string import ascii_letters


seed(1616638)

m = []
num_range = 19372
for k in range(num_range):
    m.append(randint(5, 191))


p = np.array([])
for k in range(19372):
    p = np.append(p, randint(5, 191))
z = np.array([])
for k in range(300):
    z = np.append(z, choice(ascii_letters))
g = np.array([])
for k in range(300):
    g = np.append(g, randint(5, 191))


def join_arrays(dimension, arr_1, arr_2):
    if dimension == '1d':
        #TO DO
    if dimension == '2d':
        #TO DO
    return np.hstack((np.ones(1), np.zeros(1), np.ones(1)))

e = join_arrays("2d", p, z)
o = join_arrays("2d", z, g)
