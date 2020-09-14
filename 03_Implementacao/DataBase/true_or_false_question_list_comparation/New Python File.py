from random import seed
from random import randint
seed(135)

a = []
b = []
f = []
for c in range(9):
    b.append(randint(0,9))

for d in range(30):
    a.append(randint(0,9))

for e in range(30):
    if a[e] == b[(e + 1)%len(b)]:
        f.append(True)
    if a[e] != b[(e + 1)%len(b)]:
        f.append(False)
        
