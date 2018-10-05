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
Petersen = [[],
  [2,5,6],[1,3,7],[2,4,8],[3,5,9],[1,4,10],
  [1,8,9],[2,9,10],[3,6,10],[4,6,7],[5,7,8]]

# graphes orientes
oG1 = [[],[5], [1,4], [2], [3], [2,4]]
G1a = [[1,5], [2,1], [2,4], [3,2], [4,3], [5,2], [5,4]]
  # ^ G1 sous forme de listes d'aretes

oG2 = [[],[5],[1,4,5],[2,4],[],[4]]
oG3 = [[],[3,5,6],[1],[2,4],[],[],[4]]
