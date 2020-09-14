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
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = a[1]
answer_2_true = f[2]
answer_3_true = a[3]
answer_4_true = f[4]
answer_5_true = a[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
