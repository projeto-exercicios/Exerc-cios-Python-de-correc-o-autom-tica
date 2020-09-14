from random import seed
from random import randint
seed(1394663)

v = []
h = []
s = []
for j in range(9):
    h.append(randint(0,9))

for d in range(19039):
    v.append(randint(0,9))

for r in range(19039):
    if v[r] == h[(r + 1)%len(h)]:
        s.append(True)
    if v[r] != h[(r + 1)%len(h)]:
        s.append(False)
