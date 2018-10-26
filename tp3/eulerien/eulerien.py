from vect import *

def sommets(G):
  return range(1, len(G))

def testEulerien(G):
  # par hypothese G est connexe évidemment
  odd_nodes = []
  for s in sommets(G):
    if len(G[s]) % 2 == 1:
      odd_nodes.append(s)
  n_odd = len(odd_nodes)
  if n_odd == 0:
    return (2, odd_nodes) # admet un cycle eulerien
  elif n_odd == 2:
    return (1, odd_nodes)
    # admet un chemin eulerien
    # les extrémités sont les deux
    # éléments de odd_nodes
  else :
    return (0, odd_nodes) # n'est pas eulerien

K4 = [[], [2,3,4], [1,3,4], [1,2,4], [1,2,3]]
K5 = [[], [2,3,4,5], [1,3,4,5], [1,2,4,5], [1,2,3,4]]
rectangle = [[], [2,8], [1,8,7,3], [2,8,6,4], [3,7,6,5],
  [4,6], [4,3,5,7], [2,4,6,8], [1,2,3,7]]
chemin = [[], [4,5,2,6], [1,6,5,3], [2], [1], [1,2], [1,2]]

def cheminSimple(G, start):
  newG = copy(G)
  chemin = []
  here = start
  return newG

print(testEulerien(K4))
print(testEulerien(K5))
print(testEulerien(rectangle))
print(testEulerien(chemin))


