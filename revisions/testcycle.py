from vect import *

not_visited = 0
visited = 2
being_visited = 1
yes_cyclic = True
not_cyclic = False

def cyclicRec(G,i,Visite, prefix = " "):
  Visite[i] = being_visited
  for succ in G[i]:
    state = Visite[succ]
    if state == being_visited:
      return yes_cyclic
    elif state == not_visited:
      result = cyclicRec(G,succ,Visite, prefix + " ")
      if result == yes_cyclic:
        return yes_cyclic
    else :
      pass
  Visite[i] = visited
  return not_cyclic # on n'a pas trouvé de cycles jusque là

def sommets(G):
  return range(1,len(G))
      
def isCyclic(G):
  Visite = initVect(len(G), not_visited)
  for node in sommets(G):
    if Visite[node] == not_visited:
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

# graphe cyclique: reviste arrière est signe inévitable et infaillible de cycle
# pour savoir que c'est un arc arrière, rien ne vaut un parcours profondeur
# trois etats pour vecteur visite: 0 = non visité, 1 = en cours de visite, 2 = visite terminée
# généralisé car un cycle peut etre caché n'importe où

def go_isCyclic_rec(G,i, Visite):
  Visite[i] = 1 # debut visite
  for succ in G[i]:
    if Visite[succ] == 1: # revisite d'un sommet en cours de visite
      # arc arrière, donc cycle détecté, on retourne true
      return True # G est cyclique
    elif Visite[succ] == 0:  # non visité
      est_cyclique = go_isCyclic_rec(G, succ, Visite)
      if est_cyclique:
        return est_cyclique # on casse la recursion et on remonte avec l'info
  Visite[i] = 2 # fin de visite
  return False # on n'a pas trouvé de cycles jusque là si on arrive à cette instruction

def go_isCyclic(G):
  Visite = [0 for i in range(len(G))]
  for i in range(1,len(G)):
    if Visite[i] == 1:
      continue
    est_cyclique = go_isCyclic_rec(G, i, Visite)
    if est_cyclique:
      return est_cyclique # on casse la boucle et on remonte avec l'info

  return False # G n'est pas cyclique

G = [[],[3,4,6,5], [1], [4,2], [], [], [4]]
print("G est supposé cyclique. Vérif:", go_isCyclic(G))
G2 = [[],[3,4,6,5], [4], [4,2], [], [], [4]]
print("G2 est supposé non cyclique. Vérif:", go_isCyclic(G2))
