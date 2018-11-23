## Exemple de traitement d'un graphe NON orienté valué : 
## Construction d'un arbre couvrant de poids minimum d'un graphe
from vect import *
from copy import deepcopy


## Représentation d'un graphe non orienté valué
## le graphe est donné sous forme de liste d'arêtes qui sont des triplets [i,j,p(i,j]
## On construit à partir de cette liste la liste d'adjacence et une matrice de poids
## Là encore pour simplifier, le poids de l'arete (i,j) est en M[i,j]
ListAretes=[ [1,2,7],[1,5,6],[1,6,2],[2,3,4],[2,5,5],
     [3,4,1],[3,5,2],[4,5,3],[5,6,1] ]

def areteToListe(n,L):
    G = initVectList(n+1)
    M = initMat(n,0)
    for areteValuee in L:
      i = areteValuee[0]
      j = areteValuee[1]
      w = areteValuee[2]
      M[i-1][j-1] = w
      M[j-1][i-1] = w
      G[i].append(j)
      G[j].append(i)
    return (G,M)

(G,M)=areteToListe(6,ListAretes)
print(G)
affMat(M)


## Algorithme de Kruskal
## Ici la représentation par liste d'arêtes est adaptée
## On suppose que le graphe est connexe sans le vérifier pour ne pas surcharger
def ajoutArete(G,i,j):
    G[i].append(j)
    G[j].append(i)
        

def enleveArete(G,i,j):
    if G[i].count(j) >0:
        G[i].remove(j)
        G[j].remove(i)

def cyclicRec(G,i,pere,Visite,cycle):
    #print("Sommet",i)
    Visite[i]=1
    k=0
    while (k<len(G[i]) and not cycle): # pour une fois c'est fait proprement...
        j=G[i][k]                       
        if Visite[j]==0:
             cycle=cyclicRec(G,j,i,Visite,cycle)
             #print("après exploration de ",j,cycle)
        else:
            if j!=pere:
                #print("Cycle détecté par l'arête en arrière",i,j)
                return True
           #else:
           #print("Je suis ton père!")
        k=k+1
    return cycle
    
def isCyclic(G):
    Visite=initVect(len(G),0)
    cycle=False
    i=1
    while (i<len(G) and not cycle):
        if Visite[i]==0:
            cycle=cyclicRec(G,i,i,Visite,False)
        i=i+1
    return cycle

# Algorithme de Kruskal

def Kruskal(n,L):
    T = initVectList(n+1)
    G, M = areteToListe(n,L)
    P = deepcopy(M)
    poids = 0
    nbAretes = 0
    L.sort(key = lambda a: a[2])
    for a in L:
      i, j, w = a[0], a[1], a[2]
      ajoutArete(T, i, j)
      if (isCyclic(T)):
        enleveArete(T, i, j)
      else:
        poids += w
        P[i-1][j-1] = w
        P[j-1][i-1] = w
        nbAretes += 1
        if nbAretes == n-1:
          break
    return (T,poids)

def isCyclic2(connexite, i, j):
    return connexite[i] == connexite[j]

def connecte(connexite, i, j):
    ival = connexite[i]
    jval = connexite[j]
    for k in range(1,len(connexite)):
      if connexite[k] == jval:
        connexite[k] = ival
    

def Kruskal2(n,L):
    T = initVectList(n+1)
    G, M = areteToListe(n,L)
    P = deepcopy(M)
    connexite = list(range(n+1))
    poids = 0
    nbAretes = 0
    L.sort(key = lambda a: a[2])
    for a in L:
      i, j, w = a[0], a[1], a[2]
      #ajoutArete(T, i, j)
      if (isCyclic2(connexite, i, j)):
        #enleveArete(T, i, j)
        pass
      else:
        ajoutArete(T, i, j)
        connecte(connexite, i, j)
        poids += w
        P[i-1][j-1] = w
        P[j-1][i-1] = w
        nbAretes += 1
        if nbAretes == n-1:
          break
    return (T,poids)

Gcours = [[1,2,1], [2,3,2], [3,4,7], [4,5,10], [6,5,12], [7,6,11], [8,7,6],
[1,8,4], [8,2,8], [8,3,3], [7,4,9], [6,4,13], [2,7,5], [3,6,5]]

print(Kruskal(6,ListAretes))
print(Kruskal(8,Gcours))

print(Kruskal2(6,ListAretes))
print(Kruskal2(8,Gcours))




def updateDist(G,M, Dist, Min, i):
  Dist[i] = 0 # on ajoute I a T
  for j in G[i]:
    w = M[i-1][j-1]
    d = Dist[j]
    if d == -1 or d > w:
      Dist[j] = w
      Min[j] = i

def getMin(Dist):
  m = -1 # ici represente l'infini
  i = -1
  for k in range(len(Dist)):
    v = Dist[k]
    if v > 0 and (m > v or m == -1):
      m = v
      i = k
  return i, m

def Primm(n,L):
  G, M = areteToListe(n,L)
  Dist = initVect(len(G), -1)
  Min = initVect(len(G), 1)
  T = initVectList(len(G))
  poids = 0
  updateDist(G, M, Dist, Min, 1)
  nbAretes = 0
  #print(nbAretes,Dist, Min)
  while nbAretes != n - 1:
    k, w = getMin(Dist)
    #print(k,w)
    poids += w
    s = Min[k]
    T[s].append(k)
    T[k].append(s)
    updateDist(G, M, Dist, Min, k)
    nbAretes += 1
    #print(nbAretes,Dist, Min)
  return T, poids

print(Primm(6, ListAretes))
