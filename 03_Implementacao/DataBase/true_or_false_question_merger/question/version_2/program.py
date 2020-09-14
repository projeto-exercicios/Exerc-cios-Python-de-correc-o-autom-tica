from random import randint
from random import seed

seed(1264564)

o = []
q = []
m = []
v = []
x = []

def take_out_repetitions(nums):
    new_nums = []
    for num in nums:
        if num not in new_nums:
            new_nums.append(num)
    return new_nums

def checker(num1, num2):
    if num1[0] >= num2[0] and num1[1] >= num2[0]:
        if num1[0] <= num2[1] and num1[1] <= num2[1]:
            return True
    return False
        
def can_be_merged(num_to_check, nums, write_in_dict):
    for num in nums:
        if num == num_to_check:
            continue
        if checker(num_to_check, num):
            if write_in_dict:
                if str(num) in dic:
                    dic[str(num)] +=1
                else:
                    dic[str(num)] =1
                print(dic)
            return True
    return False

def merge(nums, write_in_dict = False):
    new_nums = []
    for num in nums:
        result = can_be_merged(num, nums, write_in_dict)
        if result:
            continue
        else:
            new_nums.append(num)
    return new_nums



dim = 19263
for w in range(dim):
    o.append([randint(447,652),randint(652,1304)])

q = take_out_repetitions(o)
m = merge(q)
v = merge(o)



for idx in m:
    x.append(idx[1] - idx[0])
