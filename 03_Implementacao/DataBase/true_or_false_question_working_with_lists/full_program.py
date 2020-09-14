from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(135)

a = []
b = []
def random_string_generator():
    l = ""
    for k in range(randint(1,15)):
        l += choice(ascii_letters)
    return l


for i in range(10):
    a.append(randint(0, 50))
    b.append(random_string_generator())


d = a

for i in range(20):
    a[i%len(a)] =  a[i%len(a)] * 3
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
