
NotDone = Object()
Done = Object()

# revisite(sommet, pere, ancetre)

def largeur(G, i, Visite, premiere_visite, revisite):
  n = sommets(G)
  ordreVisite = []
  if Visite[i] == Done:
    return ordreVisite
  Visite[i] = Done
  File = [i]
  while len(File) != 0:
    head = File.pop(0)
    premiere_visite(head)
    for j in G[head]:
      if Visite[j] == Done:
        revisite(j, head, i)
      else:
        File.append(j)
        ordreVisite.append(j)
        Visite[j] = Done
  return ordreVisite

def doNothing():
  pass

G1 = [[],[5],[1,4],[2],[3],[2,4]]


    
  
