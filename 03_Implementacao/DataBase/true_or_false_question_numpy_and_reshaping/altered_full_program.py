import numpy as np
from random import choice
from random import shuffle
from numpy.random import seed
from numpy.random import randint
from string import ascii_letters


seed(1545964)

t = []
num_range = 19751
for m in range(num_range):
    t.append(randint(0, 191))


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


w = np.eye(0)
for m in range(19751):
    w = np.append(w, randint(0, 191))
j = np.eye(0)
for m in range(74):
    j = np.append(j, choice(ascii_letters))
q = np.eye(0)
for m in range(74):
    q = np.append(q, randint(0, 191))


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

c = []
c = join_arrays("2d", w, j)
b = []
b = join_arrays("2d", j, q)
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python0

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = t[1]
answer_2_true = t[2]
answer_3_true = t[0]
answer_4_true = t[4]
answer_5_true = t[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
