"""

Compétence 1 : Lire le code

"""


"""

Prerequis : Prendre une feuille et un stylo. Vous allez lire du code et écrire sur une feuille les réponses aux exercices suivants.

"""






"""

Exercice 1 :


Pour les scripts suivants donner le nom des variables et le type des variable

"""


# Script 1

a = 1
a = a + 1
b = a
L = [a,b,b+1]


# Script 2

a = 2
b = "babar"
"babar"
Liste = a
String = {1 : "un","B":b,"babar":"babar"}




"""

Exercice 2 :

Pour les scripts suivants donner le nom des fonctions, les arguments de ces fonctions et ce qu'elles renvoient.

"""


# Script 1
def Fonction1(a,b,c):
    return a + b + c


# Script 2
def AvecUnReturn(p,pp):
    a = p + pp
    print(a)

# Script 3

def EnFaitIlNyAvaitPasDeReturnAvant(argument):
    return str(argument)

# Script 4
def PasD_Inspiration():
    a = input("Mettez un nombre")
    A = int(a)
    return A + 3


"""

Exercice 3 :

Dans les prochains scripts, donner le noms des variables et dire si elles sont locales ou globales. De plus donner leur type.

Une variable locale est une variable à l'intérieur d'une fonction. C'est une variable intermédiaire que la console ne connait pas.

Une variable globale est une variable définit à l'exterieur de toute fonction. Indication : Une classe et une fonction sont des variables globales.

"""


# Script 1

a = 1
b = "2"
c = "Babar"


# Script 2

a = 1
b = "2"

def Babar(c):
    return c


# Script 3

a = "ff"
b = 3
def Barbare(b):
    c = b + 1
    return c**2


# Script 4

a = 1
deux = "2"
def Trois():
    aa = 3
    b = 4
    return a + b
C = Trois()



"""

Exercice 4 :

Recopier et Corriger les Scripts suivants

"""

# Script 1

def fonction()
    return 3

# Script 2

for i in range(3)
    print(i)

# Script 3

for i in range(3):
print(i)

# Script 4

def Fonction():
    a = "Kikou"
    b = 2
    return a + b