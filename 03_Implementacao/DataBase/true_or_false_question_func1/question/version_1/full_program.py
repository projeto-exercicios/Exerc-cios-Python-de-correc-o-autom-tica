from random import randint
from random import seed
seed(1623537)
a = []
def func1():
    global a
    x = range(19294);
    for j in x:
        a.append(randint(718,1552))
        
func1()
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(c))
#print('list max = ', max(c))

answer_1_true = a[1]
answer_2_true = a[2]
answer_3_true = a[3]
answer_4_true = a[4]
answer_5_true = a[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
