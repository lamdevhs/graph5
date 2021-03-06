from vect import *

# graphes simples orientés par liste d'adjacence

def newGraph(size):
  return initVectList(size + 1)

def sommets(G):
  return range(1, len(G))

def nbSommets(G):
  return len(G) - 1

def nbArcs(G):
  return sum(map(len, G))

# cette fonction tient compte du fait que le contexte
# n'autorise que les graphes orientes simples
# en consequence, la fonction refuse d'ajouter un arc deja
# preexistant, et retourne False dans ce cas-la (True dans le
# cas contraire).
def ajoutArc(G, i, j):
  if j in G[i]:
    return False
  else:
    G[i].append(j)
    return True

def enleveArc(G,i,j):
  G[i] = enleveUn(G[i],j)

def enleveUn(liste,val):
  r = []
  found = False
  for k in liste:
    if not found and k == val:
      found = True
    else:
      r.append(k)
  return r

def degS(G,i):
  return len(G[i])

def degreS(G):
  r = initVect(nbSommets(G), 0)
  for i in sommets(G):
    r[i-1] = degS(G,i)
  return r

def voisinageE(G,i):
  v = []
  for j in sommets(G):
    for k in G[j]:
      if k == i:
        v.append(j)
  return v

def degE(G,i):
  return len(voisinageE(G,i))

def degreE(G):
  r = initVect(nbSommets(G), 0)
  for i in sommets(G):
    r[i-1] = degE(G,i)
  return r

if __name__ == "__main__":
  def test():
    G = initVectList(5+1)
    print("vide", G)
    ajoutArc(G, 1,5)
    ajoutArc(G, 2,1)
    ajoutArc(G, 2,4)
    ajoutArc(G, 3,2)
    ajoutArc(G, 4,3)
    ajoutArc(G, 5,2)
    ajoutArc(G, 5,4)
    print("G2 =", G)
    print("nbarcs =", nbArcs(G))
    print("degreS(G)", degreS(G))
    print("degreE(G)", degreE(G))
    print("ajout d'un arc preexistant (5,4):", ajoutArc(G, 5,4), G)
    enleveArc(G, 5,4)
    print(G)
    enleveArc(G, 5,2)
    print(G)
    enleveArc(G, 4,3)
    print(G)
    enleveArc(G, 3,2)
    print(G)
    enleveArc(G, 2,4)
    print(G)
    enleveArc(G, 2,1)
    print(G)
    enleveArc(G, 1,5)
    print(G)
    return
    
  test()
