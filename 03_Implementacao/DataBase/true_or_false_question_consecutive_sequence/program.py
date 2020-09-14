from random import randint
from random import seed
from random import choice
import numpy as np

seed(135)

a = []


def longest_consecutive_sequence(nums):
    longest_consec = []
    for num in nums:
        consec = []
        num_to_see = num
        consec.append(num)
        while True:
            num_to_see +=1
            if num_to_see in nums:
                consec.append(num_to_see)
            else: break
        if len(consec) > 1:
            longest_consec.append(consec)
    longest_consec.sort()
    return max(longest_consec, key=len)


def consecutive_sequences(nums):
    longest_consecs = []
    for num in nums:
        consec = []
        num_to_see = num
        consec.append(num)
        while True:
            num_to_see +=1
            if num_to_see in nums:
                consec.append(num_to_see)
            else: break
        if len(consec) > 1:
            longest_consecs.append(consec)
    
    return longest_consecs


def filtered_consecutive_sequences(nums):
    consec_sequences = []
    for consec in nums:
        if consec not in consec_sequences:
            consec_sequences.append(consec)
    consec_sequences.sort()
    return consec_sequences, round(len(nums) / len(consec_sequences),2)

def distinct_numbers_in_sequence(nums):
    dist_nums = []
    for num in nums:
        for n in num:
            if n not in dist_nums:
                dist_nums.append(n)

    return dist_nums


for i in range(150):
    a.append(randint(70,450))

b = longest_consecutive_sequence(a)
c = consecutive_sequences(a)
d , dd = filtered_consecutive_sequences(c)
e = distinct_numbers_in_sequence(d)
