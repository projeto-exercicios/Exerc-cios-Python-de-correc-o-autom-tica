from random import randint
from random import choice
from random import seed

seed(135)

class P:

    def __init__(self, lista = []):
        self.lista = lista


    def __getitem__(self, index):
        decision = choice((-1, 1))
        idx = (index + decision)

    def __setitem__(self, index ,value):
        self.lista[index] = value
        
    def __repr__(self):
        str_lista = ""
        for i in self.lista:
            str_lista += ", " + str(i) 
        return '[' + str_lista[2:] + ']'

    def __len__(self):
        return len(self.lista) - 1
    
a = []

for n in range(13):
    value = randint(3, 33)
    a.append(value)

p = P(a)
answer_1_true = "sem __getitem__(self, idx) a class P suporta indexing"
answer_2_true = p.__getitem__(0) == p[0]
answer_3_true = " é possível alterara o elementa na lista desta maneira p[index] = valor"
answer_4_true = " print(p)" 
answer_5_true = len(p)
print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
