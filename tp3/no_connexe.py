from vect import *

def visitsVector(graph):
  return initVect(len(graph), 0)

def size(graph):
  return len(graph) - 1

def isConnected(graph, i = 1):
  def dfs_rec(graph, i, visits, newvisit):
    visits[i] = 1
    # start visit of i
    newvisit()
    for j in graph[i]:
      if visits[j] == 0:
        dfs_rec(graph, j, visits, newvisit)
      else:
        pass # visit j again
    # end visit of i
    
  def dfs(graph, i, newvisit):
    dfs_rec(graph, i, visitsVector(graph), newvisit)

  count = 0
  def newvisit():
    nonlocal count
    count += 1
  dfs(graph, i, newvisit)
  isconnected = count == size(graph)
  print(graph, count, isconnected)
  return isconnected
  
G2 = [[],[2,5,5], [1,3,4,4], [2,3,4], [2,2,3,5], [1,1,4]]
print(isConnected(G2))
print(isConnected(G2 + [[]]))
# ^ on ajoute un unique point isole
