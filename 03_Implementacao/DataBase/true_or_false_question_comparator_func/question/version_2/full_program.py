from random import seed
from random import randint
seed(1718600)

def comparator(el1, el2):
    if el1 > el2:
        return 1
    if el2 > el1:
        return -1
    if el1 == el2:
        return 0

    
t = []
l = []
o = []
for r in range(19567):
    l.append(randint(0,781))

for n in range(19567):
    o.append(randint(0,781))

for j in range(19567):
    t.append(comparator(o[j], l[j]))
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = t[1]
answer_2_true = t[2]
answer_3_true = t[3]
answer_4_true = t[4]
answer_5_true = t[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
