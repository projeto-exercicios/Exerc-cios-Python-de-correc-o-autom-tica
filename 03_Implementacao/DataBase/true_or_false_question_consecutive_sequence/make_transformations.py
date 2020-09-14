
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
add_changeable('b')      # result of longest_consecutive_sequence()
add_changeable('c')      # result consecutive_sequences()
add_changeable('d')      # result de filtered_consecutive_sequences()
add_changeable('e')      # result de distinc_numbers_in_sequence()
add_changeable('i')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('150')    # the list length
add_changeable('70')     # min randint value
add_changeable('450')    # max randint value

# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+b+')
add_changeable(r'\verb+c+')
add_changeable(r'\verb+d+')
add_changeable(r'\verb+e+')


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
b = None
c = None
d = None
e = None






def make_transformations():

    ''
    global a
    global b
    global c
    global d
    global e

    
    # question
    _135 = str(randint(1000000, 2000000))
    a = choice(string.ascii_lowercase) # ERROR: isto está mal!!!  a letra 'a'
    # não pode ser uma letra qualquer. porque se for igual a 'n' como
    # há no programa uma variável 'n' isto vai causar um erro
    # deexecuçaõ. Intermitente, o que ainda é pior
    # soluções possíveis:
    # 1. escolher uma letra qualquer execto o 'n'
    # 2. substituir também a variável 'n' escolhendo duas letras diferentes
    # vai ser usada a solução 2 porque assim as versões ainda ficam
    # mais diferentes. a variável 'n' passa também a ser diferente
    [a, b, c, d, e, i] = sample(string.ascii_lowercase, 6)
    _150 = randint(2000, 3000)
    _70 = _150 - 1500
    _450 = _150 + 5000
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('b', b)
    change_token_all_occurrences('c', c)
    change_token_all_occurrences('d', d)
    change_token_all_occurrences('e', e)
    change_token_all_occurrences('i', i)
    change_all_occurrences('150', str(_150))
    change_all_occurrences('70', str(_70))
    change_all_occurrences('450', str(_450))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+b+', r'\verb+' + b + '+')
    change_all_occurrences(r'\verb+c+', r'\verb+' + c + '+')
    change_all_occurrences(r'\verb+d+', r'\verb+' + d + '+')
    change_all_occurrences(r'\verb+e+', r'\verb+' + e + '+')
        



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
##    global b
##    global c
##    global d
##    global e

    the_list = program.get_global(a)
    b = longest_consecutive_sequence(the_list)
    c = consecutive_sequences(the_list)
    d , dd = filtered_consecutive_sequences(c)
    e = distinct_numbers_in_sequence(d)
    _5 = choice(range(len(e)))

    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')
##    print(the_list)
    answer_1_true = b
    answer_2_true = len(b) - 1
    answer_3_true = dd
    lenght = sum(len(x) for x in c)
    answer_4_true = round(lenght / len(e),2)
    answer_5_true = e[_5]

    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([0.2, -0.2])
    increment4 = choice([0.1, -0.1])
    increment5 = choice([1, -1])

    answer_1_false = chose_for_list(c, b)
    answer_2_false = answer_2_true + increment2
    answer_3_false = answer_3_true + increment3
    answer_4_false = answer_4_true + increment4
    answer_5_false = chose_for_list(e, e[_5])

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    

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

def chose_for_list(nums ,ele):
    shuffle(nums)
    for num in nums:
        if num != ele:
            return num
