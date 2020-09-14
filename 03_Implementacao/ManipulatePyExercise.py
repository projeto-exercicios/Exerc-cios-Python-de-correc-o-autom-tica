# -*- coding: utf-8 -*-

#imports
from pdf2image import convert_from_path
from SearchEngine import SearchEngine
from differenceFinder import *

class ManipulatePyExercise:
    
    def __init__(self):
        self.theFolderName = 'true_or_false_question'
        #self.foldersNames = ['qom_questions_transformer','true_or_false_question']
        self.filesNames = ['true_or_false_question.tex','program.py','util_make_random_versions.py']
        self.questionpdf = 'true_or_false_question.pdf'
        self.questionpng = 'true_or_false_question.png'
        self.linesNamepdf = ['answer_','_true.pdf','_false.pdf']
        self.linesNamepng = ['answer_','_true.png','_false.png']
        self.questionFolder = 'question'
        self.versionFolder = 'version_'
        self.directory = ''
        self.filePath = ''
        self.searchEngine = SearchEngine()
        
        #diference finder
        self.pyFilesNames = ['full_program.py', 'answers_program.py']
        self.pyProgram = 'program.py'
        self.pyPrograms = ['program','.py']
        self.texFilesNames = ['true_or_false_question.tex']
        self.texAnswerNames = ['answer_', '_false.tex', '_true.tex']
        
        self.folders = []
        self.files = []
        
    def seeIfExercise(self, path):
        #verificar se a pasta tem os ficheiros necessários para um exercício
        self.searchEngine.setDirectory(path) #colocar na diretoria
        files = self.searchEngine.getAllFiles() #ir buscar ficheiros
        if self.isFilesExercise(files): #verificar ficheiros
            return True
        return False
    
    def isFolderExercise(self, folders):#not in use
        counter = 0
        for folder in folders: #verificar se existe um folder em que o nome se inicia por 'true_or_false_question'
            for name in self.foldersNames:
                if folder[:len(name)] == name:
                    counter += 1
                    if name == self.theFolderName:#se o folder do exercicio existir
                        self.filePath = folder #guardar nova diretoria para ser usada
        if counter == len(self.foldersNames): #se todos os folders estiverem na pasta é uma pasta exercício
            return True
        return False
    
    def isFilesExercise(self, files):
        #verificar se o folder tem os ficheiros necessários ao exercício
        counter = 0
        for file in files:
            for name in self.filesNames:
                if file == name:
                    counter += 1
        if counter == len(self.filesNames):
            return True
        return False
    
    def getExerciseImg(self):
        #verificar se o pdf existe
        if self.searchEngine.fileExists(self.questionpdf):
            #verificar se a imagem já existe
            if not self.searchEngine.fileExists(self.questionpng):
                pages = convert_from_path(self.questionpdf, 500)
                for page in pages:
                    page.save(self.questionpng, 'PNG')
            file = open(self.questionpng, 'rb')
            img = file.read()
            return img
        else:
            print('Não foi possivél encontrar o pdf do enunciado')
            return
    
    def getExerciseLinesImg(self):
        #retorna as magens png das alineas
        done = False
        lines = []
        i = 0
        while done == False:
            i = i + 1
            name_true = self.linesNamepdf[0]+str(i)+self.linesNamepdf[1]
            name_false = self.linesNamepdf[0]+str(i)+self.linesNamepdf[2]
            #verificar se o ficheiro pdf existe
            if self.searchEngine.fileExists(name_true) and self.searchEngine.fileExists(name_false):
                #se existir verificar de o png existe
                new_pages1 = self.linesNamepng[0]+str(i)+self.linesNamepng[1]
                new_pages2 = self.linesNamepng[0]+str(i)+self.linesNamepng[2]
                #veriricar se os png já existem, se não criar
                if not self.searchEngine.fileExists(new_pages1) :
                    #se não existir vamos criar
                    pages1 = convert_from_path(name_true, 500)
                    pages2 = convert_from_path(name_false, 500)
                    #guardar png
                    for page in pages1:
                        page.save(new_pages1, 'PNG')
                    for page in pages2:
                        page.save(new_pages2, 'PNG')
                #ir buscar png e guardar
                file_true = open(new_pages1, 'rb')
                img1 = file_true.read()
                file_false = open(new_pages2, 'rb')
                img2 = file_false.read()
                
                lines.append(img1)
                lines.append(img2)
            #se não existe terminar
            else :
                if i == 1:
                    print('Não foi possivél encontrar os pdfs das alineas')
                    return
                done = True
        return lines
    
    def getExerciseName(self):
        return self.searchEngine.getLastFolder()
    
    def getPyFilesNames(self):
        files = []
        #procurar programs.py
        if self.searchEngine.fileExists(self.pyProgram):
            files.append(self.pyProgram)
        i = 2
        while self.searchEngine.fileExists(self.pyPrograms[0]+str(i)+self.pyPrograms[1]):
            files.append(self.pyPrograms[0]+str(i)+self.pyPrograms[1])
            i = i+1
        for file in self.pyFilesNames:
            if self.searchEngine.fileExists(file):
                files.append(file)
        return files
    
    def getTexFilesNames(self):
        files = []
        for file in self.texFilesNames:
            if self.searchEngine.fileExists(file):
                files.append(file)
        i = 1
        while self.searchEngine.fileExists(self.texAnswerNames[0]+str(i)+self.texAnswerNames[1]):
            files.append(self.texAnswerNames[0]+str(i)+self.texAnswerNames[1])
            files.append(self.texAnswerNames[0]+str(i)+self.texAnswerNames[2])
            i = i+1
        return files
    
    def seeIfHasVersions(self):
        #verificar se o exercicio tem a pasta question
        if self.searchEngine.folderExists(self.questionFolder):
            self.searchEngine.goFoward(self.questionFolder)
            #verificar se existe pelo menos um folder de versões
            if self.searchEngine.folderExists(self.versionFolder+'1'):
                #voltar a traz e retornar true
                self.searchEngine.goBack()
                return True
        return False
            
    def getVersionsNames(self):
        i = 1
        names = []
        self.searchEngine.goFoward(self.questionFolder)
        while self.searchEngine.folderExists(self.versionFolder+str(i)):
            names.append(self.versionFolder+str(i))
            i = i+1
        self.searchEngine.goBack()
        return names
            
    def getVersionImgs(self, version_number):
        imgs = []
        self.searchEngine.goFoward(self.questionFolder)
        self.searchEngine.goFoward(self.versionFolder+version_number)
        #ir buscar enunciado
        imgs.append(self.getExerciseImg())
        #ir buscar alineas
        imgs.append(self.getExerciseLinesImg())
        self.searchEngine.goBack()
        self.searchEngine.goBack()
        return imgs
    
    def getPyFileDifferences(self, fileName):
        return pythonHTML(fileName)
    
    def getTexFileDifference(self, fileName):
        return questionHTML(fileName)
        
    def changeNumberOfVersions(self, number):
        with open("make_random_versions.py", "r") as f:
            lines = f.readlines()
        with open("make_random_versions.py", "w") as f:
            for line in lines:
                if not("number_of_versions = " in line.strip("\n")):
                    f.write(line)
                else:
                    f.write('number_of_versions = ' + str(number)+ '\n')
    
    def generateVersions(self):
        try:
            self.searchEngine.runFile('make_random_versions.py')
            self.searchEngine.runFile('make_pdfs.py')
        except:
            print('Ocorreu uma excepção na geração de versões')

        
#a = ManipulatePyExercise()
#b = a.seeIfExercise('C:\\6SEM\\Projeto\\Projeto\\DataBase\\true_or_false_question_char_counter')
# h = a.getExerciseImg()
# print(len(h))
#j = a.getExerciseLinesImg()
#print(len(j))
#print(a.k())
#print(a.getExerciseName())
#print(a.getPyFileDifferences('program.py'))
#a.changeNumberOfVersions(2)
#a.generateVersions()
#a.seeIfHasVersions()
#a.getVersionsNames()
#print(len(a.getVersionImgs('1')))

