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
e = join_arrays("2d", b, c)
f = []
f = join_arrays("2d", c, d)
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = a[1]
answer_2_true = a[2]
answer_3_true = a[3]
answer_4_true = a[4]
answer_5_true = a[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
