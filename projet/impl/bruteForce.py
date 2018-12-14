from vect import *
from copy import copy

def bruteForce_rec_draft(i, G, X, M, cardM, bestCardM, bestM):
  if i == len(X): # the end: we matched all vertices in X
    return cardM, copy(M)
  x = X[i]
  stuck = True
  for y in G[x]:
    if M[y] == 0: # y is still free
      stuck = False
      M[y] = x
      resultCard, resultM = bruteForce_rec(
         i + 1, G, X, M, cardM + 1, bestCardM, bestM)
      # ^ we try to match as many other vertices of X
      # as possible
      if resultCard > bestCardM:
        # we found a better matching
        bestCardM = resultCard
        bestM = resultM
      M[y] = 0
      cardM -= 1
  if stuck:
    pass
  return bestCardM, bestM
     
def bruteForce_rec(i, G, X, M, solutions):
  if i == len(X):
    print("Reached full end: cardM =", i)
    print("retourne best", i)
    solutions.append(copy(M))
    return
  x = X[i]
  stuck = True
  for y in G[x]:
    if M[y] == 0: # y is still free
      stuck = False
      print("Match", x, "with", y)
      M[y] = x
      M[x] = y
      bruteForce_rec(i + 1, G, X, M, solutions)
      M[y] = 0 # unmatch y
      M[x] = 0 # unmatch x
  bruteForce_rec(i + 1, G, X, M, solutions)
  # ^ we continue, leaving X unmatched
  return

def bruteForce(G, X):
  M = initVect(len(G), 0)
  solutions = []
  bruteForce_rec(0, G, X, M, solutions)
  return solutions
