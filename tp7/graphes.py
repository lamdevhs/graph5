from vect import *




G7liste = [[1,2,10], [1,3,3], [1,5,6], [2,1,0],
  [3,2,4], [3,5,2], [4,3,1], [4,5,3], [5,2,0], [5,6,1],
  [6,1,2], [6,2,1]]
# ^ cyclique mais a poids positifs

G8liste = [[1,2,1], [1,3,-2], [2,4,-2], [3,2,1], [3,4,5],
  [3,5,4], [5,6,-1], [6,4,-5]]
# ^ poids negatif mais sans cycle, pour bellman

def conversion(n,L):
    G = initVectList(n+1)
    M = initMat(n,0)
    for areteValuee in L:
      i = areteValuee[0]
      j = areteValuee[1]
      w = areteValuee[2]
      M[i-1][j-1] = w
      G[i].append(j) # oriente
    return (G,M)

(G7, M7) = conversion (6, G7liste)
(G8, M8) = conversion (6, G8liste)

def conversion2(n,L):
    G = initVectList(n+1)
    Pred = initVectList(n+1)
    M = initMat(n,0)
    for areteValuee in L:
      i = areteValuee[0]
      j = areteValuee[1]
      w = areteValuee[2]
      M[i-1][j-1] = w
      G[i].append(j) # oriente
      Pred[j].append(i)
    return (G,Pred,M)

(G8, Pred8, M8) = conversion2 (6, G8liste)
