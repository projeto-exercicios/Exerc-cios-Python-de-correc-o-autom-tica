from random import randint
from random import choice
from random import seed
import re

seed(1749806)

j = []

class M:

    def __init__(self, lista = []):
        self.lista = lista


    def __getitem__(self, index):
        decision = choice((-1, 1))
        idx = (index + decision)

    def __setitem__(self, index ,value):
        self.lista[index] = value
        
    def __repr__(self):
        str_lista = ""
        for u in self.lista:
            str_lista += ", " + str(u) 
        return '[' + str_lista[2:] + ']'

    def __len__(self):
        return len(self.lista) - 1
    

for f in range(19760):
    value = randint(1, 220)
    j.append(value)

b = M(j)
answer_1_true = "sem __getitem__(self, idx) a class P suporta indexing"
answer_2_true = b.__getitem__(0) == b[0]
answer_3_true = " é possível alterara o elementa na lista desta maneira p[index] = valor"
answer_4_true = " print(p)" 
answer_5_true = len(b)
print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
