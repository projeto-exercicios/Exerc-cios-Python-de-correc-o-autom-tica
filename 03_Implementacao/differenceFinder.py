from IPython.display import display, HTML
import glob
import re
import sys
import os
from random import seed
from random import randint
from string_formater import format_string
from SearchEngine import SearchEngine

searchEngine = SearchEngine()


def idxFinder(arr):
    idxBegin = 0
    idxCode = []
    isCode = False
    idxEnd = 0
    endFound = False

    for indice in range(len(arr)):
        if r'\begin{document}' in arr[indice]:
            idxBegin = indice
        if r'\lstinputlisting{' in arr[indice]:
            idxCode.append(indice)
            isCode = True
        if not endFound:
            if r'\questiom' in arr[indice]:
                idxEnd = indice
                endFound = True
            if r'\end{document}' in arr[indice]:
                idxEnd = indice
                endFound = True
    return idxBegin, idxCode, idxEnd, isCode

def get_name_from_str(string):
    if string[0] == "'" or  string[0] == '"':
        cause = string[0]
        return string.replace(cause, '')
    return string

def find_general_files_to_change():
    sys.path.append('../qom_questions_transformer')
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file

    ldText = load_source_code_from_file('make_random_versions.py')
    arrLdText = ldText.to_string().split('\n')
    found = False
    generalFile = []
    general_files_to_change_list = []
    for line in arrLdText:
        if found :
            if ']' in line:
                found = False
                continue
            else:
                splittedLine = line.split()
                for word in splittedLine:
                    if word.strip():
                        generalFile.append(word)

        if 'general_files_to_change_list = [' in line:
            found = True
            continue
        
    for file in generalFile:
        words = re.split(',',file)
        for word in words:
            if word.strip():
                general_files_to_change_list.append(get_name_from_str(word))      
        

    return general_files_to_change_list

def codeFileName(string) :
    idxStart = 0
    idxEnd = 0
    for i in range(len(string)):
        if string[i] is '{':
            idxStart = i
        if string[i] is '}':
            idxEnd = i   
    return string[idxStart + 1: idxEnd]

def questionHTML(fileName, pdfVersion = False, prefix = 'question/version_1/'):
    scriptExists = searchEngine.fileExists("make_transformations.py")
    if scriptExists != True:
        return "Script make_transformations não encontrado"
    
    if fileName in find_general_files_to_change():
        simulateTex(fileName, prefix)
        file = open(fileName,'r',encoding='utf_8') if prefix == '' else open('simulated_tex.tex','r',encoding='utf_8')
    else:
        file = open(fileName,'r',encoding='utf_8')
    fileSplitted = re.split('\n|\n\n',file.read())
    idxBegin, idxCode, idxEnd, isCode = idxFinder(fileSplitted)
    codeName = []
    for code in idxCode:
        codeName.append(codeFileName(fileSplitted[code]))
    rangeValue = range(idxBegin + 1, idxEnd) if pdfVersion else range(len(fileSplitted))
    idxCode = idxCode if pdfVersion else -1
    final_text = ""
    for idx in rangeValue:
        final_text += '<p>'
        if pdfVersion and idx in idxCode:
            final_text += pythonHTML(codeFileName(fileSplitted[idx]), prefix)
            continue
        final_text += fileSplitted[idx]
        final_text += '</p>'
    if isCode and not pdfVersion:
        for code in codeName:
            final_text += '<h3>' + code + '</h3>'
            final_text += pythonHTML(code, prefix)
    return final_text
        
def create_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def alter_full_program(prefix):
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file

    clear()
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_transformations", os.getcwd() + "\\make_transformations.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    python_module = load_source_code_from_file('full_program.py')
    if os.path.isfile(os.getcwd() + "\\" +  prefix +  'seed.txt'):
        seedFile = get_file_content(os.getcwd() + "\\" +  prefix +  'seed.txt')
        seed(int(seedFile))
    else:
        if os.path.isfile('seed.txt'):
            seedFile = get_file_content('seed.txt')
            seed(int(seedFile))
        else:
            seed_value = randint(1000, 9999)
            create_file('seed.txt', str(seed_value))
            seed(int(seed_value))
    foo.make_transformations()
    create_file('altered_full_program.py', python_module.to_string())
    

def simulateTex(text, prefix):
    '''
        Esta função com a ajuda do "alter_make_transformations" consegue repro
        duzir o código de python com as tags de html necessária para identificar
        onde occoreu uma alteração em comparação com o ficheiro de python
        original
    '''
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear, load_text
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file
    make_transformations_text = alter_make_transformations()
    file1 = open('altered_make_transformations.py','w+')
    file1.writelines(make_transformations_text)
    file1.close()
    
    clear()
    
    import importlib.util
    spec = importlib.util.spec_from_file_location("altered_make_transformations", os.getcwd() + "\\altered_make_transformations.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    seed_value= 0
    text_module = load_text(get_file_content(text))
    
    if os.path.isfile(os.getcwd() + "\\" +  prefix +  'seed.txt'):
        seedFile = get_file_content(os.getcwd() + "\\" +  prefix +  'seed.txt')
        seed_value=int(seedFile)
        seed(int(seedFile))
    else:
        if os.path.isfile('seed.txt'):
            seedFile = get_file_content('seed.txt')
            seed(int(seedFile))
        else:
            seed_value = randint(1000, 9999)
            create_file('seed.txt', str(seed_value))
            seed(int(seed_value))
    foo.make_transformations()
    alter_full_program(prefix)
    simulateTex_values(text_module.to_string(),prefix, seed_value)

def simulateTex_values(text, prefix, seed_value):
    '''
        Esta função com a ajuda do "alter_make_transformations" consegue repro
        duzir o código de python com as tags de html necessária para identificar
        onde occoreu uma alteração em comparação com o ficheiro de python
        original
    '''
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear, load_text
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file
    make_transformations_text = alter_make_transformations_for_code()
    file1 = open('altered_make_transformations_for_code.py','w+')
    file1.writelines(make_transformations_text)
    file1.close()
    
    clear()
    import importlib.util
    spec = importlib.util.spec_from_file_location("altered_make_transformations_for_code", os.getcwd() + "\\altered_make_transformations_for_code.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    

    python_module = load_source_code_from_file('full_program.py')
    text_module = load_text(text)
    seed(int(seed_value))
    foo.make_transformations()
    python_module.execute()
    foo.make_transformations_on_results(python_module)
    final_text = text_module.to_string()
    create_file('simulated_tex.tex', final_text)



def fileExists(prefix, fileName, extension):
    files = glob.glob(prefix+'*.' + extension)
    for file in files:
        if fileName in file:
            return True
    return False
    
def get_file_content(filename):

    with open(filename, "r") as f:
        content = f.read()

    return content

def substitute_in_line(line):
    '''
        Está função adiciona as tags html ao código
    '''
    splittedLine = re.split(',',line)
    if len(splittedLine) == 2:
        oldSplittedLinePart = splittedLine[1]
        splittedLine[1] = ',"<b><font color='"red"'><i>" + ' + oldSplittedLinePart [0:-1]+ '+ "</font></i></b>")'
        return ''.join(splittedLine)
    return ''.join(splittedLine)

def alter_make_transformations_for_code():
    '''
        Esta função percorre o código de "make_transformations.py" adicionando
        as tag html nas funções change_all_occurrences e
        change_token_all_occurrences com a ajuda da função substitute_in_line()
    '''
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file
    pythonCode = load_source_code_from_file('make_transformations.py')
    pyLines = pythonCode.to_string().split('\n')
    newLines = []
    for line in pyLines:
        if "change_all_occurrences(r\'\\verb+" in line:
            result = (substitute_in_line(line))
            newLines.append(result)
        else:
            newLines.append(line)
    text = ''
    for pyLine in newLines:
        if '' == pyLine:
            text +='\n'
        else:
            text += pyLine + '\n'
    return text

def alter_make_transformations():
    '''
        Esta função percorre o código de "make_transformations.py" adicionando
        as tag html nas funções change_all_occurrences e
        change_token_all_occurrences com a ajuda da função substitute_in_line()
    '''
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file
    pythonCode = load_source_code_from_file('make_transformations.py')
    pyLines = pythonCode.to_string().split('\n')
    newLines = []
    for line in pyLines:
        if 'change_all_occurrences' in line:
            result = (substitute_in_line(line))
            newLines.append(result)
        elif 'change_token_all_occurrences' in line:
            result = (substitute_in_line(line))
            newLines.append(result)
        else:
            newLines.append(line)
    text = ''
    for pyLine in newLines:
        if '' == pyLine:
            text +='\n'
        else:
            text += pyLine + '\n'
    return text

def markDifferences(pythonCode, prefix):
    '''
        Esta função com a ajuda do "alter_make_transformations" consegue repro
        duzir o código de python com as tags de html necessária para identificar
        onde occoreu uma alteração em comparação com o ficheiro de python
        original
    '''
    
    sys.path.append('../qom_questions_transformer')
    from text_transformer.tt_text_transformer_interface import clear
    from python_transformer.pt_util.pt_util_file import load_source_code_from_file
    make_transformations_text = alter_make_transformations()
    file1 = open('altered_make_transformations.py','w+')
    file1.writelines(make_transformations_text)
    file1.close()
    import os
    
    clear()
    import importlib.util
    spec = importlib.util.spec_from_file_location("altered_make_transformations", os.getcwd() + "\\altered_make_transformations.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    python_module = load_source_code_from_file(pythonCode)
    if os.path.isfile(os.getcwd() + "\\" +  prefix +  'seed.txt'):
        seedFile = get_file_content(os.getcwd() + "\\" +  prefix +  'seed.txt')
        seed_value=int(seedFile)
        seed(int(seedFile))
    else:
        if os.path.isfile('seed.txt'):
            seedFile = get_file_content('seed.txt')
            seed(int(seedFile))
        else:
            seed_value = randint(1000, 9999)
            create_file('seed.txt', str(seed_value))
            seed(int(seed_value))
    
    
    foo.make_transformations()

    return python_module.to_string()


def pythonHTML(fileName, prefix = 'question/version_1/'):
    '''
        Esta função pode mostrar em HTML 2 versões do código, original, caso o
        prefix esteja vazio e alterada caso o prefix indique o path da versão
        da questão. Com a ajuda da função markDifferences que simula o código
        alterado é reproduzido o código após as alterações efetuadas no ficheiro
        "make_transformations.py"
    '''

    scriptExists = searchEngine.fileExists("make_transformations.py")
    if scriptExists != True:
        return "Script make_transformations não encontrado"
    
    originalFile = open(fileName, 'r')
   
    text = "<p>"
    pyCodeLines = originalFile.read().split('\n') if prefix == '' else markDifferences(fileName, prefix).split('\n')

    for pyCodeLine in pyCodeLines:
        
        pyCodeSplitedLine = pyCodeLine.split(' ')

        for splitedSection in pyCodeSplitedLine:

            text += '&ensp;' if splitedSection == '' else splitedSection + ' '

        text += '</br>'

    text += '</p>'

    return text


