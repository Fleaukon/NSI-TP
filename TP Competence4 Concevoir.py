"""

Compétence 4 : Concevoir

"""



"""

Prérequis : Même si ici la feuille de papier et le stylo n'est pas obligatoire. Il est très fortement recommandé d'avoir un brouillon

"""


"""
Exercice 1 : Faire des scripts, algorithmes réalisant les objectifs suivants
"""


# Objectif 1 : Calculer votre age en 2060
age = 30
Année = 2020
TempsRestant = 2060 - Année
AgeEn2060 = age + TempsRestant




# Objectif 2 : Pour un nombre donné calculer le carré du triple du nombre

n = 13
CarréDuTriple = (3*n)**2





# Objectif 3 :On lance deux dés à six faces parfaitement équilibrés et on additionne les deux résultats obtenus. Écrire un programme qui modélise les lancers de ces deuxdés et qui donne le nombre n de lancers qu’il a fallu pour obtenir la somme 12. On veut voir le résultat des 2 dés à chaque tour.

import random

s = 0
n = 0

while s != 12:
    u = random.randint(1,6)
    v = random.randint(1,6)
    s = u+v
    n = n+1

#    n est le nombre de lancers




# Objectif 4 : Écrire un programme qui demande un entier positif ou nul et qui donne ensuite son nombre de chiffre.

def chiffre(n):
    strN = str(n)
    chiffres = len(strN)
    return chiffres



# Objectif 5 : Un joueur doit trouver un nombre mystère choisi de manière aléatoire par l’ordinateur. À chaque tour, le joueur propose un nombre et l’ordinateur indique si le nombre mystère est plus petit ou plus grand que le nombre proposé jusqu’à ce que le joueur trouve le nombre mystère.Écrire un programme permettant de jouer à ce jeu avec un nombre à chercher compris entre zéro et 100.  Compléter ce programme afin de faire afficher le nombre d’essais effectués.

import random

N = random.randint(0,100)
guess = -1

while guess != N:
    strguess = input("Tente un nombre \n")
    guess = int(strguess)
    if guess == N:
        print("gagné")
    elif guess > N:
        print("Trop Grand")
    else :
        print("Trop Petit")




# Objectif 6 : Faites une fonction qui prends en entrée 3 entiers n,a,b et qui donne en sortie une liste de n nombres aléatoires compris entre a et b.

import random

def Liste(n,a,b):
    L = []
    for i in range(n):
        u = random.randint(a,b)
        L.append(u)
    return L


# Objectif 7 : Faire une fonction qui prend en entrée une liste et qui donne en sortie un dictionnaire avec comme clé les items de la liste et comme valeur le nombre de fois où cette clé est dans la liste. Exemple ci dessous

def Compter(Liste):
    dico = {}
    LL = Liste.sort()
    for item in Liste:
        if item in dico:
            dico[item] = dico[item]+1
        else:
            dico[item] = 1
    return dico



