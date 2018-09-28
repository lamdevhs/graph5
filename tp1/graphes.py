from TP1GraphesNonOrientes import kuratowski

# graphes non orientes
G2 = [[],[2,5,5], [1,3,4,4], [2,3,4], [2,2,3,5], [1,1,4]]
aG2 = [[1,2],[1,5],[1,5],[2,3],[2,4],[2,4],[3,3],[3,4],[4,5]]
  # ^ G2 sous forme de listes d'aretes

K3 = kuratowski(3)
K4 = kuratowski(4)
K5 = kuratowski(5)
K6 = kuratowski(6)
K7 = kuratowski(7)

# graphes orientes
G1 = [[],[5], [1,4], [2], [3], [2,4]]
aG1 = [[1,5], [2,1], [2,4], [3,2], [4,3], [5,2], [5,4]]
  # ^ G1 sous forme de listes d'aretes
