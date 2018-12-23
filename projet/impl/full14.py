from vect import *
import random

# Note: Tout le code exécutable de ce fichier se trouve tout à la fin.

# Afin de conserver la lisibilité du code, certains
# commentaires sont placés après la fonction commentée,
# et sont référencés dans la fonctions par la notation
# <1>, <2>, etc.

# Les messages de verbosité qui étaient dans la
# version remise le 14 dec ont été retirés.

# ------------------------------------
# ------------------------------------
# CONSTANTES ET UTILITAIRES
Infinity = float("inf")

def interval (a, b):
  return list(range(a, b+1))



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
  etape = 1
  shortestLength, distance = BFS_shortestAugmentingPath(G, X, M)
  # ^ commentaire <1>

  # tant qu'on trouve des chemins d'augmentation:
  while shortestLength != Infinity:
    DFS_visited = initVect(len(G), False)
    # ^ commentaire <2>
    for x in X: # commentaire <3>
      if M[x] == 0: # si x est libre
        # commentaire <4>
        found = DFS_augmentM(x, G, M, DFS_visited,
            distance, shortestLength)
        if found:
          # un chemin d'augmentation pour M a été trouvé
          cardM += 1 # |M| a augmenté d'une arête
    #
    # on recommence le processus depuis le début:
    print("[HK] Couplage M à l'étape", etape, ":", M)
    etape += 1
    shortestLength, distance = BFS_shortestAugmentingPath(G, X, M)
  #
  # il n'existe plus de chemins d'augmentation pour M dans G,
  # donc d'après le Théorème de Berge, M est maximum.
  return (M, cardM)

# <1> parcours de M en largeur à partir de tous les sommets libres
# de X, en s'arrêtant à la plus petite profondeur où l'on trouve
# le premier chemin d'augmentation pour M.
# Retourne la longueur du plus court chemin d'augmentation
# pour M, et le vecteur des distances du parcours en largeur

# <2> vecteur des visites du DFS généralisé
# il ne sera pas remis à zéro avant le prochain
# tour de boucle: pas de revisite admise.

# <3> A partir de tous les sommets libres de X,
# recherche par parcours profondeur d'un chemin
# d'augmentation de M de longueur shortestLength.
# Tous ces chemins d'augmentations doivent être deux à
# deux disjoints. Il suffit pour cela de refuser toute revisite.
# Chaque chemin trouvé est aussitôt utilisé pour augmenter M lors
# de la remontée de la pile d'exécution.

# <4> recherche d'un chemin d'augmentation de longueur shortestLength
# à partir de x, qui ne passe par aucun des sommets déjà visités.



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
  # ^ distance: de chaque sommet, dans l'arbre de parcours
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
    head = queue.pop(0)
    d = distance[head]
    if distance[head] < shortestLength:
      # ^ cette condition permet d'arrêter le parcours
      # largeur prématurément au premier niveau de profondeur
      # où l'on a trouvé un chemin d'augmentation pour M
      if d % 2 == 0:
        # commentaire <5>
        for v in G[head]:
          if not visited[v]:
            # alors nécessairement, v != M[head]
            # donc (head, v) n'est pas dans M
            distance[v] = distance[head] + 1
            visited[v] = True
            queue.append(v)
            if M[v] == 0:
              # v est dans Y, et libre
              # on a trouvé un plus petit chemin d'augmentation
              shortestLength = distance[v]
      else: # d == 1 mod 2: niveau de profondeur impair
        # commentaire <6>
        v = M[head]
        if not visited[v]:
          distance[v] = distance[head] + 1
          visited[v] = True
          queue.append(v)
  return (shortestLength, distance)

# <5> Profondeur paire, donc head est dans X,
# et les arêtes à traverser à partir d'ici doivent
# être des arêtes qui n'appartiennent *pas* à M.
# Si head est libre, càd M[head] == 0, alors
# parcourir tous ses voisins non visités.
# Si head n'est pas libre, son parent dans l'arbre de
# parcours est M[head], donc a déjà été visité.
# Dans les deux cas: il suffit de visiter tous les voisins
# de head non visités.

# <6> Profondeur impaire, donc head est dans Y,
# et la prochaine arête traversée doit être dans M.
# La seule candidate est donc {head, M[head]}.
# Si cette arête n'est pas dans M, càd si M[head] == 0,
# alors head est libre pour M, donc est l'extrémité d'un chemin
# d'augmentation de M, donc distance[head] >= shortestLength:
# contradiction avec la condition `if` ci-dessus :
#    ```if distance[head] < shortestLength:```
# Donc head n'est pas libre, et M[head] n'est pas nul.



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
#    pour M.
def DFS_augmentM(v, G, M, visited, distance, shortestLength):
  visited[v] = True
  d = distance[v]
  if d == shortestLength:
    return False # pas de bon chemin trouvé
  if d % 2 == 0:
    # il faut explorer des arêtes qui ne sont pas dans M
    for w in G[v]:
      if not visited[w] and distance[w] == d + 1:
        # commentaire <7>
        if M[w] == 0:
          visited[w] == True
          found = True
        else:
          # récursion
          found = DFS_augmentM(w, G, M, visited, distance, shortestLength)
        if found:
          # commentaire <8>
          M[v] = w
          M[w] = v
          return found
  else: # d impair
    # commentaire <9>
    w = M[v]
    if not visited[w] and distance[w] == d + 1:
      found = DFS_augmentM(w, G, M, visited, distance, shortestLength)
      if found:
        # commentaire <10>
        return found
  return False # pas de chemin d'augmentation trouvé


# <7> si M[v] == w, alors v n'est pas libre, son parent
# dans l'arbre de parcours DFS doit être w, donc
# w a déjà été visité: contradiction. Donc M[v] != w.
# Donc (v, w) n'est pas dans M.

# <8> on fait la différence symétrique entre M
# et le chemin trouvé, donc ici
# on ajoute l'arête (v,w) à M, et on sépare donc
# éventuellement v et/ou w de leurs précédents partenaires.

# <9> l'arête suivante doit être dans M, donc
# doit être {v,M[v]},
# sauf si v est libre pour M: mais c'est impossible
# par hypothèse de récursion (si v était libre on aurait
# déjà fini ce parcours en cours.)

# <10> on fait un différence symétrique entre M
# et le chemin trouvé, et ici l'arête en cours est
# {v,w} is in M, donc on ne fait rien, et on laisse
# les arêtes d'avant et d'après séparer v et w pour M


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
# /!\ Condition sur la valeur d'entrée:
# il faut que halfn >= 3
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
# suffisament clair pour être digne de confiance.
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
def exhaustive_rec(i, G, X, M, cardM, maxCardM):
  if i == len(X): # condition d'arret
    maxCardM[0] = max(cardM, maxCardM[0])
    return
  else:
    x = X[i]
    for y in G[x]:
      if M[y] == 0:
        # y est libre
        M[y] = x
        M[x] = y
        exhaustive_rec(i + 1, G, X, M, cardM + 1, maxCardM)
        M[y] = 0 # unmatch y
        M[x] = 0 # unmatch x
    #
    # on explore finalement l'option de laisser x libre
    exhaustive_rec(i + 1, G, X, M, cardM, maxCardM)

# initialisation de la récursion
def exhaustive(G, X):
  M = initVect(len(G), 0)
  maxCardM = [0]
  exhaustive_rec(0, G, X, M, 0, maxCardM)
  return maxCardM[0]



# ------------------------------------
# ------------------------------------
# ALGORITHME DES CHEMINS D'AUGMENTATION
# Recherche de couplage maximum en O(n^3)

def simpleMatching(G, X):
  M = initVect(len(G), 0)
  cardM = 0
  n = len(G) - 1
  cardX = len(X)
  cardY = n - cardX
  boundary = min(cardX, cardY)
  # ^ forcément, le cardinal du couplage maximum
  # sera <= boundary

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
    

# Cette fonction est très similaire à la fonction DFS_augmentM
# ci-dessus, qui est utilisée dans l'algorithme Hopcroft-Karp.
# Les commentaires sur le code sont donc les mêmes.
def DFS_findOnePath_rec(v, isInX, G, M, visited):
  visited[v] = True
  if isInX: # == v in X
    # il faut explorer des arêtes qui ne sont pas dans M
    for w in G[v]:
      if not visited[w]:
        # commentaire <7>
        if M[w] == 0:
          visited[w] == True
          found = True
        else:
          # récursion
          found = DFS_findOnePath_rec(w, not isInX, G, M, visited)
        if found:
          # commentaire <8>
          M[v] = w
          M[w] = v
          return found
  else: # v not in X donc v in Y
    # commentaire <9>
    w = M[v]
    if not visited[w]:
      found = DFS_findOnePath_rec(w, not isInX, G, M, visited)
      if found:
        # commentaire <10>
        return found
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


# vérifier manuellement (à l'oeil nu) que les
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
 # ^ graphe d'example des marriages
 # X = {1,...,6} = {Paris,...,Rodrigue}
 # Y = {7,...,12} = {Hélène,...,Chimène}

G2 = [[], [6,7],[6,10],[8,9],[6,10],[7,9], # X
          [1,2,4],[1,5],[3],[3,5],[2,4]] # Y
 # ^ graphe de l'image jointe au projet
 # X = {1,...,5} = {u0,...,u4}
 # Y = {6,...,10} = {v0,...,v4}

G3 = [[], [4], [4], [4, 5, 6], [1, 2, 3], [3], [3]]
 # Un graphe qui ne respecte pas la condition du théorème de hall

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
  # d'augmentation (celui en O(n^3)).

