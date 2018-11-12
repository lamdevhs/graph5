from vect import *

def pcc(G, i):
  Dist = [-1 for i in range(len(G))]
  Visite = [0 for i in range(len(G))]
  Parent = [0 for i in range(len(G))]

  File = [i]
  Visite[i] = 1
  Dist[i] = 0
  Parent[i] = i
  while len(File) != 0:
    head = File.pop(0)
    for succ in G[head]:
      if Visite[succ] == 0: # on ne tient pas compte des revisites
        Visite[succ] = 1
        File.append(succ)
        Dist[succ] = Dist[head] + 1
        Parent[succ] = head
  print("====", Dist, Parent)
  return Dist, Parent


def plusCourtChemin(G,i):
  Pere = initVect(len(G), 0)
  profondeur = 0
  Dist = initVect(len(G), -1)
  NiveauEnCours = []
  ProchainNiveau = []
  Visite = initVect(len(G), 0)

  Pere[i] = i
  NiveauEnCours.append(i)
  Visite[i] = 1
  while not (len(NiveauEnCours) == 0 and len(ProchainNiveau) == 0):
    if len(NiveauEnCours) == 0:
      NiveauEnCours = ProchainNiveau
      ProchainNiveau = []
      profondeur += 1
    
    head = NiveauEnCours.pop(0)
    Dist[head] = profondeur
    for adj in G[head]:
      if Visite[adj] == 1:
        pass
      else:
        ProchainNiveau.append(adj)
        Visite[adj] = 1
        Pere[adj] = head
  return (Dist, Pere)

G = [[],[2],[1]] # non orienté, connexe, super simple
print("## Test G =", G)
print(plusCourtChemin(G,2) == pcc(G,2))

G2 = [[], [3], [4,3], [2,6,7], [8,5], [9], [2], [1,3], [], [1], [2]] # orienté, non fortement connexe, multigraphe

# représentation de l'arborescence de visite de G2
# pour un parcours largeur à partir du sommet 2:
#    2
#  4   3
# 8 5 6 7
#   9   1
# le sommet 10 n'est pas accessible à partir de 2
# vecteur des peres attendu :
#      sommets =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
pere_theorique = [0, 7, 2, 2, 2, 4, 3, 3, 4, 5,  0]
# vecteur des distances attendu :
#                  0 1 2 3 4 5 6 7 8 9 10
#      sommets =   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
dist_theorique = [-1, 3, 0, 1, 1, 2, 2, 2, 2, 3, -1]
resultat_theorique = (dist_theorique, pere_theorique)

print()
print()
print("## Test G2 =", G2)
resultat = plusCourtChemin(G2,2)
print()
print("Résultat final pour G2:", resultat)
print("Valeurs espérées :", resultat_theorique)
print("Concordance?", resultat == resultat_theorique)
print("Concordance2?", resultat == pcc(G2,2))
