import numpy as np
from random import choice
from random import shuffle
from numpy.random import seed
from numpy.random import randint
from string import ascii_letters


seed(135)

_5 = '2, :'
_5_dimension = 1
a = []

def quest_5(the_list):
    idx = _5.split(', ')
    if _5_dimension == 1:
        idx = _5[0]
        return  'array constituido somente por letras'  if int(idx) % 2 == 0 \
               else str('array constituido somente por ' + pt_numeros) 
    return str(the_list[:,int(_5[1])])

