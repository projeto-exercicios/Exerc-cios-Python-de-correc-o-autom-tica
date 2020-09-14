from random import randint
from random import seed
seed(1464336)
w = []
def func1():
    global w
    i = range(19954);
    for t in i:
        w.append(randint(538,3923))
        
func1()
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(c))
#print('list max = ', max(c))

answer_1_true = w[1]
answer_2_true = w[2]
answer_3_true = w[3]
answer_4_true = w[4]
answer_5_true = w[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
