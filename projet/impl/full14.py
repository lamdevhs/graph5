from vect import *
import random

# Note: Tout le code exécutable de ce fichier est tout à la fin.

# ------------------------------------
# ------------------------------------
# AVANCEMENT DU PROJET
#
# Hopcroft-Karp a été codé, testé et vérifié.
#
# J'ai écrit une fonction pour créer des graphes biparti aléatoires
# et une autre qui s'arrange pour que le graphe biparti généré
# ne respecte pas la condition du théorème de hall, et donc qu'il
# n'admette pas de couplage parfait.
# Une méthode exhaustive bruteforce par backtracking a été écrite
# afin de vérifier que les solutions données par mon implémentation
# de Hopcroft-Karp sont optimales.
# Une petite fonction (check_matchingHK) dont l'appel a été commenté
# teste la cohérence des résultats entre la méthode HK et la méthode
# exhaustive.
# Elle tourne en boucle jusqu'à trouver un graphe aléatoire pour lequel mon
# implémentation de HK échouerait à trouver une méthode optimale,
# ce qui jusque là n'est jamais arrivé.
#
# J'ai aussi implémenté l'algorithme de couplage par
# chemins augmentant simple (celui en O(n^3)).
# Idem il y a une fonction qui vérifie sa cohérence par rapport à
# l'algorithme de recherche exhaustif.
#
# J'ai écrit un rapport présentant et prouvant le théorème de hall,
# celui de Berge et celui de Hopcroft-Karp, présentant l'algorithme
# de H.K., sa complexité, et la preuve de sa complexité.
#
# Il me faudrait encore polir un peu le rapport écrit, et un peu ce
# fichier aussi, cependant je ne pense pas nécessairement ajouter grand
# chose de plus que ce que j'ai déjà fait.


# ------------------------------------
# ------------------------------------
# CONSTANTES ET UTILITAIRES
Infinity = float("inf")

def interval (a, b):
  return list(range(a, b+1))


# ------------------------------------
# ------------------------------------
# CONTROLE DE LA VERBOSITÉ

print("Verbosité : juste tapez <entrer> pour la version PAS (trop) verbeuse,")
print("et n'importe quoi d'autre pour la version (très) verbeuse.")
if input("Faites votre choix: ") == '':
  print("Mode non verbeux")
  def verbose(*args):
    pass # don't print anything
else:
  print("Mode verbeux")
  def verbose(offset, *args): # offset: crée une indentation
    print(*([' '*offset] + list(args)))
  def verbose(*args): # offset: crée une indentation
    print(*args)


# == Fonction matchingHK
# Description: Construit un couplage maximum pour
# le graphe donné en input selon l'algorithme de
# Hopcroft-Karp.
# Input: (G, X)
# -- G = (V, E) avec V = (X u Y) est un graphe non orienté biparti
#    représenté par une liste d'adjacence.
# -- X: l'un des deux ensembles de sommets de G formant sa bipartition
# Output: (M, size)
# -- M: le couplage maximum construit par l'algorithme,
#    représenté par une liste d'entiers:
#       forall i,j in V :
#       --  M[i] = j  <==>  i est associé à j dans M,
#                           càd l'arête {i,j} est dans M
#       --  M[i] = 0  <==> i est libre dans M
# -- cardM: |M|
def matchingHK(G, X):
  M = initVect(len(G), 0)
  cardM = 0
  
  # parcours de M en largeur à partir de tous les sommets libres
  # de X, en s'arrêtant à la plus petite profondeur où l'on trouve
  # le premier chemin d'augmentation pour M.
  shortestLength, distance = BFS_shortestAugmentingPath(G, X, M)
  # ^ retourne la longueur du plus court chemin d'augmentation
  # pour M, et le vecteur des distances du parcours en largeur

  etape = 1
  # tant qu'on trouve des chemins d'augmentation:
  while shortestLength != Infinity:
    DFS_visited = initVect(len(G), False)
    # ^ vecteur des visites du DFS généralisé
    # il ne sera pas remis à zéro avant le prochain
    # tour de boucle: pas de revisite admise.

    # A partir de tous les sommets libres de X,
    # recherche par parcours profondeur d'un chemin
    # d'augmentation de M de longueur shortestLength.
    # Tous ces chemins d'augmentations doivent être deux à
    # deux disjoints. Il suffit pour cela de refuser toute revisite.
    # Chaque chemin trouvé est aussitôt utilisé pour augmenter M lors
    # de la remontée de la pile d'exécution.
    for x in X:
      if M[x] == 0: # si x est libre
        # recherche d'un chemin d'augmentation de longueur shortestLength
        # à partir de x, qui ne passe pas par un des sommets déjà visités.
        verbose(">>> Début de DFS à partir de", x)
        found = DFS_augmentM(x, G, M, DFS_visited, distance, shortestLength)
        verbose(">>> Fin de DFS à partir de", x)
        if found:
          # un chemin d'augmentation pour M a été trouvé
          cardM += 1 # |M| a augmenté d'une arête
    
    # on recommence le processus depuis le début
    print("[HK] Couplage M à l'étape", etape, ":", M)
    etape += 1
    shortestLength, distance = BFS_shortestAugmentingPath(G, X, M)

  # il n'existe plus de chemins d'augmentation pour M dans G,
  # donc d'après le Théorème de Berge, M est maximum.
  return (M, cardM)


# == Fonction BFS_shortestAugmentingPath
# Input:
# -- G : graphe biparti
# -- X : une des composantes de la bipartition de G,
# -- M : un couplage quelconque pour G
# Parcours profondeur de G à partir des sommets de X libres pour M,
# en alternant une arête dans M et un arête pas dans M à chaque
# traversée d'un sommet. Les sommets de profondeur paire
# seront l'extrémité de début d'une arête pas dans M,
# ceux de profondeur impaire seront l'extrémité de début d'une
# arête de M.
# On s'arrête à la profondeur où l'on trouve le premier chemin
# d'augmentation pour M (le plus cours donc, puisque c'est un BFS).
# Output:
# -- shortestLength: longueur du plus petit chemin d'augmentation de M
# -- distance:       vecteur des distances du parcours profondeur.
def BFS_shortestAugmentingPath(G, X, M):
  shortestLength = Infinity

  distance = initVect(len(G), Infinity)
  # distance: de chaque sommet, dans l'arbre de parcours
  # par rapport aux racines (points de départ) de l'arbre.
  # càd tous les sommets libres (par rapport à M) de X
  
  visited = initVect(len(G), False)
  # ^ pas de revisite dans ce BFS
  
  queue = []
  # initialisation: mettre toutes les racines
  # dans la file: les sommets libres de X.
  for x in X:
    if M[x] == 0: # x est libre pour le couplage M
      distance[x] = 0
      visited[x] = True
      queue.append(x)
  
  while len(queue) != 0:
    verbose("file =", queue)
    head = queue.pop(0)
    verbose("défilement de head =", head)
    d = distance[head]
    verbose("distance de head =", d)
    if distance[head] < shortestLength:
      # ^ cette condition permet d'arrêter le parcours
      # largeur prématurément au premier niveau de profondeur
      # où l'on a trouvé un chemin d'augmentation pour M
      verbose("exploration à partir de head")
      if d % 2 == 0:
        verbose("niveau de profondeur pair")
        # head est dans X.
        # Pair ==> les arêtes à traverser ici doivent
        # être des arêtes qui n'appartiennent *pas* à M.
        # Si head est libre, càd M[head] == 0, alors
        # parcourir tous ses voisins non visités.
        # Si head n'est pas libre, son parent dans l'arbre de
        # parcours est M[head], donc a déjà été visité.
        # Dans les deux cas: il suffit de visiter tous les voisins
        # de head non visités.
        for v in G[head]:
          verbose("voisin de head v =", v)
          if not visited[v]:
            # alors nécessairement, v != M[head]
            # donc (head, v) n'est pas dans M
            verbose("visite de v")
            distance[v] = distance[head] + 1
            verbose("distance[v] =", distance[v])
            visited[v] = True
            queue.append(v)
            if M[v] == 0:
              # v est dans Y, et libre
              verbose("!!! shortest path found")
              # on a trouvé un plus petit chemin d'augmentation
              shortestLength = distance[v]
      else: # d == 1 mod 2: niveau de profondeur impair
        verbose("niveau de profondeur impair")
        # head est dans Y.
        # la prochaine arête traversée doit être dans M.
        # la seule candidate est donc {head, M[head]}
        # si M[head] == 0, alors head est l'extrémité d'un chemin
        # d'augmentation de M, donc distance[head] >= shortestLength:
        # contradiction avec la condition if ci-dessus.
        # Donc M[head] n'est pas nul.
        v = M[head]
        verbose("voisin = M[head] =", v)
        if not visited[v]:
          verbose("visite de v")
          distance[v] = distance[head] + 1
          verbose("distance[v] =", distance[v])
          visited[v] = True
          queue.append(v)
  return (shortestLength, distance)

# Parcours profondeur récursif. Chaque visite d'un sommet u
# à partir d'un sommet v doit être tel que
# distance[u] == distance[v] + 1, et:
# -- si distance[v] pair: v dans X, donc {v,u} ne doit pas être dans M
# -- sinon: {v,u} doit être dans M
# Pas de revisite autorisée durant tout le parcours profondeur
# généralisé, car les chemins doivent être deux à deux disjoints.
# On cherche un chemin d'augmentation de longueur <= shortestLength.
# Donc, on s'arrête dès que l'on est trop profond ou bien dès
# qu'on a trouvé le chemin qu'on cherchait.
# Output
# -- booléen: True si on a trouvé un chemin d'augmentation
#    pour M de longueur plus petite que shortestLength.
def DFS_augmentM(v, G, M, visited, distance, shortestLength):
  verbose("visite de", v)
  visited[v] = True
  d = distance[v]
  verbose("distance[v] =", d)
  if d == shortestLength:
    verbose("trop profond: backtracking")
    return False # pas de bon chemin trouvé
  if d % 2 == 0:
    verbose("niveau de profondeur paire")
    # il faut explorer des arêtes qui ne sont pas dans M
    for w in G[v]:
      verbose("voisin  w =", w)
      if not visited[w] and distance[w] == d + 1:
        # si M[v] == w, alors v n'est pas libre, son parent
        # dans l'arbre de parcours DFS doit être w, donc
        # w a déjà été visité: contradiction. Donc M[v] != w.
        # Donc (v, w) n'est pas dans M.
        verbose("w est acceptable")
        if M[w] == 0:
          verbose("w est libre: un plus court chemin d'augmentation trouvé")
          visited[w] == True
          found = True
        else:
          # récursion
          verbose("récursion à partir de w")
          found = DFS_augmentM(w, G, M, visited, distance, shortestLength)
          verbose("remontée: v =", v)
        if found:
          # we do a symetric difference between M
          # and the path we found, so here
          # we create the edge (v,w) in M
          verbose("Augmentation de M")
          M[v] = w
          M[w] = v
          return found
  else: # d impair
    verbose("niveau de profondeur impair")
    # l'arête suivante doit être dans M, donc
    # doit être {v,M[v]},
    # sauf si v est libre pour M: mais c'est impossible
    # par hypothèse de récursion (si v était libre on aurait
    # déjà fini ce parcours en cours.
    w = M[v]
    verbose("w = M[v] =", w)
    if not visited[w] and distance[w] == d + 1:
      verbose("w = M[v] is acceptable, récursion")
      found = DFS_augmentM(w, G, M, visited, distance, shortestLength)
      verbose("remontée: v =", v)
      if found:
        verbose("chemin trouvé précédemment, augmentation passive de M")
        # on fait un différence symétrique entre M
        # et le chemin trouvé, et ici l'arête en cours est
        # {v,w} is in M, donc on ne fait rien, et on laisse
        # les arêtes d'avant et d'après séparer v et w pour M
        return found
  verbose("return False: backtrack sans succès")
  return False # pas de chemin d'augmentation trouvé


# ------------------------------------
# ------------------------------------
# GÉNÉRATION DE GRAPHES ALÉATOIRES

def randomBool(): 
  return bool(random.getrandbits(1))

# V = {1,...,|X|} union {|X|+1,..., n}
# |V| = n and y = |Y| = n - |X|
def randomBipartite(n, cardX):
  G = initVectList(n+1)
  cardY = n - cardX
  X = interval(1, cardX)
  Y = interval(cardX + 1, n)
  for x in X:
    Vx = G[x]
    while len(Vx) == 0: # nobody wants to be alone
      for y in Y:
        if randomBool():
          Vx.append(y)
          G[y].append(x)
  # on s'assure que les sommets de Y
  # ne sont pas isolés 
  for y in Y:
    if len(G[y]) == 0:
      x = random.randint(1,cardX)
      G[x].append(y)
      G[y].append(x)
  return G

# Crée un graphe aléatoire G = (X u Y, E)
# avec E subset X x Y,
# n = |X u Y| et n/2 = |X| = |Y|
# et tel qu'il existe k < |X| tel
# que B = {1, ..., k} subset X
# soit tel que |B| = k > |V(B)|
# En d'autres termes, G ne respecte pas
# la condition de Hall, n'admet donc pas
# de couplage parfait.
# Condition d'entrée: halfn >= 3
def randomImperfectBipartite(halfn):
  assert(halfn >= 3)
  n = halfn*2
  G = initVectList(n+1)
  cardX = halfn
  cardY = halfn
  Y = interval(cardX + 1, n)
  k = random.randint(2,cardX-1) # 2 <= k < |X|
  B = interval(1, k)
  maxVoisinsDeB = random.randint(1,k-1)
  # k > maxVoisinsDeB >= |V(B)|
  # tous les voisins de B doivent être dans
  # {|X| + 1, |X| + maxVoisinsDeB} subset Y
  voisinsPossiblesDeB = interval(cardX + 1, cardX + maxVoisinsDeB)
  # cela assurera |B| = k > |V(B)|
  for x in B:
    Vx = G[x] # voisinage de x
    while len(Vx) == 0:
      # on ne veut pas de sommets isolés
      for y in voisinsPossiblesDeB:
        # on associe ou non x et y aléatorement
        if randomBool():
          Vx.append(y)
          G[y].append(x)
  # pour les autres éléments de X
  # il n'y a pas de restrictions
  # sur leurs voisins
  X_minus_B = interval(k+1, cardX)
  for x in X_minus_B:
    Vx = G[x]
    while len(Vx) == 0: # nobody wants to be alone
      for y in Y: # on associe ou non x et y aléatorement
        if randomBool():
          Vx.append(y)
          G[y].append(x)
  # on s'assure enfin qu'aucun sommet de Y n'est vide:
  for y in Y:
    if len(G[y]) == 0:
      G[k+1].append(y)
      G[y].append(k+1)
      # k + 1 <= |X| donc k+1 est dans X\B
      # c'est pour ça qu'il faut que
      # halfn = |X| >= 3.
  return G


# ------------------------------------
# ------------------------------------
# ALGORITHME EXHAUSTIF BRUTEFORCE
# Pour vérifier les résultats de Hopcroft-Karp

# calcule le cardinal d'un couplage
# en nombre d'arêtes
def cardOfM(M):
  card = len(M)
  for v in M:
    if v == 0: # si v est libre dans M
      card -= 1
  return card//2

# Cet algorithme est volontairement
# inefficace et peu optimisé, mais 
# suffisament clair pour être trustworthy.
# Input:
# -- i = curseur sur les éléments de X
# Output: (par paramètre modifié)
# -- maxCardM: une liste d'un élément commune à
#   tous les appels récursifs, contenant à la fin
#   la taille d'un couplage maximum pour G.
# Principe:
#   Pour tout x dans X, on explore l'option de l'associer
#   à n'importe quel élément de G[x] disponible, et
#   aussi l'option de le laisser tout seul.
def exhaustive_rec(i, G, X, M, maxCardM):
  if i == len(X):
    cardM = cardOfM(M)
    maxCardM[0] = max(cardM, maxCardM[0])
    return
  else:
    x = X[i]
    for y in G[x]:
      if M[y] == 0:
        # y est libre
        M[y] = x
        M[x] = y
        exhaustive_rec(i + 1, G, X, M, maxCardM)
        M[y] = 0 # unmatch y
        M[x] = 0 # unmatch x
    #
    # on explore finalement l'option de laisser x libre
    exhaustive_rec(i + 1, G, X, M, maxCardM)

# initialisation de la récursion
def exhaustive(G, X):
  M = initVect(len(G), 0)
  maxCardM = [0]
  exhaustive_rec(0, G, X, M, maxCardM)
  return maxCardM[0]



# ------------------------------------
# ------------------------------------
# ALGORITHME DES CHEMINS D'AUGMENTATION
# (la version simple en O(n^3))

def simpleMatching(G, X):
  M = initVect(len(G), 0)
  cardM = 0
  n = len(G) - 1
  cardX = len(X)
  cardY = n - cardX
  boundary = min(cardX, cardY)
  # ^ forcément cardM <= boundary

  etape = 1
  # tant qu'on trouve des chemins d'augmentation:
  while cardM != boundary and DFS_findOnePath(G,X,M) != False:
    cardM += 1
    print("[SIMPLE] Couplage M à l'étape", etape, ":", M)
    etape += 1
  # il n'existe plus de chemins d'augmentation pour M dans G,
  # donc d'après le Théorème de Berge, M est maximum.
  return (M, cardM)
  
def DFS_findOnePath(G,X,M):
  for x in X:
    if M[x] == 0:
      visited = initVect(len(G), False)
      found = DFS_findOnePath_rec(x, True, G, M, visited)
      if found:
        return found
  return False
  # impossible de trouver un chemin d'augmentation pour M
    

def DFS_findOnePath_rec(v, isInX, G, M, visited):
  verbose("visite de", v)
  visited[v] = True
  if isInX: # == v in X
    verbose("niveau de profondeur paire")
    # il faut explorer des arêtes qui ne sont pas dans M
    for w in G[v]:
      verbose("voisin  w =", w)
      if not visited[w]:
        # si M[v] == w, alors v n'est pas libre, son parent
        # dans l'arbre de parcours DFS doit être w, donc
        # w a déjà été visité: contradiction. Donc M[v] != w.
        # Donc (v, w) n'est pas dans M.
        verbose("w est acceptable")
        if M[w] == 0:
          verbose("w est libre: un plus court chemin d'augmentation trouvé")
          visited[w] == True
          found = True
        else:
          # récursion
          verbose("récursion à partir de w")
          found = DFS_findOnePath_rec(w, not isInX, G, M, visited)
          verbose("remontée: v =", v)
        if found:
          # we do a symetric difference between M
          # and the path we found, so here
          # we create the edge (v,w) in M
          verbose("Augmentation de M")
          M[v] = w
          M[w] = v
          return found
  else: # v not in X donc v in Y
    verbose("niveau de profondeur impair")
    # l'arête suivante doit être dans M, donc
    # doit être {v,M[v]},
    # sauf si v est libre pour M: mais c'est impossible
    # par hypothèse de récursion (si v était libre on aurait
    # déjà fini ce parcours en cours.
    w = M[v]
    verbose("w = M[v] =", w)
    if not visited[w]:
      verbose("w = M[v] is acceptable, récursion")
      found = DFS_findOnePath_rec(w, not isInX, G, M, visited)
      verbose("remontée: v =", v)
      if found:
        verbose("chemin trouvé précédemment, augmentation passive de M")
        # on fait un différence symétrique entre M
        # et le chemin trouvé, et ici l'arête en cours est
        # {v,w} is in M, donc on ne fait rien, et on laisse
        # les arêtes d'avant et d'après séparer v et w pour M
        return found
  verbose("return False: backtrack sans succès")
  return False # pas de chemin d'augmentation trouvé


# ------------------------------------
# ------------------------------------
# FONCTIONS DE TESTS

def test_matchingHK(G, cardX):
  print("---- Test de matchingHK, G =", G)
  X = interval(1,cardX) # X = {1,..., |X|}
  #input("Tapez <entrer> pour lancer l'algo sur G")
  M, cardM = matchingHK(G, X)
  print("Couplage maximum trouvé:", M)
  print("Taille du couplage: |M| =", cardM)


# vérifier manuellement que les
# graphes générés aléatoirement sont
# bien formés (pas de sommets isolés, etc)
# et que ceux qui sont censés 
def test_random_generation():
  for n in range(3,10):
    test = randomImperfectBipartite(n)
    print(test)
  for n in range(3,10):
    test = randomBipartite(n, n//2)
    print(test)
# test_random_generation()

def check_algo(algo):
  while True:
    for n in range(3, 12):
      G = randomImperfectBipartite(n)
      X = interval(1,n)
      bruteMax = exhaustive(G, X)
      M, algoMax = algo(G, X)
      ok = bruteMax == algoMax
      print(n, bruteMax, algoMax, ok)
      if not ok:
        print(G, M)
        raise Exception("the Checking found a failure")

# Test de simpleMatching
def test_simple(G, cardX):
  print("---- Test de simpleMatching, G =", G)
  X = interval(1,cardX) # X = {1,..., |X|}
  #input("Tapez <entrer> pour lancer l'algo sur G")
  M, cardM = simpleMatching(G, X)
  print("Couplage maximum trouvé:", M)
  print("Taille du couplage: |M| =", cardM)
  



# ------------------------------------
# ------------------------------------
# CODE EXECUTABLE

G1 = [[], [7,8,11],[7,10],[8],[9,11],[9],[9,12], # X
          [1,2],[1,3],[4,5,6],[2],[1,4],[6]] # Y
G2 = [[], [6,7],[6,10],[8,9],[6,10],[7,9],
          [1,2,4],[1,5],[3],[3,5],[2,4]] # example des marriages
G3 = [[], [4], [4], [4, 5, 6], [1, 2, 3], [3], [3]]

# test de Hopcroft-Karp sur G1 et G2:
test_matchingHK(G1, 6)
test_matchingHK(G2, 5)
test_matchingHK(G3, 3)

test_simple(G1, 6)
test_simple(G2, 5)
test_simple(G3, 3)

#check_algo(matchingHK)
  # ^ Cette appel de fonction construit des graphes aléatoires
  # ne respectant pas la condition de Hall, et vérifie
  # que le plus grand couplage trouvé par Hopcroft-Karp
  # est aussi grand que le plus grand trouvé par
  # algorithme exhaustif.
  # Cette fonction ne s'arrête jamais, sauf si elle tombe sur un
  # exemple pour lequel H-K échoue à être optimal.
  # D'expérience, elle ne s'est jamais arrêté toute seule.

#check_algo(simpleMatching)
  # ^ même chose pour l'algorithme simple par chemins
  # d'augmentation non optimisé.

