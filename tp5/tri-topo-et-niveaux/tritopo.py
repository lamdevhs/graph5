from vect import *

def sommets(G):
  return range(1, len(G))

def degEntrants(G):
  degresE = initVect(len(G), 0)
  for s in sommets(G):
    for i in G[s]:
      degresE[i] += 1
  return degresE

def triTopo(G):
  n = len(G) - 1
  T = []
  S = []
  deg = degEntrants(G)
  for s in sommets(G):
    if deg[s] == 0:
      S.append(s)
      print("ajout de",s,"dans S")
  
  while len(S) != 0:
    head = S.pop(0)
    T.append(head)
    print("ajout de",head,"dans T")
    for friend in G[head]:
      print("friend:", head, friend)
      deg[friend] -= 1
      if deg[friend] == 0:
        S.append(friend)
        print("ajout de",friend,"dans S")
  if len(T) == n:
    return T
  else:
    return False # G contient un cycle, tri topo impossible

G = [[],[2,3],[3],[]]
print(triTopo(G))

print(triTopo([[],[2,7],[6],[2,4,5], [5], [], [5,7], []]))
