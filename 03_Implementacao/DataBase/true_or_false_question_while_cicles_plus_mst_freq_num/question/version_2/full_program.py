import random
from random import randint
from random import seed

seed(1941706)


i = []
for s in range(19601):
    i.append(randint(1,35))

x = 0

def while_1():
    while x < 5:
        print(x + 1)

def while_2():
    while x < 5:
        if x == 4:
            x = 0
        print(x)
        x += 1

def while_3():
    global x
    while x < 5:
        print(x)
        x += 1


def most_frequent_num(nums, max_num):
    nums = [x for x in nums if x < max_num]
    if len(nums) == 0:
        return "None"
    else:
        return max(set(nums), key = nums.count)


def counter_0(nums):
    return len([x for x in nums if x % 2 != 0 or x == 0])

def counter_1(nums):
    return len([x for x in nums if x % 2 != 0 and x == 0])

def counter_2(nums):
    return len([x for x in nums if x % 2 != 0 or x != 0])

def counter_3(nums):
    return len([x for x in nums if x % 2 != 0 and x != 0])

def counter_4(nums):
    return len([x for x in nums if x % 2 != 0])

def counter_5(nums):
    return len([x for x in nums if x % 2 == 0 or x == 0])

def counter_6(nums):
    return len([x for x in nums if x % 2 == 0 and x == 0])

def counter_7(nums):
    return len([x for x in nums if x % 2 == 0 or x != 0])

def counter_8(nums):
    return len([x for x in nums if x % 2 == 0 and x != 0])

def counter_9(nums):
    return len([x for x in nums if x % 2 == 0]) 
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python1

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = i[1]
answer_2_true = i[2]
answer_3_true = i[1]
answer_4_true = i[4]
answer_5_true = i[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
