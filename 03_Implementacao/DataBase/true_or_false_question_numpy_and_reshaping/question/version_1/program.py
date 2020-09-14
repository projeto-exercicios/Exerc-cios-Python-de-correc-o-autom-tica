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


def possible_shape(num):
    idxs = [x for x in range(101)]
    idxs = idxs[1:]
    idxs = idxs[::-1]
    nums_remainder_0 = [x for x in idxs if (num % x)== 0]
    result = []
    result.append(choice(nums_remainder_0))
    result.append(int(num / result[0]))
    shuffle(result)
    return result, nums_remainder_0


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
        return np.hstack((arr_1, arr_2))
    if dimension == '2d':
        dimension_diff = len(arr_1) - len(arr_2)
        if dimension_diff < 0:
            return np.vstack((np.hstack((arr_1, np.ones(abs(dimension_diff)))),
                              arr_2))
        else:
            return np.vstack((arr_1,
                              np.hstack((arr_2, np.ones(abs(dimension_diff))))))
    return np.hstack((np.ones(1), np.zeros(1), np.ones(1)))

e = []
e = join_arrays("2d", p, z)
o = []
o = join_arrays("2d", z, g)
