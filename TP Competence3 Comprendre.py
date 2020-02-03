"""

Compétence 3 : Comprendre

"""


"""

Prerequis : Prendre une feuille et un stylo. Vous allez lire les codes suivants et expliquer comment ils fonctionnent.

Par exemple que fait telle fonction ? Comment elle agit dans telle boucle etc...

"""


"""

Exercice 1 : Sur des exemples simples (déconnecté du réel)

Expliquer comment le script fonctionne et ce que l'on veut calculer.


"""


# Script 1 :

def f(i):
    j = (i+1)**2
    return j

S = 0
for i in range(1000):
    S = S  + f(i)

"""

Ce script calcule la somme de 1 à 1000 des (i+1)**2
Au final on a :
S = 1**2 + 2**2 + 3**2 + ... + 1000**2


"""






# Script 2 :

def Cube(n):
    m = n**3
    return m

def Inverse(x):
    y = 1/x
    return y

def UnSurXauCube(n):
    X = list(range(1,n))
    Y = []
    for x in X:
        y = Inverse(Cube(x))
        Y.append(y)
    return (X,Y)

"""


"""





# Script 3

def Transm(lettre):
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if type(lettre)  == str and len(lettre) == 1:
        lettreminuscule = lettre.lower()
        code = Alphabet.index(lettreminuscule)
    else:
        code = -1
    return code

def DeformCode(code,coeff):
    if code == -1:
        NouveauCode = -1
    else:
        NouveauCode = code + coeff
        # On ramène le nouveau code dans [0,25] en faisant une division euclidienne par 26
        NouveauCode = NouveauCode % 26
    return NouveauCode

def CodeVersLettre(code):
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    NouvelleLettre = Alphabet[code]
    return NouvelleLettre


def TransformerMot(mot,coeff):
    NouveauMot = ""
    for lettre in mot:
        code = Transm(lettre)
        NouvCode = DeformCode(code,coeff)
        NouvLettre = CodeVersLettre(NouvCode)
        NouveauMot = NouveauMot + NouvLettre
    return NouveauMot

def TransformerMotAlea(mot):
    import random
    u = random.randint(1,1000)
    NouveauMot = TransformerMot(mot,u)
    return NouveauMot


# Script 4 :

import random

ListeNombreAuHasard = []

for i in range(1000):
    u = random.randint(-10000,10000)
    ListeNombreAuHasard.append(u)

Compteur = 0
for nombre in ListeNombreAuHasard:
    if nombre %2 == 0:  # Si nombre est pair
        Compteur = Compteur + 1




"""

Exercice 2 :

Cette fois nous allons prendre des vrais bouts de code, et vous allez expliquer ce qu'ils font et comment ils le font.


"""

# Script 1

import os
from PIL import Image

path = os.getcwd()
path = path + "//Google Drive//Python//Python et Windows//Contenu Dossier//Darwin's Game" # Dossier de travail avec plusieurs sous dossiers
os.chdir(path)
path = os.getcwd()
print(os.getcwd())


os.mkdir("Resize")
os.chdir("Resize")
pathResize = os.getcwd()

os.chdir("..")


for SousDossier in os.listdir():
    if SousDossier != "Resize":
        os.chdir(SousDossier)
        pathSousDossier = os.getcwd()
        print("path Sous Dossier Ok")
        for elt in os.listdir():
            im = Image.open(elt)
            os.chdir(pathResize)
            newname = SousDossier + " " + elt
            im.save(newname,quality = 50, optimize = True)
            os.chdir(pathSousDossier)
        os.chdir(path)

# Script 2

def doss(D,path):
    os.chdir(D)
    print(os.getcwd())
    u = rd.randint(1,2)
    print(u)
    if u == 1:
        os.mkdir(str(u))
        print("Creation sous dossier")
        doss(str(u),path)
    else :
        os.chdir(path)
        print("sortie")
        print(os.getcwd())



def WorkingDossier():
    os.chdir("C://Users//Utilisateur//Google Drive//Python//Python et Windows//Creation Dossier")  # Changer l'adresse par une adresse sur l'ordinateur qui le lance
    print(os.getcwd())
    return os.getcwd()

def Lancer(path):
    print(os.getcwd())
    for i in range(1,10):
        print(i)
        os.mkdir(str(i))
        doss(str(i),path)


# Script 3

import os
import codecs
def dossier():
    os.chdir("Google Drive//Python//ApplicationProf//Compilateur de Cours")
dossier()
os.chdir("Test")

with codecs.open("NC1.tex","r", encoding = 'utf-8') as file:
    d = file.read()

with codecs.open("test.tex","w",encoding = 'utf-8') as file:
    file.write(d)



"""

Exercice 3 :

Voilà un long script avec des classes.

Expliquer la classe Eleve, ses attributs et sa méthode. Comment un Objet Eleve fonctionne ?

Expliquer la classe Classe, ses attributs, ses méthodes.

Expliquer la classe GroupeDeClasse, ses attributs et ses méthodes


"""





class Eleve:
    def __init__(self):
        self.nom =  "Moi"
        self.genre  = "Adolescent"
        self.voeux = []

    def Voeux(self,L):
        if L[0] == "H":
            self.genre = "Homme"
        else :
            self.genre = "Femme"
        if L[1] == "1" or L[1] == 1:
            self.voeux.append("HLP")
        if L[2] == "1" or L[2] == 1:
            self.voeux.append("Géopol")
        if L[3] == "1" or L[3] == 1:
            self.voeux.append("LCE")
        if L[4] == "1" or L[4] == 1:
            self.voeux.append("SES")
        if L[5] == "1" or L[5] == 1:
            self.voeux.append("Math")
        if L[6] == "1" or L[6] == 1:
            self.voeux.append("Phy")
        if L[7] == "1" or L[7] == 1:
            self.voeux.append("SVT")
        if L[8] == "1" or L[8] == 1:
            self.voeux.append("SI")
        if L[9] == "1" or L[9] == 1:
            self.voeux.append("NSI")
        self.voeux.sort()


class Classe:
    def __init__(self):
        self.Homme = 0
        self.Femme = 0
        self.N = 0
        self.DicoSpe = {"HLP":0,"Géopol":0,"LCE":0,"SES":0,"Math":0,"Phy":0,"SVT":0,"SI":0,"NSI":0}
        self.DispersionSL = self.DicoSpe["HLP"] + self.DicoSpe["Géopol"] + self.DicoSpe["LCE"] + self.DicoSpe["SES"] - self.DicoSpe["Math"] - self.DicoSpe["Phy"] -self.DicoSpe["SVT"] - self.DicoSpe["SI"] - self.DicoSpe["NSI"]
        self.DicoEleve = {}
    def update(self):
        self.Homme = 0
        self.Femme = 0
        self.N = 0
        self.DicoSpe = {"HLP":0,"Géopol":0,"LCE":0,"SES":0,"Math":0,"Phy":0,"SVT":0,"SI":0,"NSI":0}
        for eleve in self.DicoEleve:
            self.Homme = self.Homme + 1*(self.DicoEleve[eleve].genre == "Homme")
            self.Femme = self.Femme + 1*(self.DicoEleve[eleve].genre == "Femme")
            self.N = self.N + 1
            for matiere in self.DicoSpe:
                self.DicoSpe[matiere] += self.DicoEleve[eleve].voeux.count(matiere)
        self.DispersionSL = self.DicoSpe["HLP"] + self.DicoSpe["Géopol"] + self.DicoSpe["LCE"] + self.DicoSpe["SES"] - self.DicoSpe["Math"] - self.DicoSpe["Phy"] -self.DicoSpe["SVT"] - self.DicoSpe["SI"] - self.DicoSpe["NSI"]

    def AjoutEleve(self,Eleve):
        self.DicoEleve[Eleve.nom] = Eleve


class GroupeDeClasses:

    def __init__(self,DicoSeconde):
        self.DicoSeconde = DicoSeconde
        self.DicoSave = DicoSave
        self.DicoClasse = {}
        self.Energie = 1000000
        self.n = 6
        self.EffectifTotal = 0

    def FaireClasseGene(self):
        self.DicoClasse.clear()
        for i in range(1,self.n+1):
            nom = "Première Géné " + str(i)
            #print(nom)
            self.DicoClasse[nom] = Classe()
        for eleve in DicoSeconde:
            u = rd.randint(1,self.n)
            #print(u)
            nom = "1G" + str(u)
            #print(nom)
            self.DicoClasse[nom].AjoutEleve(DicoSeconde[eleve])
        for classe in self.DicoClasse:
            self.DicoClasse[classe].update()



    def DeplacerEleve(self,nomClasse,p):
        L = []
        ListeClasse = list(self.DicoClasse.keys())
        for nomEleve in self.DicoClasse[nomClasse].DicoEleve:
            if rd.random() < p:
                L.append(nomEleve)
                tempEleve = self.DicoClasse[nomClasse].DicoEleve[nomEleve]
                u = rd.randint(0,len(ListeClasse)-1)
                #print(nomEleve)
                #print(u+1)
                self.DicoClasse[ListeClasse[u]].AjoutEleve(tempEleve)
        Classe = self.DicoClasse[nomClasse]
        for l in L:
            del Classe.DicoEleve[l]

    def Optim(self,ite):
        m = 0
        #print(m)
        ListeOptim.clear()
        Backup = deepcopy(self)
        EnCours = deepcopy(self)
        EnergieRef = Backup.Energie
        ListeClasse = list(EnCours.DicoClasse.keys())
        print(EnergieRef)
        while m<ite and self.Energie > 30:
            m +=1
            pp=0.3
            for classe in ListeClasse:
                if rd.random()<pp:
                    p = 0.3
                    EnCours.DeplacerEleve(classe,p)
            for classe in ListeClasse:
                EnCours.DicoClasse[classe].update()
            NRJ = EnCours.CalculEnergie()
            ListeOptim.append(NRJ)
            if (m%100 == 0): print(m)
            #print("A m = {1} La Nouvelle Energie est {0}".format(NRJ,m))
            if NRJ < EnergieRef and EnCours.EffectifTotal == Backup.EffectifTotal:
                Backup = deepcopy(EnCours)
                EnergieRef = Backup.Energie
                FaireClasseur(EnCours)
                print(EnergieRef)
            else:
                EnCours = deepcopy(Backup)
        print(EnergieRef)
        self.DicoClasse = EnCours.DicoClasse
        self.Energie = EnCours.Energie


    def CalculEnergie(self):
        NRJ = 0
        L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for classe in self.DicoClasse:
            for v in self.DicoClasse[classe].DicoSpe.values():
                if v!=0:
                    L[v] += 1
        for i in range(0,len(L)):
            NRJ += 10*L[i]*exp(-i/5) + 10000*(L[i]>30)
        Effectif = []
        DiffHF = []
        DiffSL = []
        for classe in self.DicoClasse:
            Effectif.append(self.DicoClasse[classe].N)
            DiffHF.append((self.DicoClasse[classe].Homme - self.DicoClasse[classe].Femme))
            DiffSL.append((self.DicoClasse[classe].DispersionSL))
        self.Energie = 3*NRJ + 10*std(Effectif) + Std0(DiffHF) + Std0(DiffSL)
        self.EffectifTotal = sum(Effectif)
        return self.Energie

