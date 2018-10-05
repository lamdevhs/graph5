from vect import *
from graphes import *

def sommets(G):
  return range(1,len(G))

def profRec(G, i, Visite, ordreVisite, prefix=" "):
  print(prefix + ". Appel profRec sur", i, Visite, ordreVisite)
  # definir i comme visite
  Visite[i] = 1
  # ajouter i a la liste de ordreVisite (cas premiere visite)
  ordreVisite.append(j)
  for j in G[i]:
    # si j n'a pas ete visite
    if Visite[j] == 0:
      # rappeler profRec: descente recursive
      profRec(G, j, Visite, ordreVisite, prefix + " ")
   # sinon: marquer revisite
   else:
      print(prefix + ". Revisite", j)
   # ajouter i a la liste de ordreVisite (cas derniere visite)
   #ordreVisite.append(j)
   
  # quitter profRec, remonter la pile de recursion
  print(prefix + ". Fin profRec sur", i, Visite, ordreVisite)
  

def profond(G, i):
  s = sommets(G)
  n = len(s)
  Visite = initVect(n+1, 0)
  ordreVisite = []
  profRec(G, i, Visite, ordreVisite)
  return ordreVisite

profond(oG1, 1)
profond(oG2, 1)
profond(oG3, 1)
profond(Peterson, 1)
