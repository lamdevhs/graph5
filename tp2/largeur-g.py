from vect import *

def sommets(G):
  return range(1,len(G))

def largeurG(G):
  print("= Debut parcours largeur generalise G", G)
  s = sommets(G)
  n = len(s)
  Visite = initVect(n+1, 0)
    # ^ Visite[0] ne correspond a rien
    # puisque il n'y a pas de sommet 0
  ordreVisite = []
  print("= Vecteur visite", Visite)
  print("= Ordre de visite", ordreVisite)
  for i in s:
    if Visite[i] == 1:
      print("== revisite parcours generalise", i)
      continue
    
    print("== Debut de parcours simple a partir du sommet", i)
    Visite[i] = 1
    File = [i]
    ordreVisite = [i]
    print("   entree dans file", i, File)
    print("   Ordre de visite", ordreVisite)
    print("   Vecteur visite", Visite)
    while len(File) != 0:
      head = File.pop(0)
      print("   . tete de file traitee", head, File)
      for j in G[head]:
        if Visite[j] == 1:
          print("     . revisite", j)
        else:
          Visite[j] = 1
          File.append(j)
          ordreVisite.append(j)
          print("     . entree dans file", j, File)
          print("       Ordre de visite", ordreVisite)
          print("       Vecteur visite", Visite)
    print("== Fin de parcours simple, ordre de visite", ordreVisite)
  print("= Fin de parcours generalise, ordre de visite", ordreVisite)
  print("= Vecteur visite", Visite)
  print("= Ordre de visite", ordreVisite)
  return ordreVisite

G1 = [[],[5],[1,4],[2],[3],[2,4]]
G2 = [[],[5],[1,4,5],[2,4],[],[4]]
G3 = [[],[3,5,6],[1],[2,4],[],[],[4]]
Petersen = [[],
  [2,5,6],[1,3,7],[2,4,8],[3,5,9],[1,4,10],
  [1,8,9],[2,9,10],[3,6,10],[4,6,7],[5,7,8]]

print("\n\n------- parcours G1")
largeurG(G1)
print("\n\n------- parcours G2")
largeurG(G2)
print("\n\n------- parcours G3")
largeurG(G3)
print("\n\n------- parcours Petersen")
largeurG(Petersen)


    
  
