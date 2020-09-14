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
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = c[1]
answer_2_true = d[2]
answer_3_true = c[3]
answer_4_true = d[4]
answer_5_true = c[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
