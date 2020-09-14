import random
from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1651405)


t = []
str_t = 0
int_t = 0
m = []
f = []
for j in range(19601):
    t.append(choice((randint(4,361), choice(ascii_letters))))


def str_int_splitter(List):
    return [b for b in List if isinstance(b, str)],           [b for b in List if isinstance(b, int)]


def create_dict(str_t, int_t):
    f = {}
    size_str_a = len(str_t)
    size_int_a = len(int_t)
    for i in range(size_str_a):
        if i < size_str_a:
            f[str_t[i]] = int_t[i % size_int_a]
        else:
            f[str_t[i]] = ''
    return f

def get_max_key():
    return max(f, key=f.get)

def get_min_key():
    return min(f, key=f.get)

class Dictionary:

    def __init__(self, dictionary):
        self.f = dictionary


    def __getitem__(self, var):
        if isinstance(var, str):
            return [value for key, value in self.f.items() if key == var]
        if isinstance(var, int):
            return [key for key, value in self.f.items() if value == var]
        else: return "None"

    def __setitem__(self, key, value):
        self.f[key] = value

    def __repr__(self):
        str_dict = "{"
        for key, value in self.f.items():
            str_dict +=  "'" + key + "'" + ': ' + str(value) + ', '
        return str_dict[:-2] + '}'

    def __len__(self):
        return len(self.f)
        

str_t, int_t = str_int_splitter(t)
f = create_dict(str_t, int_t)
m = Dictionary(f)
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python4

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = t[1]
answer_2_true = t[2]
answer_3_true = t[4]
answer_4_true = t[4]
answer_5_true = t[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
