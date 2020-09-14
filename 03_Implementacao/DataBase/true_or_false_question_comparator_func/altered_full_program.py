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
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = y[1]
answer_2_true = y[2]
answer_3_true = y[3]
answer_4_true = y[4]
answer_5_true = y[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
