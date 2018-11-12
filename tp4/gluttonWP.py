
def sommets(G):
  return range(1,len(G))

def addNoyau(G,coloration, couleur):
  taille = 0
  for s in sommets(G):
    if coloration[s] == -1: # si pas colorie
      ok = True # peut-on colorer s avec la nouvelle couleur
      for voisin in G[s]:
        if coloration[voisin] == couleur:
          # un voisin a deja la nouvelle couleur
          ok = False
          break # on abandonne, break la loop sur voisin
      if ok:
        coloration[s] = couleur
        taille += 1
  return taille # taille du nouveau noyau

def sortByDecreasingDegree(G):
  G2 = zip(G[1:], range(1,len(G)))
  f = lambda tup: len(tup[0])
  return sorted(G2, key = f, reverse = True)

def unzip(l):
  A = []
  B = []
  for tup in l:
    a,b = tup
    A.append(a)
    B.append(b)
  return A,B
  
def colorWP(G):
  n = len(G) - 1 # ordre de G
  zipped = sortByDecreasingDegree(G)
  (G,indices) = unzip(zipped)
  indices.insert(0,0)
  G.insert(0,[])
  print(G)
  print(indices)
  sommetsColories = 0
  coloration = [-1 for i in range(len(G))]
  for couleur in range(len(G)-1): # on aura besoin de n couleurs max, [0,n-1]
    sommetsColories += addNoyau(G, coloration, couleur)
    if sommetsColories == n: # fini
      break
  print(coloration)
  print(indices)
  zipped = zip(coloration,indices)
  s = sorted(zipped, key = lambda tup: tup[1])
  coloration,_ = unzip(s)
  return coloration # normalement cette instruction est inutile

def coloration(G):
  return colorGluttonWP(G)

