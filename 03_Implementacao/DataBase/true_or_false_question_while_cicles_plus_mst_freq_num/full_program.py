import random
from random import randint
from random import seed

seed(135)


a = []
for n in range(13):
    a.append(randint(3,33))

c = 0

def while_1():
    while c < 5:
        print(c + 1)

def while_2():
    while c < 5:
        if c == 4:
            c = 0
        print(c)
        c += 1

def while_3():
    global c
    while c < 5:
        print(c)
        c += 1


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
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

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
