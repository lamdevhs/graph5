

def pcc(G, i):
  Dist = [0 for i in range(len(G))]
  Visite = [0 for i in range(len(G))]
  Parent = [-1 for i in range(len(G))]

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
  return Dist, Parent
