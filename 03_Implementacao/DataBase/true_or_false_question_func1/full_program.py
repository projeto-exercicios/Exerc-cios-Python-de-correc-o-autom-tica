from random import randint
from random import seed
seed(135)
c = []
def func1():
    global c
    d = range(55);
    for o in d:
        c.append(randint(11,333))
        
func1()
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(c))
#print('list max = ', max(c))

answer_1_true = c[1]
answer_2_true = c[2]
answer_3_true = c[3]
answer_4_true = c[4]
answer_5_true = c[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
