from vect import *


def plusCourtChemin(G,i):
  # l'algorithme se base sur le parcours en largeur
  # a partir du sommet i

  # on va enregistrer l'arbre de visite dans un vecteur
  # des peres qui servira a retrouver les plus courts
  # chemins trouves
  Pere = initVect(len(G), 0)

  # on mémorise la profondeur atteinte dans l'arbre de visite à tout instant
  # on rappelle que l'arbre de visite formera une arborescente
  # donc une hiérarchie avec des niveaux qui correspondent aux
  # distances des sommets de l'arborescence au sommet i.
  profondeur = 0

  # pour chaque sommet visité, on enregistrera la profondeur
  # atteinte au moment de la premiere visite, ce qui donnera
  # la distance de ce sommet au sommet i
  # au début tout est à -1 (non accessible à partir de i)
  Dist = initVect(len(G), -1)
  
  # comme dans le parcours en largeur classique,
  # on utilise presque une file de sommets a traiter
  # mais cette fois on va en fait utiliser deux files
  # l'une contenant les sommets en cours de visite
  # dans le niveau de profondeur courant, l'autre que l'on
  # remplira avec les sommets du niveau inférieur
  # tout cela est nécessaire afin de savoir quand un niveau
  # est terminé, et donc quand est-ce que l'on doit augmenter
  # la profondeur
  NiveauEnCours = []
  ProchainNiveau = []

  # on a aussi besoin de verifier si on a deja visité
  # un sommet ou non auparavant, via le vecteur de visite:
  Visite = initVect(len(G), 0)

  # dans l'arborescence, i est son propre pere:
  Pere[i] = i

  # la premiere etape est de mettre le sommet i
  # en queue de file courante pour le traiter dans le corps de
  # l'algorithme
  NiveauEnCours.append(i)

  # on va partir du principe que des qu'un sommet est
  # entré dans une des files, alors on le marque comme visité
  # immédiatement

  # on doit donc marquer i comme visité
  Visite[i] = 1

  # Note: Dist[i] sera initialisé dans la boucle while, c.f. plus bas.

  print("Profondeur de départ:", profondeur)
  print("  niveau zéro:", NiveauEnCours)
  print("  Vecteur des Peres:", Pere)
  print("  Vecteur des Distances:", Dist)
  print("  Vecteur de Visite:", Visite)

  # la boucle while se termine des qu'a la fois le niveau en cours
  # est epuisé, et en plus il n'y a aucun sommet à traiter dans
  # le niveau de hiérarchie suivant
  while not (len(NiveauEnCours) == 0 and len(ProchainNiveau) == 0):
    # si le NiveauEnCours a ete completement traité,
    # on remplace NiveauEnCours par ProchainNiveau, et on
    # crée un nouveau ProchainNiveau, et bien sûr on incrémente
    # la profondeur parce qu'on change de niveau de hiérarchie
    # dans l'arborescence de visite
    if len(NiveauEnCours) == 0:
      NiveauEnCours = ProchainNiveau
      ProchainNiveau = []
      profondeur += 1
      print("Changement de niveau ; nouvelle profondeur:", profondeur)
      print("  Nouveau NiveauEnCours:", NiveauEnCours)
      print("  Vecteur des Peres:", Pere)
      print("  Vecteur des Distances:", Dist)
      print("  Vecteur de Visite:", Visite)
    
    # tant que la file courante n'est pas vide, on traite sa tete
    head = NiveauEnCours.pop(0)
    # pas besoin de modifier Visite[head]: par hypothese
    # c'est deja mis a 1
    
    # c'est le moment ideal pour enregistrer la profondeur
    # de l'element head, c'est a dire sa distance par rapport a i
    # on devra avoir par exemple dès le premier tour de boucle, Dist[i] = 0
    Dist[head] = profondeur
    # tous les elements qui font partie de NiveauEnCours sont a egale
    # distance de i, et cette distance vaut precisement "profondeur".
    # les elements de ProchainNiveau seront a distance "profondeur + 1"
    # de i, etc.
    
    # on va maintenant ajouter tous les sommets adjacents
    # de head a ProchainNiveau, sauf s'ils ont ete visités precedemment
    # en effet, les sommets non déjà visités adjacents à head
    # sont dans le niveau du dessous (plus profond == plus éloigné de i)
    # par rapport à celui de head (c'est à dire le niveau en cours)
    for adj in G[head]:
      if Visite[adj] == 1:
        # revisite, on ne fait rien
        pass
      else:
        # on met adj dans la file ProchainNiveau pour futur traitement
        ProchainNiveau.append(adj)
        # on marque adj comme officiellement visité
        Visite[adj] = 1
        # on enregistre la position de adj dans l'arbre de visite
        # ici représenté par le vecteur des peres, donc,
        # comme le père de adj dans l'arbre de visite est head,
        Pere[adj] = head
  
  # une fois la boucle while épuisée, on aura fini le parcours en largeur
  # de G a partir de i, et on retourne alors simplement Pere et Dist:
  return (Dist, Pere)

G = [[],[2],[1]] # non orienté, connexe, super simple
print("## Test G =", G)
print(plusCourtChemin(G,2))

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
