from vect import *

not_visited = 0
visited = 2
being_visited = 1
yes_cyclic = True
not_cyclic = False

def cyclicRec(G,i,Visite, prefix = " "):
  print(prefix + "Début de visite de", i)
  Visite[i] = being_visited
  for succ in G[i]:
    state = Visite[succ]
    if state == being_visited:
      # revisite d'un sommet en cours de visite
      # càd revisite d'un sommet de la branche en cours
      # càd arc arrière, càd cycle détecté
      # on casse alors la récursion pour finir le
      # vite possible
      print(prefix + "!!! cycle détecté: arc arrière de", i, "vers", succ)
      return yes_cyclic
      # on remarque que Visite n'a pas été mis à jour,
      # càd Visite[i] n'a pas été mis à "visited"
      # mais on s'en fout on a trouvé ce qu'on était
      # venu chercher

    elif state == not_visited:
      # si succ n'a pas encore été visité, on le visite
      result = cyclicRec(G,succ,Visite, prefix + " ")
      # une fois la viste de succ terminée, on vérifie
      # qu'un cycle n'a pas été détecté plus bas
      if result == yes_cyclic:
        return yes_cyclic
    else :
      # arc avant ou transverse, on n'a rien à faire
      print(prefix + "- arc avant ou transverse de", i, "vers", succ)
      
  # on n'oublie pas de mettre i à "visité" avant de le quitter,
  # pour ne plus y revenir
  Visite[i] = visited
  print(prefix + "Fin de visite de", i)
  return not_cyclic # on n'a pas trouvé de cycles jusque là

def sommets(G):
  return range(1,len(G))
      
def isCyclic(G):
  Visite = initVect(len(G), not_visited)
  for node in sommets(G):
    if Visite[node] == not_visited:
      print("Début parcours profondeur depuis", node)
      result = cyclicRec(G, node, Visite)
      if result == yes_cyclic:
        return yes_cyclic
      else:
        print("Fin parcours largeur depuis", node)

  return not_cyclic

G = [[],[3,4,6,5], [1], [4,2], [], [], [4]]
print("G est supposé cyclique. Vérif:", isCyclic(G))
G2 = [[],[3,4,6,5], [4], [4,2], [], [], [4]]
print("G2 est supposé non cyclique. Vérif:", isCyclic(G2))
