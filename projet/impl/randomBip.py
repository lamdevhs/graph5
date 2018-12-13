from vect import *
import random

def randomBool(): 
  return bool(random.getrandbits(1))

# V = {1,...,|X|} union {|X|+1,..., n}
# |V| = n and y = |Y| = n - |X|
def randomBipartite(n, cardY):
  L = initVectList(cardY)
  cardX = n - cardY
  for l in L:
    while len(l) == 0: # no loose ends
      for x in range(1,cardX +1):
        if randomBool():
          l.append(x)
  return L

# Same as the other one, but
# with the constraint:
# forall x in X,  V(x) <= x
def randomSparseBipartite(n, cardX):
  L = initVectList(cardX)
  cardX = n - cardX
  for l in L:
    while len(l) == 0: # no loose ends
      for x in range(1,cardX +1):
        if randomBool():
          l.append(x)
  return L

for n in range(10,20):
  cardY = n//2
  test = randomBipartite(n,cardY)
  print(n-cardY, cardY, test)
