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

G = buildBipartite(12, B)
print(G)


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
  M = initVect(n+1, 0) # represents the matching
  size = 0 # the size of the matching M
  shortest, depths = shortestAugmentingPath(G, X, Y, M)
  while shortest > 0:
    visited = initVect(n+1, False)
    for x in X:
      if M[x] == 0: # if x is free
        found = findAugmentingPath(x, G, X, Y, M,
                    visited, depths, shortest)
        if found: # if an augmenting path from x was found
          size += 1
    shortest, depths = shortestAugmentingPath(G, X, Y, M)
  return (M, size)

def shortestAugmentingPath(G, X, Y, M):
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
M = [0,6,10,8,0,7,1,5,3,0,2]
shortestAugmentingPath(G, X, Y, M)
M = [0 for i in M]
shortestAugmentingPath(G, X, Y, M)

def findAugmentingPath(x, G, X, Y, visited, depths, shortest)
  found = False
  




# TODO list:
# -- delete Y from arguments of shortest augmenting path
