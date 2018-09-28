from vect import *
from TP1GraphesOrientes import *
from graphes import *

def listToMatrix(G):
  n = nbSommets(G)
  M = initMat(n,0)
  for i in sommets(G):
    adjacents = G[i]
    for j in adjacents:
      M[i-1][j-1] += 1
  return M

def arcsToList(n, L):
  G = newGraph(n)
  for arc in L:
    ajoutArc(G, arc[0], arc[1])
  return G

def matToList(M):
  n = len(M)
  G = newGraph(n)
  for i in range(0,n):
    for j in range(0,n):
      for k in range(0, M[i][j]):
        ajoutArete(G, i+1, j+1)
  return G
      
def test():
  def test_listToMatrix(G):
    print(G)
    M = listToMatrix(G)
    affMat(M)
  test_listToMatrix(G1)
  print("test areteToList:",
    "allok" if arcsToList(5, aG1) == G1 else "error")
  
test()
