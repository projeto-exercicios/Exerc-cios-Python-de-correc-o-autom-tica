from random import randint
from random import seed
from random import choice
import numpy as np

seed(1029325)

k = []


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


for e in range(2871):
    k.append(randint(1371,7871))

n = longest_consecutive_sequence(k)
a = consecutive_sequences(k)
c , dd = filtered_consecutive_sequences(a)
q = distinct_numbers_in_sequence(c)
answer_1_true = n
answer_2_true = len(n) - 1
answer_3_true = a[1]
lenght = sum(len(x) for x in a)
answer_4_true = round(lenght / len(q),2)
answer_5_true = q[choice(range(len(q)))]


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
