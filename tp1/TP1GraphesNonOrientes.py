from vect import *

# graphe ou multigraphe non orienté par liste d'adjacence

def newGraph(size):
  return initVectList(size + 1)

def sommets(G):
  return range(1, len(G))

def nbSommets(G):
  return len(G) - 1

# attention aux boucles {i,i} qui doivent etre
# comptees une seule fois
# on ne peut donc pas juste additionner les longueurs
# de chaque liste d'adjacence de chaque sommet et puis
# diviser par deux
# on compte une arete pour tout couple {i,j}, i <= j
def nbArete(G):
  r = 0
  for i in sommets(G):
    for j in G[i]:
      if i <= j:
        r += 1
  return r

def ajoutArete(G, i, j):
  G[i].append(j)
  if j != i:
    G[j].append(i)

def enleveArete(G,i,j):
  G[i] = enleveUn(G[i],j)
  if j != i:
    G[j] = enleveUn(G[j],i)

def enleveUn(liste,val):
  r = []
  found = False
  for k in liste:
    if not found and k == val:
      found = True
    else:
      r.append(k)
  return r

def deg(G,i):
  return len(G[i])

def degre(G):
  r = initVect(nbSommets(G), 0)
  for i in range(1, len(G)):
    r[i-1] = deg(G,i)
  return r

# on ne doit ajouter un couple (i,j) comme
# arete que lorsque i different de j, et
# i inferieur ou egal a j pour eviter les
# doublons, d'ou au final uniquement lorsque
# i < j
def kuratowski(n):
  G = newGraph(n)
  for i in sommets(G):
    for j in sommets(G):
      if i < j:
        ajoutArete(G,i,j)
  return G
  
if __name__ == "__main__":
  def test():
    G = initVectList(5+1)
    print("vide", G)
    ajoutArete(G, 1,2)
    ajoutArete(G, 1,5)
    ajoutArete(G, 1,5)
    ajoutArete(G, 2,3)
    ajoutArete(G, 2,4)
    ajoutArete(G, 2,4)
    ajoutArete(G, 3,3)
    ajoutArete(G, 3,4)
    ajoutArete(G, 4,5)
    print("G2 =", G)
    print("degre(G)", degre(G))
    enleveArete(G, 1,2)
    enleveArete(G, 1,5)
    enleveArete(G, 1,5)
    print(G)
    enleveArete(G, 2,3)
    enleveArete(G, 2,4)
    print(G)
    enleveArete(G, 2,4)
    enleveArete(G, 3,3)
    print(G)
    enleveArete(G, 3,4)
    enleveArete(G, 4,5)
    print(G)
    K6 = kuratowski(6)
    print("kuratowski 6", K6)
    print("degree K6", degre(K6))
    
  test()
