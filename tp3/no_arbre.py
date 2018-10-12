from vect import *

def nodesOf(graph):
  return range(1, len(graph))

def visitsVector(graph):
  return initVect(len(graph), 0)

def size(graph):
  return len(graph) - 1

def isTree(graph):
  def dfs_rec(graph, i, visits, parent):
    visits[i] = 1
    # start visit of i
    for j in graph[i]:
      if j != parent:
        if visits[j] == 0:
          cyclique = dfs_rec(graph, j, visits, parent = i)
          if cyclique:
            return True # stop parcours
        else:
          # revisite (pas du parent)
          # donc cycle detecte
          return True
          # ^ stop parcours: graphe est cyclique
    # end visit of i
    return False # continuer parcours
    
  def gdfs(graph):
    visits = visitsVector(graph)
    nodes = nodesOf(graph)
    for i in nodes:
      if visits[i] == 0:
        cyclique = dfs_rec(graph, i, visits, parent = 0)
        # sommet 0 n'existe pas: pas de parent
        # car debut de parcours a partir de i

        if cyclique:
          return True # stop parcours
    return False

  cyclique = gdfs(graph)
  #print (graph)
  return cyclique
  
print("ces graphes sont-ils cycliques?")


G2 = [[],[2,5,5], [1,3,4,4], [2,3,4], [2,2,3,5], [1,1,4]]
print("G2", isCyclique(G2))

  # ==== graphes non cycliques
pasCyclique1 = [[], [2], [1,3,4,5], [2,7,6], [2], [2], [3], [3]]
pasCyclique2 = [[], [2], [1,3,4,5], [2,7,6], [2], [2], [3], [3],
  [9, 10], [8], [8]]
  # ^ celui-la n'est pas connexe

  # ==== graphes cycliques
cyclique1 = [[], [2], [1,3,4,5], [2,7,6], [2], [2], [3, 7], [3, 6]]
cyclique2 = [[], [2], [1,3,4,5], [2,7,6], [2], [2], [3], [3],
  [9, 10], [8,10], [8,9]]
  # ^ celui-la n'est pas connexe

print("pasCyclique1", isCyclique(pasCyclique1))
print("pasCyclique2", isCyclique(pasCyclique2))
print("cyclique1", isCyclique(cyclique1))
print("cyclique2", isCyclique(cyclique2))

