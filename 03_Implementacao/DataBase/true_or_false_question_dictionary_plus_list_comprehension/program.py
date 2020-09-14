import random
from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(135)


a = []
str_a = 0
int_a = 0
dic = []
d = []
for n in range(13):
    a.append(choice((randint(3,33), choice(ascii_letters))))


def str_int_splitter(List):
    return [x for x in List if isinstance(x, str)], \
           [x for x in List if isinstance(x, int)]


def create_dict(str_a, int_a):
    d = {}
    size_str_a = len(str_a)
    size_int_a = len(int_a)
    for i in range(size_str_a):
        if i < size_str_a:
            d[str_a[i]] = int_a[i % size_int_a]
        else:
            d[str_a[i]] = ''
    return d

def get_max_key():
    return max(d, key=d.get)

def get_min_key():
    return min(d, key=d.get)

class Dictionary:

    def __init__(self, dictionary):
        self.d = dictionary


    def __getitem__(self, var):
        if isinstance(var, str):
            return [value for key, value in self.d.items() if key == var]
        if isinstance(var, int):
            return [key for key, value in self.d.items() if value == var]
        else: return "None"

    def __setitem__(self, key, value):
        self.d[key] = value

    def __repr__(self):
        str_dict = "{"
        for key, value in self.d.items():
            str_dict +=  "'" + key + "'" + ': ' + str(value) + ', '
        return str_dict[:-2] + '}'

    def __len__(self):
        return len(self.d)
        

str_a, int_a = str_int_splitter(a)
d = create_dict(str_a, int_a)
dic = Dictionary(d)
