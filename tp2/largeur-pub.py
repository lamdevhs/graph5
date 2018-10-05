from vect import *

def sommets(G):
  return range(1,len(G))

def largeur(G, i):
  print("= Debut parcours largeur(G, i)", G, i)
  s = sommets(G)
  n = len(s)
  Visite = initVect(n+1, 0)
    # ^ Visite[0] ne correspond a rien
    # puisque il n'y a pas de sommet 0

  Visite[i] = 1
  File = [i]
  ordreVisite = [i]
  print("entree dans file", i, File)
  print("Ordre de visite:", ordreVisite)
  print("Vecteur visite", Visite)
  while len(File) != 0:
    head = File.pop(0)
    print(". tete de file traitee", head, File)
    for j in G[head]:
      if Visite[j] == 1:
        print("  . revisite", j)
      else:
        Visite[j] = 1
        File.append(j)
        ordreVisite.append(j)
        print("  . entree dans file", j, File)
        print("    Ordre de visite", ordreVisite)
        print("    Vecteur visite", Visite)
  print("= Fin de parcours, ordre de visite", ordreVisite)
  return ordreVisite

G1 = [[],[5],[1,4],[2],[3],[2,4]]
G2 = [[],[5],[1,4,5],[2,4],[],[4]]
G3 = [[],[3,5,6],[1],[2,4],[],[],[4]]
Petersen = [[],
  [2,5,6],[1,3,7],[2,4,8],[3,5,9],[1,4,10],
  [1,8,9],[2,9,10],[3,6,10],[4,6,7],[5,7,8]]

print("==== parcours G1")
largeur(G1, 1)
print("==== parcours G2")
largeur(G2, 1)
print("==== parcours G3")
largeur(G3, 1)
print("==== parcours Petersen")
largeur(Petersen, 1)


    
  
