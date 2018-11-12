from graphes import *

def isConnexe_rec(G, i, Visite):
  Visite[i] = 1
  count = 1
  for succ in G[i]:
    if Visite[succ] == 0:
      # voisin non visite
      count += isConnexe_rec(G, succ, Visite)
    else :
      # revisite d'un sommet
      pass
  return count

def isConnexe(G):
  Visite = [0 for i in range(0,len(G))]
  count = isConnexe_rec(G, 1, Visite)
  return count == len(G) - 1 

G = [[],[2,3],[1,3],[1,2]]
print(isConnexe(G))
G = [[],[2,3],[1,3],[1,2],[5],[4]]
print(isConnexe(G))
print(isConnexe(K4))
print(isConnexe(K5))
print(isConnexe(K6))
print(isConnexe(K7))
print(isConnexe(Petersen))
print(isConnexe(wheels2))
