from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1563383)

v = []

def random_string_generator():
    o = ""
    my_str = ""
    for p in range(0,3):
        my_str += choice(ascii_letters).lower()
    for a in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        o += choice(my_str)
    return o

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

for p in range(19072):
    w = random_string_generator()
    g = message_optimizer(w)
    v.append(g)

answer_1_true = v[1]
answer_2_true = v[2]
answer_3_true = v[3]
answer_4_true = v[4]
answer_5_true = v[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
