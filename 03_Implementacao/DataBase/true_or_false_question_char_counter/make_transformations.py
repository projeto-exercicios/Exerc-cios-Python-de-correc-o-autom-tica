
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
from random import sample
from random import choice
from random import randint
from random import shuffle

from text_transformer.tt_text_transformer_interface import add_changeable
#from text_transformer.tt_text_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import change_one_occurrence

# # this import removes an import error. I don't know why (jbs
# # 2018/12/12). see pt_import_tests.py and try to correct the problem.
# import py_transformer.ast_processor

# from python_transformer.pt_python_transformer_interface import change_identifier_all_occurrences
# from python_transformer.pt_python_transformer_interface import change_all_occurrences_in_strings
from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences

#from sympy import latex, sympify





# in the question (program)
add_changeable('135') # seed
add_changeable('a')      # the list
add_changeable('i')      # the loop variable. this was added after an
add_changeable('k')      # error ocurred. see ERROR below
add_changeable('l')      # result of random_string_generator()
add_changeable('m')      # optimized message

add_changeable('10')     # the list length
add_changeable('15')     # max length of a string

# answers list name
add_changeable(r'\verb+a+')

# answer index
add_changeable(r'\verb+b+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
add_changeable(r'\verb+3+')
add_changeable(r'\verb+4+')
add_changeable(r'\verb+5+')

# right answers values
add_changeable(r'\verb+11+')
add_changeable(r'\verb+22+')
add_changeable(r'\verb+33+')
add_changeable(r'\verb+44+')
add_changeable(r'\verb+55+')

# wrong answers values
add_changeable(r'\verb+111+')
add_changeable(r'\verb+222+')
add_changeable(r'\verb+333+')
add_changeable(r'\verb+444+')
add_changeable(r'\verb+555+')





# variáveis partilhas entre as funções make_transformations e
# make_transformations_on_results
a  = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None
the_list = None




def make_transformations():

    ''
    global a
    global _1
    global _2
    global _3
    global _4
    global _5
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, i, k, l, m] = sample(string.ascii_lowercase, 5)
    _10 = randint(19000, 20000)
    _15 = randint(10, 20)
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('i', i)
    change_token_all_occurrences('k', k)
    change_token_all_occurrences('l', l)
    change_token_all_occurrences('m', m)
    change_all_occurrences('10', str(_10))
    change_all_occurrences('15', str(_15))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    
    # indexes with no repetitions
    [_1,_3, _4, _5] = sample(range(_10), 4)

    
    change_all_occurrences(r'\verb+b+', r'\verb+' + str(_1) + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + str(_3) + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global _1
    global _2
    global _3
    global _4
    global _5
    global the_list
 
    the_list = program.get_global(a)

    letter = choice(the_list[_1])
    change_all_occurrences(r'\verb+1+', r'\verb+' + letter + '+')
    word, equasion = choice_to_do()
    change_all_occurrences(r'\verb+2+', r'\verb+' + word + '+')
    letter_2, max_occur = max_num_occurences(the_list)
    change_all_occurrences(r'\verb+4+', r'\verb+' + letter_2 + '+')
    answer_1_true = letter_occurence(letter, the_list[_1])
    answer_2_true = equasion
    answer_3_true = the_list[_3]
    answer_4_true = max_occur
    answer_5_true = len(the_list[_5])  

    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment1 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1 if answer_1_true > 1 else answer_1_true + 1
    answer_2_false = find_word_with_different_length(the_list, len(equasion), word, answer_2_true)
    answer_3_false = the_list[_3 + increment3]
    answer_4_false = answer_4_true + increment4
    answer_5_false = answer_5_true + increment5

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))

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
    letter =''
    for cod in lista:
        for word in lowercase:
            num = letter_occurence(word, cod)
            if num > maxOccur:
                maxOccur = num
                letter = word
    return letter, maxOccur

def choice_to_do():
    var = choice((1,2))
    if var == 1:
        return "menor" , min(the_list, key=len)
    else:
        return "maior" , max(the_list, key=len)

def find_word_with_different_length(lista, length, choice_to_do, answer_2_true):
    if choice_to_do == "maior" and length == 1:
        for word in lista:
            if word != answer_2_true:
                return word
    else:
        val = 1 if choice_to_do == "menor" else -1 
        newLength = length + val
        while(True):
            for word in lista:
                if len(word) == newLength:
                    return word
            newLength += val
    
