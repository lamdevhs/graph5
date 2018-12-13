from vect import *

B = [[1,2],[1,3],[4,5,6],[2],[1,4],[6]]

# The n vertices {1,...,n} of G are partitioned in two groups :
# X = {1, ..., |X|} and Y = {|X| + 1, ..., n}
# All the edges in G are in (X x Y) : G is bipartite.
# Here, L contains a set of lists, each list l_y
# corresponding to all the neighbors x in X
# of the vertex y in Y, for each y in Y :
# l_y = V(y) subset X
# Therefore len(L) = |Y| = n - |X|,
# and the first vertex of Y is precisely :
# y = |X| + 1 = n - |Y| + 1 = n - len(L) + 1
def buildBipartite(n, L):
  G = initVectList(n + 1)
  y = n - len(L) + 1 # cf above
  for l in L: # l = V(y) subset X
    G[y] = l # connect y to all x in l subset X
    for x in l:
      G[x].append(y) # connect x to y (G is not oriented)
    y += 1 # treat next element of Y
  return G

GG = buildBipartite(12, B)
print(GG)


Free = 0
Infinity = float("inf")
    
# Input: (G, X, Y)
# -- G = (V = X union Y, E) bipartite graph
#    represented with a neighborhood list
# -- X, Y: sets of vertices of G forming its bipartition
# Output: (M, size)
# -- M: the matching that the algorithm builds
#       forall i,j in V :
#       --  M[i] = j  <==>  {i,j} is in the matching M
#       --  M[i] = 0  <==> i is not matched by M, i is free
# -- size: |M|
def matchingHK(G, X, Y):
  M = initVect(len(G), 0) # represents the matching
  size = 0 # the size of the matching M
  shortest, depths = shortestAugmentingPath(G, X, M)
  while shortest > 0:
    visited = initVect(len(G), False)
    for x in X:
      if M[x] == 0: # if x is free
        found = findAugmentingPath(x, G, M,
                    visited, depths, shortest)
        if found: # if an augmenting path from x was found
          size += 1
    shortest, depths = shortestAugmentingPath(G, X, M)
  return (M, size)

def shortestAugmentingPath(G, X, M):
  shortest = 0
  depths = initVect(len(G), Infinity)
  visited = initVect(len(G), False)
  queue = []
  for x in X:
    if M[x] == 0: # x is free
      depths[x] = 0
      visited[x] = True
      queue.append(x)
  
  limit = Infinity
  while len(queue) != 0:
    print("** queue =", queue)
    head = queue.pop(0)
    print("popping", head)
    d = depths[head]
    print("d =", d)
    if depths[head] < limit:
      print("under limit =", limit)
      if d % 2 == 0: # even level of depth
        print("even level")
        # the edges searched through after head must be
        # edges *not* in M
        for v in G[head]:
          print("v =", v)
          if not visited[v] and v != M[head]:
            print("(head, v) not in M")
            # the edge (head, v) is not in M: good
            depths[v] = depths[head] + 1
            print("depths[v] =", depths[v])
            visited[v] = True
            queue.append(v)
            if M[v] == 0:
              print("shortest path found")
              # we found a shortest augmenting path
              limit = depths[v]
              shortest = limit # value to be returned
      else: # d == 1 mod 2: odd level of depth
        print("odd level")
        # the edges right after head must be in M
        # so we don't have a choice, the only candidate
        # is (head, M[head])
        v = M[head]
        print("v = M[head] =", v)
        if v != 0 and not visited[v]:
          print("(head, v) is in M")
          depths[v] = depths[head] + 1
          print("depths[v] =", depths[v])
          visited[v] = True
          queue.append(v)
  print("Final thoughts:")
  print(depths)
  print(visited)
  print(shortest)
  print(limit)
  return (shortest, depths)

G = buildBipartite(10, [[1,2,4],[1,5],[3],[3,5],[2,4]])
print(G)
X = [1,2,3,4,5]
Y = [6,7,8,9,10]
M2 = [0,6,10,8,0,7,1,5,3,0,2]
M1 = [0 for i in M2]
shortest1, depths1 = shortestAugmentingPath(G, X, M1)
shortest2, depths2 = shortestAugmentingPath(G, X, M2)

def findAugmentingPath(v, G, M, visited, depths, shortest):
  print("rec into", v)
  d = depths[v]
  print("d =", d)
  visited[v] = True # whether we find a path or not
  if d == shortest:
    # we're already too deep
    # and we haven't found a path yet
    # we failed, so we're done here
    print("gone too deep")
    return False
  if d % 2 == 0: # odd level of depth
    print("odd level of depth")
    # therefore, the next edges to explore must not be in M
    for w in G[v]:
      print("w =", w)
      # we must filter out all w that have been visited
      # and the hypothetical w for which (v,w) is in M
      # and those that were not encountered at depth d+1
      # during the BFS step
      if not visited[w] and M[v] != w and depths[w] == d + 1:
        print("w is OK")
        if M[w] == 0:
          print("w is free: shortest path found")
          # w is free:
          # we found a shortest augmenting path
          visited[w] == True
          found = True
        else:
          # we move on deeper
          print("go in deeper")
          found = findAugmentingPath(w, G, M, visited,
           depths, shortest)
          print("backtrack to v =", v, found)
        if found:
          # we do a symetric difference between M
          # and the path we found, so here
          # we create the edge (v,w) in M
          print("M oplus Path")
          M[v] = w
          M[w] = v
          print("return found")
          return found
  else: # odd level
    print("odd level")
    # the next edge must be in M
    w = M[v]
    print("w = M[v] =", w)
    if w != 0 and not visited[w] and depths[w] == d + 1:
      print("w = M[v] is ok, go deeper")
      # we move on deeper
      found = findAugmentingPath(w, G, M, visited,
           depths, shortest)
      print("back to v =", v)
      if found:
        print("found from below! passive M oplus Path and return found")
        # we do a symetric difference between M
        # and the path we found, so here
        # the edge (v,w) is in M, so we must let
        # the edges before and after it in the path
        # unmatch v and w, so here we do nothing on M
        return found
  print("return False: backtrack dejectedly")
  return False # no augmenting path was found

visited = initVect(len(G), False)
print(depths1)
size = 0
for x in X:
  if M1[x] == 0:
    if findAugmentingPath(x, G, M1, visited, depths1, shortest1):
      size += 1
print("size =",size)
print("M1 after step 1:", M1)
  

visited = initVect(len(G), False)
print(depths2)
size = 4
for x in X:
  if M2[x] == 0:
    if findAugmentingPath(x, G, M2, visited, depths2, shortest2):
      size += 1
print("size =",size)
print("M2 after step 2:", M2)

print(matchingHK(G, X, Y))

def interval (a, b):
  return list(range(a, b+1))
print(matchingHK(GG, interval(1,6), interval(7,12)))

from randomBip import *
from bruteForce import *

bruteForce(GG, interval(1,6))

GGG = buildBipartite(20, randomBipartite(20,8))
print(GGG)
bruteForce(GGG, interval(13,20))
# TODO list:
# -- delete Y from arguments of shortest augmenting path
