from random import seed
from random import randint
seed(135)

def comparator(el1, el2):
    if el1 > el2:
        return 1
    if el2 > el1:
        return -1
    if el1 == el2:
        return 0

    
a = []
b = []
f = []
for c in range(300):
    b.append(randint(0,125))

for d in range(300):
    f.append(randint(0,125))

for e in range(300):
    a.append(comparator(f[e], b[e]))
