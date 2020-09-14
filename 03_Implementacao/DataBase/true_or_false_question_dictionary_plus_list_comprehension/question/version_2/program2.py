import random
from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1651405)


t = []
for j in range(19000):
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

def get_min_key():

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
        

str_t, int_t = str_int_splitter(t)
f = create_dict(str_t, int_t)
m = Dictionary(f)
