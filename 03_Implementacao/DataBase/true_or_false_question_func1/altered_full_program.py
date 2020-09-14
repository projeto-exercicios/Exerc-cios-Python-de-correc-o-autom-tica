from random import randint
from random import seed
seed(1472072)
l = []
def func1():
    global l
    u = range(19192);
    for k in u:
        l.append(randint(859,2339))
        
func1()
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(c))
#print('list max = ', max(c))

answer_1_true = l[1]
answer_2_true = l[2]
answer_3_true = l[3]
answer_4_true = l[4]
answer_5_true = l[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
