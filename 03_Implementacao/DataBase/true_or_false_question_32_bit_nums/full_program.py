from random import randint
from random import seed
import numpy as np
seed(135)

class Reverser:

    def reverse(self, num):
        num_check = num if not isinstance(num, str) else bin_to_dec(num)
        if num_check < - 2**31 or num_check >= 2**31:
            return 0
        else:
            if(isinstance(num, str)):
                num_str = str(num)
                mult = ''
                if num_str[0] == '-':
                    num_str = num_str[1:]
                    mult = '-'
                return mult + (num_str[::-1])
            if(not isinstance(num, str)):
                num_str = str(num)
                mult = 1
                if num_str[0] == '-':
                    num_str = num_str[1:]
                    mult = -1
                return int(num_str[::-1]) * mult


def to_bits(num):
  return '{0:01b}'.format(num)


def bin_to_dec(num):
    if(not isinstance(num, str)): num = str(num)
    mult = 1
    if num[0] == '-':
        num = num[1:]
        mult = -1
    r_num = num[::-1]
    idxs = []
    for i in range(len(r_num)):
        if r_num[i] == '1':
            idxs.append(i)
    result = 0
    for i in idxs:
        result += 2**i
    return result * mult


def binary_sum(num1, num2):
    d_num1 = bin_to_dec(num1)
    d_num2 = bin_to_dec(num2)
    result = d_num1 + d_num2
    return to_bits(result)
    
a = []
b = []
c = []

dim = 13
for i in range(dim):
    a.append(randint(-2**31, 2**31))

r = Reverser()
for i in range(dim):
    b.append(r.reverse(a[i]))

for i in range(dim):
    c.append(r.reverse(b[i]))
answer_1_true = a[1]
answer_2_true = b[2]
answer_3_true = sum(np.array(a) != np.array(c) * 1.0)
answer_4_true = sum(np.array(c) == 0 * 1.0)
answer_5_true = r.reverse(binary_sum(to_bits(a[0]),to_bits(b[0])))


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
