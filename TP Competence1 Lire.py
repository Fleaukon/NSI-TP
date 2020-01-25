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

Pour les scripts suivants donner le nom des variables et dire si les variables sont locales (contenues dans des fonctions) ou non (à l'exterieur des fonctions, que la console connait)

"""


# Script 1
a = 2
def f(n):
    m = n + 1
    return m


# Script 2
n = 1
def f(n):
    m = n**n
    return m

m = f(n)

# Script