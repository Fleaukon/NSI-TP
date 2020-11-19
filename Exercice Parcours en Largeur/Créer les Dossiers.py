import random
import os
root = os.getcwd() #Naviguer avant de lancer le programme sinon ça va envahir Home
File = []
Compteur = 0


def MkDos(p,path): #path chemin dossier, p proba de créer un dossier
    global File,Compteur
    os.chdir(path)
    u = 0
    while u<p:
        os.mkdir(str(Compteur))
        os.chdir(str(Compteur))
        temp_path = os.getcwd()
        File.append(temp_path)
        os.chdir("..")
        u = random.random()
        Compteur +=1
    os.chdir(root)


def Boucle(p,t): #p proba initiale, t taux de décroissance
    global File,Compteur
    MkDos(p,root)
    while len(File)>0:
        pathDos = File.pop(0)
        p = max(0, p-t)
        print(Compteur)
        print(p)
        MkDos(p,pathDos)