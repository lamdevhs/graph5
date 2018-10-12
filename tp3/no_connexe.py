from vect import *
from graphs import *

def visitsVector(graph):
  return initVect(len(graph), 0)

def size(graph):
  return len(graph) - 1

# def gdfs(graph):
#   visits = visitsVector(graph)
#   nodes = nodesOf(graph)
#   for i in nodes:
#     if visits[i] == 0:
#       dfs_rec(graph, i, visits)

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

  #global count
  count = 0
  def newvisit():
    nonlocal count
    count += 1
  dfs(graph, i, newvisit)
  print (graph)
  print (count, size(graph))
  return count == size(graph)
  
print(isConnected(G2))
print(isConnected(G2 + [[]]))
