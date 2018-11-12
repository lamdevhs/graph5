
def sommets(G):
  return range(1,len(G))

def noyau(G,coloration, couleur, ordreSommets):
  taille = 0
  for s in ordreSommets:
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
  
# def unzip(l):
#   A = []
#   B = []
#   for tup in l:
#     a,b = tup
#     A.append(a)
#     B.append(b)
#   return A,B
  
def colorWP(G):
  n = len(G) - 1 # ordre de G
  
  # zipped = zip(G[1:], range(1,len(G)))
  # f = lambda tup: len(tup[0])
  # sortedZipped = sorted(zipped, key = f, reverse = True)
  # _,ordreSommets = unzip(sortedZipped)

  k = lambda i: len(G[i])
  ordreSommets = sorted(range(1,len(G)), key = k, reverse = True)

  sommetsColories = 0
  coloration = [-1 for i in range(len(G))]
  for couleur in range(len(G)-1): # on aura besoin de n couleurs max, [0,n-1]
    sommetsColories += noyau(G, coloration, couleur, ordreSommets)
    if sommetsColories == n: # fini
      return coloration
  return coloration # normalement cette instruction est inutile

def coloration(G):
  return colorGlutton(G)

