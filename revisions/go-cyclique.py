
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
      est_cyclique = go_isCyclic_rec(G, succ, visite)
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

