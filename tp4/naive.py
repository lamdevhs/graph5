def sommets(G):
  return range(1,len(G))

def mini(L): # on suppose que L est une liste d'entiers
  n = len(L)
  I = list(range(0,n+1)) # il y aura forcement un entier dans [0,n]
  # qui ne sera pas dans L puisque len(L) < card[0,n]
  #print("L,I",L,I)
  for val in L:
    if val >= 0 and val <= n:
      # si val n'est pas une valeur de I, on l'ignore
      I[val] = -1
  for k in I: # on parcourt I et on recupere la premiere valeur
    # qui n'est pas -1
    if k >= 0:
      return k

def colorNaive(G):
  couleurs = [-1 for i in range(len(G))]
  for s in sommets(G):
    voisins = G[s]
    couleursDesVoisins = list(map(lambda v: couleurs[v], voisins))
    couleurs[s] = mini(couleursDesVoisins)
    
  return couleurs
    
def coloration(G):
  return colorNaive(G)
