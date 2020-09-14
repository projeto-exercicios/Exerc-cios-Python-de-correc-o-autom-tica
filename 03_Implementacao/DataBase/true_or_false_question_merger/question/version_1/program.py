from random import randint
from random import seed

seed(1241846)

b = []
f = []
k = []
o = []
p = []

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



dim = 19863
for t in range(dim):
    b.append([randint(405,868),randint(868,1736)])

f = take_out_repetitions(b)
k = merge(f)
o = merge(b)



for idx in k:
    p.append(idx[1] - idx[0])
