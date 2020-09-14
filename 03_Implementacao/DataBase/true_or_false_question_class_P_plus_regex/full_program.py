from random import randint
from random import seed
import re

seed(135)

a = []
b = []

class P:
    __var = 7

    def __init__(self, num = 0):
        self.num = num

    def get_var(self):
        return self.__var


def power(num, exp):
    if isinstance(num, P):
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

for i in range(13):
    value = randint(3, 33)
    a.append(P(value))
    b.append(str(value))

p = P()
answer_1_true = regular_search("2", b)
new_b = regular_subtitution("1", "2", b)
answer_2_true = regular_search("2", new_b) / answer_1_true
answer_3_true = a[3].num
new_new_b = regular_subtitution("[^2]", "2", new_b)
answer_4_true = regular_search("2", new_new_b) 
answer_5_true = power(a[3].num, 2)
print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
