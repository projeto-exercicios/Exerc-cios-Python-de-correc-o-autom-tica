from random import seed
from random import randint
seed(1303994)

n = []
v = []
d = []
for a in range(9):
    v.append(randint(0,9))

for m in range(19091):
    n.append(randint(0,9))

for y in range(19091):
    if n[y] == v[(y + 1)%len(v)]:
        d.append(True)
    if n[y] != v[(y + 1)%len(v)]:
        d.append(False)
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = n[1]
answer_2_true = d[2]
answer_3_true = n[3]
answer_4_true = d[4]
answer_5_true = n[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
