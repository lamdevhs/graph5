
NotDone = Object()
Done = Object()

def largeur(G, i, Visite, traite, revisite):
  n = sommets(G)
  if Visite[i] != NotDone:
    return
  Visite[i] = Done
  revisite(i, i, i)
  File = [i]
  while len(File) != 0:
    head = File.pop(0)
    traite(head)
    for j in G[head]:
      if Visite[j] == Done:
        revisite(j, head, i)
      File.append(j)



    
  
