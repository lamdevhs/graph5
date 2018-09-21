from vect import *
from TP1GraphesNonOrientes import *
from graphes import *

def listToMatrix(G):
  n = nbSommets(G)
  M = initMat(n,0)
  for i in sommets(G):
    adjacents = G[i]
    for j in adjacents:
      M[i-1][j-1] += 1
  return M

def areteToList(n, L):
  G = newGraph(n)
  for arete in L:
    ajoutArete(G, arete[0], arete[1])
  return G

def matToList(M):
  for

def nonOriente(M):
  for i in range(len(M)):
    for j in range(i, len(M)):
      if M[i][j] != M[j][i]:
        return False
  return True

def test():
  def test_listToMatrix(G):
    print(G)
    M = listToMatrix(G)
    affMat(M)
  test_listToMatrix(K6)
  test_listToMatrix(G2)
  print("test areteToList:",
    "allok" if areteToList(5, aG2) == G2 else "error")
  oriente = initMat(4,0)
  oriente[1][2] = 42
  print("test non oriente",
    "allok" if nonOriente(listToMatrix(G2))
      and nonOriente(listToMatrix(K6))
      and not nonOriente(oriente)
      else "error")

  
test()
