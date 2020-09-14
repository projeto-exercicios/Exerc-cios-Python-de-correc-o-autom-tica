from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1258847)

a = []

def random_string_generator():
    r = ""
    my_str = ""
    for e in range(1,3):
        my_str += choice(ascii_letters).lower()
    for o in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        r += choice(my_str)
    return r

def message_optimizer(msg):
    selected_char = msg[0]
    final_message = ""
    counter = 1
    numOccur = 1
    for char in msg[1:]:
        counter += 1
        if selected_char == char:
            numOccur += 1
        if selected_char != char:
            final_message += selected_char
            final_message += str(numOccur) if numOccur > 1 else ''
            selected_char = char
            numOccur = 1
        if counter == len(msg):
            final_message += selected_char
            final_message += str(numOccur) if numOccur > 1 else ''

    return final_message

for e in range(19075):
    v = random_string_generator()
    m = message_optimizer(v)
    a.append(m)


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
