import random as rd



# Exercice 1


class Ville:
    def __init__(self):
        self.index = -1
        self.valeur = rd.randint(1,10000)
    def Roll(self):
        self.valeur = rd.randint(1,10000)


ListeVilles = []
for i in range(1000):
    TempVille = Ville()
    ListesVilles.append(TempVille)


"""

1°) Quelle est la nature de ListeVilles
2°) Quelle est la nature de :
        Ville
        __init__
        valeur
        Roll
3°) Combien il y a-t-il d'éléments dans ListesVilles
4°) Classer ListeVilles par ordre de valeur croissant en utilisant 3 algorithmes différents


"""



