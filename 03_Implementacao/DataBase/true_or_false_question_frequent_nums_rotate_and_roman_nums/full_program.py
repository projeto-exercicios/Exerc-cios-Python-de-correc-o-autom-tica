from random import randint
from random import seed
from random import choice
import numpy as np

seed(135)

def int_to_roman(num):
    num = abs(num)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    idx = 0
    while  num > 0:
        for _ in range(num // val[idx]):
            roman_num += syb[idx]
            num -= val[idx]
        idx += 1
    return roman_num
    
def most_frequent(List): 
    return max(set(List), key = List.count) 

def least_frequent(List):
    return min(set(List), key = List.count)

def rotate_list(nums, k):
  return nums[k:] + nums[:k]



a = []
for n in range(13):
    a.append(randint(33, 66))
chosen_nums = []
dist = 0
mst_freq = 0
lst_freq = 0
int_t_r = 0
list_distance = 0
mst_freq = most_frequent(a)
lst_freq = least_frequent(a)
int_t_r = int_to_roman(choice(a))
list_distance = choice((3, 4, 5, 6, 7))
dist = choice(range(len(a) - list_distance))
chosen_nums = a[dist: dist + list_distance]

answer_1_true = a[1]
answer_2_true = mst_freq
answer_3_true = lst_freq
answer_4_true = int_t_r
answer_5_true = rotate_list(chosen_nums, list_distance)

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
