from random import seed
from random import randint
seed(1718600)

t = []
l = []
o = []
for r in range(19567):
    l.append(randint(0,781))

for n in range(19567):
    o.append(randint(0,781))

for j in range(19567):
    t.append(comparator(o[j], l[j]))
