from random import randint
from random import choice
from random import seed

seed(1749806)

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
    
j = []

for f in range(19760):
    value = randint(1, 220)
    j.append(value)

b = M(j)
