from vect import *
from graphs import *

def visitsVector(graph):
  return initVect(len(graph), 0)

def size(graph):
  return len(graph) - 1

def dfs_rec(graph, i, visits):
  visits[i] = 1
  startvisit(i, visits) # start visit of i
  for j in graph[i]:
    if visits[j] == 0:
      dfs_rec(graph, j, visits)
    else:
      revisit(i, visits, j) # visit j again
  endvisit(i, visits) # end visit of i
  
def dfs(graph, i, visits):
  dfs_rec(graph, i, visits)

def gdfs(graph):
  visits = visitsVector(graph)
  nodes = nodesOf(graph)
  for i in nodes:
    if visits[i] == 0:
      dfs(graph, i, visits)

count = 0
    
def startvisit(i, visits):
  global count
  count += 1

def endvisit(i, visits):
  pass
def revisit(i, visits, j):
  pass

def isConnected(graph, i = 1):
  global count
  count = 0
  dfs(graph, i, visitsVector(graph))
  print (graph)
  print (count, size(graph))
  return count == size(graph)
  
print(isConnected(G2))
print(isConnected(G2 + [[]]))
