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





