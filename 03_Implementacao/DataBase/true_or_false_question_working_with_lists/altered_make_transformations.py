
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
add_changeable('135')    # seed
add_changeable('a')      # the list with numbers
add_changeable('b')      # the list with strings
add_changeable('d')      # 2nd list with numbers
add_changeable('l')      # string to be generated
add_changeable('k')      # loop variable
add_changeable('i')
add_changeable('3')      # multiplier
add_changeable('10')     # the list length
add_changeable('20')     # second for range
add_changeable('50')     # max int number


# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+b+')
add_changeable(r'\verb+ab+')
add_changeable(r'\verb+d+')
add_changeable(r'\verb+_33+')

#functions to be insered in questions
add_changeable(r'\verb+func1+')
add_changeable(r'\verb+func2+')
add_changeable(r'\verb+func3+')
add_changeable(r'\verb+func4+')
add_changeable(r'\verb+func5+')



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
d  = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None
decision = None
_10 = None
_20 = None
_33 = None
_func5 = None





def make_transformations():
    ''
    global a
    global d
    global _1
    global _2
    global _3
    global _4
    global _5
    global _10
    global _20
    global _33
    global decision
    global _func5
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, b, d, l, k, i] = sample(string.ascii_lowercase, 6)
    _10 = randint(18000, 20000)
    _50 = randint(50, 150)
    _20 = _10 * randint(2, 4)
    _33 = randint(2, 5)
    
    change_all_occurrences('135',"<b><font color=red><i>" +  _135+ "</font></i></b>")
    change_token_all_occurrences('a',"<b><font color=red><i>" +  a+ "</font></i></b>")
    change_token_all_occurrences('b',"<b><font color=red><i>" +  b+ "</font></i></b>")
    change_token_all_occurrences('d',"<b><font color=red><i>" +  d+ "</font></i></b>")
    change_token_all_occurrences('l',"<b><font color=red><i>" +  l+ "</font></i></b>")
    change_token_all_occurrences('k',"<b><font color=red><i>" +  k+ "</font></i></b>")
    change_token_all_occurrences('i',"<b><font color=red><i>" +  i+ "</font></i></b>")
    change_all_occurrences('10',"<b><font color=red><i>" +  str(_10)+ "</font></i></b>")
    change_all_occurrences('50',"<b><font color=red><i>" +  str(_50)+ "</font></i></b>")
    change_all_occurrences('20',"<b><font color=red><i>" +  str(_20)+ "</font></i></b>")
    change_all_occurrences('3',"<b><font color=red><i>" +  str(_33)+ "</font></i></b>")

    func1 = choice(('[::-1].sort()', '[-1::].sort()', '[:-1:].sort()'))
    func2 = 'sort(reverse=True)'
    func3 = ['sort(key=len)', 'sort()',
             'sort(key=len, reverse=True)', 'sort(reverse=True)']
    ab = [b, a]
    decision = choice((0, 1, 2, 3))
    # answers
    change_all_occurrences(r'\verb+_33+',"<b><font color=red><i>" +  r'\verb+' + str(_33) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+a+',"<b><font color=red><i>" +  r'\verb+' + a + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+b+',"<b><font color=red><i>" +  r'\verb+' + b + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+ab+',"<b><font color=red><i>" +  r'\verb+' + ab[decision % 2] + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+d+',"<b><font color=red><i>" +  r'\verb+' + d + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+func1+',"<b><font color=red><i>" +  r'\verb+' + func1 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+func2+',"<b><font color=red><i>" +  r'\verb+' + func2 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+func3+',"<b><font color=red><i>" +  r'\verb+' + func3[decision] + '+'+ "</font></i></b>")
    # indexes with no repetitions
    _5 = choice((2, 3, 4, 5))
    _func5 = choice(('primeiros', 'ultimos'))

    [_3] = sample(range(_50), 1)
    change_all_occurrences(r'\verb+2+',"<b><font color=red><i>" +  r'\verb+' + _func5[decision] + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3+',"<b><font color=red><i>" +  r'\verb+' + str(_3) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+5+',"<b><font color=red><i>" +  r'\verb+' + str(_5) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+func5+',"<b><font color=red><i>" +  r'\verb+' + _func5 + '+'+ "</font></i></b>")
    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global d
    global _1
    global _2
    global _3
    global _4
    global _5
    global decision
    global _10
    global _20
    global _33
    global _func5

    
    form = ['crescente', 'decrescente']
    base = ['com base no tamanho da string', 'com base no numero']
    answer = form[0] if decision < 3 else form[1]
    answer += ' '
    answer += base[decision%2]
    the_list = program.get_global(d)
    #print(the_list)
    
    answer_2_true = answer
    times = _33
    for i in range(1, int(_20 / _10)):
        times *= _33
    answer_3_true = the_list[_3]
    answer_4_true = times
    answer_5_true = a + '[:' + str(_5) + ':]'  if _func5 == 'primeiros' else a + '[-' + str(_5) +'::]'

    # true answers
  
    change_all_occurrences(r'\verb+22+',"<b><font color=red><i>" +  str(answer_2_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+33+',"<b><font color=red><i>" +  str(answer_3_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+44+',"<b><font color=red><i>" +  str(answer_4_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+55+',"<b><font color=red><i>" +  str(answer_5_true)+ "</font></i></b>")

    # wrong answers
    
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer = form[1] if decision < 3 else form[0]
    answer += ' '
    answer += base[decision%2]

    
    answer_2_false = answer
    answer_3_false = the_list[_3] + increment3
    answer_4_false = answer_4_true + increment4
    answer_5_false = a + wrong_5_awnser(_func5, _5)
    
    change_all_occurrences(r'\verb+222+',"<b><font color=red><i>" +  str(answer_2_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+333+',"<b><font color=red><i>" +  str(answer_3_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+444+',"<b><font color=red><i>" +  str(answer_4_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+555+',"<b><font color=red><i>" +  str(answer_5_false)+ "</font></i></b>")


def wrong_5_awnser(string, num):
    num = str(num)
    if string == 'primeiros':
        return choice(('['+ num + ']', '[' + num +'::]', '[::' + num +']'))
    return choice(('[-'+ num + ']', '[:-' + num +':]', '[::-' + num +']'))

