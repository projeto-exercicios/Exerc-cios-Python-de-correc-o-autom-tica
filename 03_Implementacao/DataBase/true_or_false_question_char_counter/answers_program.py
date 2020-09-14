# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))
    
answer_1_true = letter_occurence(letter, a[1])
answer_2_true = min(a, key=len)
answer_3_true = a[3]
answer_4_true = max_num_occurences(a)
answer_5_true = len(a[5])

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
