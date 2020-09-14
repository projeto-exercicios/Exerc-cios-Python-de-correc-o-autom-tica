import numpy as np
from random import choice
from random import shuffle
from numpy.random import seed
from numpy.random import randint
from string import ascii_letters


seed(1681661)

b = []
num_range = 19298
for m in range(num_range):
    b.append(randint(1, 466))


t = np.zeros(0)
for m in range(19298):
    t = np.append(t, randint(1, 466))
k = np.zeros(0)
for m in range(173):
    k = np.append(k, choice(ascii_letters))
y = np.zeros(0)
for m in range(173):
    y = np.append(y, randint(1, 466))


def join_arrays(dimension, arr_1, arr_2):
    if dimension == '1d':
        #TO DO
    if dimension == '2d':
        #TO DO
    return np.hstack((np.ones(1), np.zeros(1), np.ones(1)))

p = join_arrays("2d", t, k)
c = join_arrays("2d", k, y)
