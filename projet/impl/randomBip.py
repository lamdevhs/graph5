from vect import *
import random

def randomBool(): 
  return bool(random.getrandbits(1))

# V = {1,...,|X|} union {|X|+1,..., n}
# |V| = n and y = |Y| = n - |X|
def randomBipartite(n, cardX):
  G = initVectList(n+1)
  cardY = n - cardX
  X = range(1, cardX + 1)
  Y = range(cardX + 1, n + 1)
  for x in X:
    Vx = G[x]
    while len(Vx) == 0: # nobody wants to be alone
      for y in Y:
        if randomBool():
          Vx.append(y)
          G[y].append(x)
  return G

# Same as the other one, but
# with the constraint:
# forall x in X,  d(x) <= x
def randomSparseBipartite(n, cardX):
  G = initVectList(n+1)
  cardY = n - cardX
  X = range(1, cardX + 1)
  Y = range(cardX + 1, n + 1)
  for x in X:
    Vx = G[x]
    dx = 0 # degré de x
    while len(Vx) == 0: # nobody wants to be alone
      for y in Y:
        if randomBool():
          dx += 1
          Vx.append(y)
          G[y].append(x)
        if dx == x:
          break # casse la for loop
  return G

# Crée un graphe aléatoire G = (X u Y, E)
# avec E subset X x Y,
# n = |X u Y| et B = {1, ..., k} subset X
# avec n/2 = |X| = |Y|
# avec k <= |X|
# est un ensemble tel que |B| = k > |V(B)|
# En d'autres termes, G ne respecte pas
# le théorème de Hall
def randomImperfectBipartite(halfn):
  n = halfn*2
  G = initVectList(n+1)
  cardX = halfn
  cardY = halfn
  Y = range(cardX + 1, n + 1)
  k = random.randint(2,cardX) # 2 <= k <= |X|
  B = range(1, k+1)
  X_minus_B = range(k+1, cardX + 1) # éventuellement vide
  cardVB = random.randint(1,k-1) # == |V(B)|
  # càd nombre de voisins des sommets de B dans Y
  # bon concrètement c'est juste une borne maximale
  # 1 <= cardVB < k
  VB = range(halfn + 1, halfn + cardVB + 1)
  for x in B:
    Vx = G[x]
    dx = 0 # degré de x
    while len(Vx) == 0: # nobody wants to be alone
      for y in VB:
        if randomBool():
          dx += 1
          Vx.append(y)
          G[y].append(x)
        if dx == x:
          break # end for loop prématurément

  for x in X_minus_B:
    Vx = G[x]
    dx = 0 # degré de x
    while len(Vx) == 0: # nobody wants to be alone
      for y in Y:
        if randomBool():
          dx += 1
          Vx.append(y)
          G[y].append(x)
        if dx == x:
          break # end for loop prématurément
  return G


for n in range(10,20):
  cardY = n//2
  test = randomBipartite(n,cardY)
  print(n-cardY, cardY, test)
