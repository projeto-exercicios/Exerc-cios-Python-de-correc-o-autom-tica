from random import randint
from random import seed
import numpy as np
seed(1501676)

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
    for h in range(len(r_num)):
        if r_num[h] == '1':
            idxs.append(h)
    result = 0
    for h in idxs:
        result += 2**h
    return result * mult


def binary_sum(num1, num2):
    d_num1 = bin_to_dec(num1)
    d_num2 = bin_to_dec(num2)
    result = d_num1 + d_num2
    return to_bits(result)
    
d = []
g = []
v = []

dim = 19566
for h in range(dim):
    d.append(randint(-2**31, 2**31))

q = Reverser()
for h in range(dim):
    g.append(q.reverse(d[h]))

for h in range(dim):
    v.append(q.reverse(g[h]))
