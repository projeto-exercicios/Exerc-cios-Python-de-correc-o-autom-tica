# -*- coding: utf-8 -*-
import os

class SearchEngine:
    
    def __init__(self):
        self.directory = os.getcwd()
        self.folders = os.listdir()
    
    def __repr__(self):
        return 'directory: '+ str(self.directory) + ', folders: '+ str(self.folders)
    
    def setDirectory(self, directory):
        os.chdir(directory)
        self.refresh()
        
    def getDirectory(self):
        return self.directory
    
    def getFileDirectory(self):
        return os.path.dirname(__file__)
    
    def getFolders(self):
        onlyFolders = []
        for folder in self.folders:
            if os.path.isdir(folder):
                onlyFolders.append(folder)
        return onlyFolders
    
    def getAllFiles(self):
        return self.folders
    
    def goBack(self):
        os.chdir(os.path.dirname("../"))
        self.refresh()
    
    def goFoward(self, folder):
        os.chdir(self.directory + "\\" + folder)
        self.refresh()
    
    def refresh(self):
        self.directory = os.getcwd()
        self.folders = os.listdir()
    
    def fileExists(self, name):
        return os.path.isfile(name)
    
    def folderExists(self, name):
        return os.path.isdir(name)
    
    def getLastFolder(self):
        return os.path.basename(os.path.normpath(self.directory))
    
    def runFile(self, file):
        os.system(file)
        #os.system('exit')