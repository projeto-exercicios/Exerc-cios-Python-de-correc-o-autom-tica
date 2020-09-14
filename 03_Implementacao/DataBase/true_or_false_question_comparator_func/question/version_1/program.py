from random import seed
from random import randint
seed(1599060)

def comparator(el1, el2):
    if el1 > el2:
        return 1
    if el2 > el1:
        return -1
    if el1 == el2:
        return 0

    
y = []
c = []
l = []
for t in range(19223):
    c.append(randint(0,226))

for n in range(19223):
    l.append(randint(0,226))

for h in range(19223):
    y.append(comparator(l[h], c[h]))
