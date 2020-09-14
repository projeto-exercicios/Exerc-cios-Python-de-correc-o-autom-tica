from random import seed
from random import choice
from random import randint
from string import ascii_letters
seed(1850201)

t = []

def random_string_generator():
    f = ""
    my_str = ""
    for z in range(0,3):
        my_str += choice(ascii_letters).lower()
    for s in range(randint(1,20)):
        idx = randint(1,len(my_str) - 1)
        f += choice(my_str)
    return f

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

for z in range(19891):
    f = random_string_generator()
    l = message_optimizator(f)
    t.append(l)

letter = choice(t[1])
def letter_occurence(letter, string):
    idx = 0
    counter = 0
    for ch in string:
        if ch != letter: continue
        if ch == letter:
            counter +=1
            if idx < len(string) - 1:
                num = int(string[idx + 1]) if  string[idx + 1].isdigit() else 0
                counter +=num
            idx +=1
    return counter

def max_num_occurences(lista):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']
    maxOccur = 0
    choosenLetter =''
    for cod in lista:
        for letter in lowercase:
            num = letter_occurence(letter, cod)
            if num > maxOccur:
                maxOccur = num
                choosenLetter = letter
    return choosenLetter, maxOccur

def find_word_with_bigger_length(lista, length):
    newLength = length + 1
    while(True):
        for word in lista:
            if len(word) == newLength:
                return word
        newLength += 1
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))
    
answer_1_true = letter_occurence(letter, t[1])
answer_2_true = min(t, key=len)
answer_3_true = t[3]
answer_4_true = max_num_occurences(t)
answer_5_true = len(t[5])

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
