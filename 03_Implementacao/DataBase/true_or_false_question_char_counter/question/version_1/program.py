from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1938043)

o = []

def random_string_generator():
    b = ""
    my_str = ""
    for w in range(0,3):
        my_str += choice(ascii_letters).lower()
    for y in range(randint(1,15)):
        idx = randint(1,len(my_str) - 1)
        b += choice(my_str)
    return b

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

for w in range(19049):
    b = random_string_generator()
    r = message_optimizator(b)
    o.append(r)
