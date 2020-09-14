from random import randint
from random import choice
from random import seed

seed(1875861)

class O:

    def __init__(self, lista = []):
        self.lista = lista


    def __getitem__(self, index):
        decision = choice((-1, 1))
        idx = (index + decision)

    def __setitem__(self, index ,value):
        self.lista[index] = value
        
    def __repr__(self):
        str_lista = ""
        for q in self.lista:
            str_lista += ", " + str(q) 
        return '[' + str_lista[2:] + ']'

    def __len__(self):
        return len(self.lista) - 1
    
i = []

for g in range(19421):
    value = randint(1, 215)
    i.append(value)

b = O(i)
