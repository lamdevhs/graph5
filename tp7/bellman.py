from vect import *
from graphes import *

infty = float('inf')

def bellman(G, Pred, M, s):
  File = []
  VoisinsInconnus = list(map(lambda x: len(x), Pred))
  Dist = initVect(len(G), infty)
  Parent = initVect(len(G), 0)

  Dist[s] = 0
  Parent[s] = s
  VoisinsInconnus[s] = 0
  File.append(s)

  while len(File) != 0:
    head = File.pop(0)
    #print(head)
    for friend in G[head]:
      #print(friend)
      VoisinsInconnus[friend] -= 1
      v = VoisinsInconnus[friend]
      #print(v)
      if v == 0:
        w = M[head-1][friend-1]
        File.append(friend)
        Dist[friend] = Dist[head] + w
        Parent[friend] = head
  return (Dist, Parent)

def minimum(File, Dist):
  mini = 0
  minid = Dist[File[0]]
  k = 0
  for f in File:
    d = Dist[f]
    if d < minid:
      mini = k
      minid = d
    k+=1
  return mini

def dijkstra2(G, M, s):
  File = []
  Changed = initVect(len(G), False)
  Dist = initVect(len(G), infty)
  Parent = initVect(len(G), 0)

  File.append(s)
  Dist[s] = 0
  Parent[s] = s
  Changed[s] = True

  while len(File) != 0:
    ix = minimum(File, Dist)
    head = File.pop(ix)
    #print(Dist)
    if Changed[head]:
      for friend in G[head]:
        #print(friend)
        w = M[head-1][friend-1]
        d = Dist[head] + w
        old = Dist[friend]
        #print(head, friend, w, d, old)
        if d < old:
          #print(True)
          Dist[friend] = d
          Parent[friend] = head
          File.append(friend)
          Changed[friend] = True
  return (Dist, Parent)

res = bellman(G8,Pred8,M8,1)
print(res)
res = dijkstra2(G8,M8,1)
print(res)
