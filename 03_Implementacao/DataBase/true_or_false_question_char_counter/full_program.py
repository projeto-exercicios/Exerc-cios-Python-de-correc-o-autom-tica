from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(135)

a = []

def random_string_generator():
    l = ""
    my_str = ""
    for i in range(0,3):
        my_str += choice(ascii_letters).lower()
    for k in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        l += choice(my_str)
    return l

def message_optimizator(my_str):
    char_to_evaluate = my_str[0]
    finalMessage = ""
    counter = 1
    char_occurence = 1
    if len(my_str) == 1:
        return my_str
    for char in my_str[1:]:
        counter += 1
        if char_to_evaluate == char:
            char_occurence += 1
        if char_to_evaluate != char:
            finalMessage += char_to_evaluate
            finalMessage += str(char_occurence) if char_occurence > 1 else ''
            char_to_evaluate = char
            char_occurence = 1
        if counter == len(my_str):
            finalMessage += char_to_evaluate
            finalMessage += str(char_occurence) if char_occurence > 1 else ''

    return finalMessage

for i in range(10):
    l = random_string_generator()
    m = message_optimizator(l)
    a.append(m)
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
