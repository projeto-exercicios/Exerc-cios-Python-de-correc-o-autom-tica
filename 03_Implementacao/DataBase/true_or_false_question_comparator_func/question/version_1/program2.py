from random import seed
from random import randint
seed(1599060)

y = []
c = []
l = []
for t in range(19223):
    c.append(randint(0,226))

for n in range(19223):
    l.append(randint(0,226))

for h in range(19223):
    y.append(comparator(l[h], c[h]))
