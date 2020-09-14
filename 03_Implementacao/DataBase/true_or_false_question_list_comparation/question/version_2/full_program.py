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
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = v[1]
answer_2_true = s[2]
answer_3_true = v[3]
answer_4_true = s[4]
answer_5_true = v[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
