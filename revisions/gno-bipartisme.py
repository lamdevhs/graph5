from graphes import *

def sommets(G):
  return range(1,len(G))

def bipartisme(G):
  Visite = [0 for i in range(0,len(G))]
  partition = [[], [], []] # les deux dernieres listes sont pour les composantes
  # de bipartisme, la premiere c'est pour decaler les indices car les deux couleurs
  # seront 1 et 2
  for i in sommets(G):
    if Visite[i] != 0:
      continue # deja visité (deja colorié)
    
    File = [i]
    Visite[i] = 1 # couleurs = 1,2
    partition[1].append(i)
    while len(File) != 0:
      head = File.pop(0)
      headColor = Visite[head]
      goodColor = 3 - headColor
      for succ in G[head]:
        # ^ la bonne couleur pour une revisite d'un voisin qui ne detecte pas de cycle impair
        # et c'est aussi la couleur à attribuer aux voisins de head
        if Visite[succ] != 0: # voisin deja visite
          # revisite: cycle, on verifie qu'il n'est pas impair:
          if Visite[succ] != goodColor:
            # dans le cycle contenant l'arete (head, succ), les sommets
            # head et succ ont meme couleur => longueur impair
            return False # G n'est pas biparti car il possede un cycle de longueur impair
          else:
            pass # rien a faire et tout va bien
        else: # succ pas encore visité
          Visite[succ] = goodColor
          File.append(succ)
          partition[goodColor].append(succ) # on ajoute succ a sa composante de bipartisme
      
  return partition[1], partition[2]  
  
print(bipartisme(K2))
print(bipartisme(K3))
print(bipartisme(K4))
print(bipartisme([[], [4,6],[3,5],[2],[1,5],[2,4],[1]]))
print(bipartisme([[], [2,4,6,8],[1],[],[1],[],[1],[],[1],[]]))
print(bipartisme([[], [2,4,6,8],[1,4],[],[1,2],[],[1],[],[1],[]]))
