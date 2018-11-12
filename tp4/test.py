# Coloration des sommets d'un graphe non orienté

from naive import *
from glutton import *
from glutton2 import * # welsh and powell

Petersen=[[],[2,5,6],[1,3,7],[2,4,8],[3,5,9],[1,4,10],[1,8,9],[2,9,10],[3,6,10],[4,6,7],[5,7,8]]
G=[[],[2,3,4],[1,3,4,5],[1,2,4,5,6],[1,2,3,6],[2,3,7],[3,4,7],[5,6]]


# 1) Coloration Naïve
# on a besoin d'une fonction pour trouver  le plus petit entier>=1
# qui n'est pas dans la liste des couleurs interdites

print(mini([1,4,2,6,9]) )   
    
print("Coloration naïve du graphe de Petersen")
print(colorNaive(Petersen))
print("Coloration naïve du graphe G")
print(colorNaive(G))


# 2) Coloration gloutonne
# Ici il nous faut le calcul du noyau d'un ensemble de sommets
# c'est à dire une liste maximale sans couple de sommets adjacents

print("Coloration gloutonne du graphe de Petersen")
print(colorGlouton(Petersen))           
print("Coloration gloutonne du graphe G")
print(colorGlouton(G))


# 3) Complément pour occuper les plus rapides :
#   Coloration de Welsh et Powell
# On a vu en TD qu'on diminue sensiblement le nombre de couleurs nécessaires
# en traitant les sommets dans l'ordre décroissant des degrés

# On peut trier une liste d'objets à l'aide de la fonction sorted en donnant en paramètre
# la partie de l'objet sur laquelle porte le tri avec la syntaxe
# key=lambda x: "partie de x sur laquelle porte le tri". reverse donner un tri
# dans l'ordre décroissant, nous utiliserons donc
# sorted(Deg, key=lambda x: x[1],reverse=True)


print("Coloration de Welsh et Powell du graphe de Petersen")
print(colorWP(Petersen))
print("Coloration de Welsh et Powell du graphe G")
print(colorWP(G))

