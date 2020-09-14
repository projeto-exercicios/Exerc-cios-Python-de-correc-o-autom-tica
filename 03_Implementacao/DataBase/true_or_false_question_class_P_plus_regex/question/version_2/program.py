from random import randint
from random import seed
import re

seed(1743925)

p = []
q = []

class W:
    __g = 7

    def __init__(self, num = 0):
        self.num = num

    def get_var(self):
        return self.__g


def power(num, exp):
    if isinstance(num, W):
        num = num.num
    if exp == 1: return num
    else: return num * power(num, exp - 1)

def regular_search(pattern_val, the_list):
    return sum(list(map(lambda x: 1 if re.search(r"" + pattern_val, x)
                        else 0, the_list)))

def regular_subtitution(pattern_val, subtitute_val, the_list):
    return list(map(lambda x: re.sub(r"" + pattern_val, subtitute_val, x) , the_list))

def regular_match(pattern_val, the_list):
    return sum(list(map(lambda x: 1 if re.match(r"" + pattern_val, x)
                        else 0, the_list)))

for u in range(19406):
    value = randint(3, 1418)
    p.append(W(value))
    q.append(str(value))

t = W()
