from random import seed
from random import randint
seed(1303994)

c = []
n = []
d = []
for v in range(9):
    n.append(randint(0,9))

for a in range(19091):
    c.append(randint(0,9))

for m in range(19091):
    if c[m] == n[(m + 1)%len(n)]:
        d.append(True)
    if c[m] != n[(m + 1)%len(n)]:
        d.append(False)
