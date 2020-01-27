"""

Compétence 2 : Executer

"""


"""

Prerequis : Prendre une feuille et un stylo. Vous allez lancer les codes suivants, avoir des erreurs et apprendre à reconnaitre les différents types d'erreur

"""




"""

Exercice 1 :

Pour les Scripts suivants, vous allez executer les codes suivants et écrire sur une feuille pour chaque script la quantité demandée.

"""

# Script 1 : Calculer a

a = 2
b = 4
a = b**a + a**b

# Script 2 : Ecrire le dernier élément de L

L = []
for i in range(9):
    L.append(i**2)

# Script 3 : Donner f(3)

def f(n):
    L = []
    for i in range(n):
        L.append(i**2)
    s = sum(L)
    return s

# Script 4 : A priori que devrait donner f(3) et calculer f(3)

n = 5
def f(n):
    return n + 1


"""

Exercice 2 :

Dans les scripts suivants, vous allez avoir une NameError.
"NameError : name '...' is not defined". Trouver d'où vient l'erreur et pourquoi on a cette erreur ? et corriger l'erreur.
Ecrire le script corrigé sur feuille.


"""


# Script 1 : alpha est un nombre

beta = alpha + 1

# Script 2 : String est un string

String.upper()

# Script 3 : LListe est une liste

for i in range(9):
    LListe.append(i)

# Script 4 : Dico est un Dictionnaire

Dico["AA"] = "aa"

# Script 5 : gamma est un nombre

def f(gamma):
    delta = gamma + 1
    return delta

print(gamma)


# Script 6 : delta est un nombre

def f(gamma):
    delta = gamma + 1
    return delta

print(delta)


"""

Exercice 3 :

Dans cet exercice on va obtenir des TypeError. Vous obtenez cette erreur lorsque vous utilisez une opération en deux variables de types différents.

Ecrivez sur une feuille les scripts corrigés.


"""




# Script 1 : On veut concatener écrire "Script 1"

str = "Script "
a = 1
Script1 = str + a