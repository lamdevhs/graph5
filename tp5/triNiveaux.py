from vect import *

def sommets(G):
  return range(1, len(G))

def degEntrants(G):
  degresE = initVect(len(G), 0)
  for s in sommets(G):
    for i in G[s]:
      degresE[i] += 1
  return degresE

def triNiveaux(G):
  n = len(G) - 1
  S = []
  niveaux = initVect(len(G), -1) # va contenir les numeros de niveaux des elements
  N = []
  deg = degEntrants(G)
  compteur = 0
  for s in sommets(G):
    if deg[s] == 0:
      S.append(s)
      niveaux[s] = 0 # premier niveau
      print("ajout de",s,"dans S")
  
  while len(S) != 0:
    head = S.pop(0)
    if len(N) - 1  < niveaux[head]: # N ne contient pas assez de niveaux
      N.append([]) # on cree un autre niveau
    N[niveaux[head]].append(head) # on ajoute cette source a son niveau
    compteur += 1
    print("ajout de", head,"dans le niveau", niveaux[head])
    for friend in G[head]:
      print(friend, "est un ami de", head)
      deg[friend] -= 1
      if deg[friend] == 0:
        S.append(friend)
        niveaux[friend] = niveaux[head] + 1
        print("ajout de",friend,"dans S")
  if compteur == n:
    return N
  else:
    return False # G contient un cycle, tri par niveaux impossible

G = [[],[2,3],[3],[]]
print("==== resultat pour G =", G, " :\n====",
  triNiveaux(G))
G = [[],[2,3],[3],[1]]
print("==== resultat pour G =", G, " :\n====",
  triNiveaux(G))

print("==== resultat pour G =", G, " :\n====",
   triNiveaux([[],[2,7],[6],[2,4,5], [5], [], [5,7], []]))
print("==== resultat pour G =", G, " :\n====",
  triNiveaux([[],[],[5],[],[8,9], [7,6,8,11], [3], [1], [9], [], [7], []]))
