"""

Compétence 2 : Executer

"""


"""

Prerequis : Prendre une feuille et un stylo. Vous allez lancer les codes suivants, avoir des erreurs et apprendre à reconnaitre les différents types d'erreur. A chaque fois que vous avez une erreur vous devez la corriger pour le que l'objectif soit atteint.

"""




"""

Exercice 1 :

Pour les Scripts suivants, vous allez executer les codes suivants et écrire sur une feuille pour chaque script la quantité demandée.

"""

# Script 1 : Calculer a

a = 2
b = 4
a = b**a + a**b
"""
a = 32
"""

# Script 2 : Ecrire le dernier élément de L

L = []
for i in range(9):
    L.append(i**2)
"""
La réponse est 64
"""


# Script 3 : Donner f(3)

def f(n):
    L = []
    for i in range(n):
        L.append(i**2)
    s = sum(L)
    return s
"""
f(3) = 5
"""

# Script 4 : A priori que devrait donner f(3) et calculer f(3)

n = 5
def f(n):
    return n + 1
"""
f(3) = 4
"""


"""

Exercice 2 :

Dans les scripts suivants, vous allez avoir une NameError.
"NameError : name '...' is not defined". Trouver d'où vient l'erreur et pourquoi on a cette erreur ? et corriger l'erreur.
Ecrire le script corrigé sur feuille.


"""


# Script 1 : alpha est un nombre

#alpha  = 1
beta = alpha + 1

# Script 2 : String est un string

#String  = "blaBla"
String.upper()

# Script 3 : LListe est une liste

#LListe  = []
for i in range(9):
    LListe.append(i)

# Script 4 : Dico est un Dictionnaire

#Dico = {}
Dico["AA"] = "aa"

# Script 5 : gamma est un nombre

def f(gamma):
    delta = gamma + 1
    return delta
#gamma = 3
print(gamma)


# Script 6 : delta est un nombre

def f(gamma):
    delta = gamma + 1
    return delta

#delta = f(3)
print(delta)


"""

Exercice 3 :

Dans cet exercice on va obtenir des TypeError. Vous obtenez cette erreur lorsque vous utilisez une opération en deux variables de types différents.

Ecrivez sur une feuille les scripts corrigés.


"""




# Script 1 : On veut concatener écrire "Script 1"

str = "Script "
a = 1
#a = str(a)
Script1 = str + a


# Script 2 : On veut calculer 1.2 au carré

u = 1,2
#u = 1.2
v = u**2

# Script 3 : On veut faire un string "Maison Jolie"

L = []
#Str = ""
for lettre in "Maison":
    L.append(lettre)
    # Str = Str + lettre
Str = L + "Jolie" # Cette ligne est mauvaise