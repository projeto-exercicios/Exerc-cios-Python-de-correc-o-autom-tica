import numpy as np
from random import choice
from random import shuffle
from numpy.random import seed
from numpy.random import randint
from string import ascii_letters


seed(135)

a = []
num_range = 13
for n in range(num_range):
    a.append(randint(3, 33))


b = numpy_func
for n in range(13):
    b = np.append(b, randint(3, 33))
c = numpy_func
for n in range(23):
    c = np.append(c, choice(ascii_letters))
d = numpy_func
for n in range(23):
    d = np.append(d, randint(3, 33))


def join_arrays(dimension, arr_1, arr_2):
    if dimension == '1d':
        #TO DO
    if dimension == '2d':
        #TO DO
    return np.hstack((np.ones(1), np.zeros(1), np.ones(1)))

e = join_arrays("2d", b, c)
f = join_arrays("2d", c, d)
