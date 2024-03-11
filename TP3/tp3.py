#!/usr/bin/env python3

import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

import random
from time import process_time as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")


############################################################
# Exercice 1.1
#
# Tri selection
#

def triSelection(T):
    for i in range(len(T)):
        min = i
        for j in range(i+1, len(T)):
            if T[j] < T[min]:
                min = j
        T[i], T[min] = T[min], T[i]
    return T

############################################################
# Exercice 1.2
#
# randomPerm prend en paramètre un entier n et renvoie une
# permutation aléatoire de longueur n dont l'algorithme s'appuie
# sur le tri sélection
#

def randomPerm(n):
    T = [i+1 for i in range(n)]
    for i in range(len(T)):    
        index = random.randint(i, len(T)-1)
        T[i], T[index] = T[index], T[i]
    return T

############################################################
# Exercice 1.3
#
# testeQueLaFonctionTrie prend en paramètre une fonction de
# tri f et l’applique sur des permutations aléatoires de
# taille i variant de 2 à 100 et vérifie que le résultat est
# un tableau trié
#

def testeQueLaFonctionTrie(f):
    for i in range(2, 101):
        T = randomPerm(i)
        T2 = T.copy()
        T2 = f(T2)
        for j in range(i-1):
            if T2[j] > i or T2[j] > T2[j+1]:
                print("Test Failed!!!")
                print("\tavant le tri: " + str(T))
                print("\tapres le tri: " + str(T2) + "\n")
                return False
        #print("Test passed: ")
        #print("\tavant le tri: " + str(T))
        #print("\tapres le tri: " + str(T2) + "\n")
    #print("\n  ____________________________________________________ Fin teste fonction tri " + f.__name__ + " ______________________________________________________\n\n")
    return True

############################################################
# Exercice 1.4
#
# randomTab prend des entiers n, a et b et renvoie un tableau
# aléatoire de taille n contenant des entiers compris entre
# les bornes a et b.

def randomTab(n,a,b):
    T = [0]*n
    for i in range(n):
        T[i] = random.randint(a, b)
    return T

############################################################
# Exercice 1.5
#
# derangeUnPeu prend des entiers n, k et un booléen rev et
# effectue k échanges entre des positions aléatoires sur la
# liste des entiers de 1 à n si rev vaut False ou sur la
# liste des entiers n à 1 si rev vaut True.
#

def derangeUnPeu(n,k,rev):
    T = [ n - i for i in range(n) ] if rev else [ i + 1 for i in range(n) ]
    for i in range(k):
        p, q = random.randint(1, n-1), random.randint(1, n-1)
        T[p], T[q] = T[q], T[p]
    return T

############################################
# Exercice 2.1
#
# Trois variantes du tri par insertion L échanges successifs,
# insertion directe à la bonne position, et avec recherche
# dichotomique de la position
#

def triInsertionEchange(T):
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j-1] <= T[j]: break
            T[j-1], T[j] = T[j], T[j-1]
    return T

def triInsertionRotation(T):
    for i in range(1, len(T)):
        for j in range(i+1):
            if T[i] < T[j]: break
        for k in range(j, i):
            T[i], T[k] = T[k], T[i]
    return T

def recherche_dicho(T, x, begin = 0, end = None):
    if end == None:
        end = len(T) - 1

    if begin == end:
        if T[begin] > x:
            return begin
        else:
            return begin + 1
        
    if begin > end:
        return begin
    
    mid = (begin + end) // 2
    if T[mid] < x:
        return recherche_dicho(T, x, mid+1, end)
    elif T[mid] > x:
        return recherche_dicho(T, x, begin, mid-1)
    else:
        return mid


def triInsertionRapide(T):
    for i in range(1, len(T)):
        x = T[i]
        j = recherche_dicho(T, x, 0, i-1)
        T = T[:j] + [x] + T[j:i] + T[i+1:]
    return T

############################################################
# Exercice 2.2
#
# Tri fusion
#

def fusion(T1,T2):
    i, j = 0, 0
    res = []
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1

    while i < len(T1):
        res.append(T1[i])
        i += 1

    while j < len(T2):
        res.append(T2[j])
        j += 1
    
    return res

def triFusion(T, deb=0, fin=None) :
    if fin == None:
        fin = len(T) - 1
    
    if fin > deb:
        mid = (deb + fin) // 2
        L = triFusion(T, deb, mid)
        R = triFusion(T, mid+1, fin)
        return fusion(L, R)
    else:
        return T[deb:fin+1]



############################################################
# Exercice 2.3
#
# Tri à bulles
#

def triBulles(T) :
    for i in range(len(T)-1, 0, -1):
        swapped = False # optimisation
        for j in range(i):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
                swapped = True
        if not swapped:
            break
    return T

############################################################
# Exercice 3.1
#
# Trie par insertion le sous-tableau T[debut::gap] de T
#

def triInsertionPartiel(T, gap, debut) :
    for i in range(debut, len(T)):
            tmp = T[i]
            j = i
            while j >= gap and T[j - gap] > tmp:
                T[j] = T[j - gap]
                j -= gap
            T[j] = tmp
    return T

############################################################
# Exercice 3.2
#
# Tri Shell
#

def triShell(T) :
    interval = len(T) // 2
    while interval > 0:
        triInsertionPartiel(T, interval, 0)
        interval //= 2
    return T

##############################################################
#
# Mesure du temps
#

def mesure(algo, T) :
    debut = clock()
    algo(T)
    return clock() - debut

def mesureMoyenne(algo, tableaux) :
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-') :
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos) :
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesureMoyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche(titre) :
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution')
  plt.legend(loc='upper left')
  plt.title(titre)
  plt.show()

def compareAlgos (algos, taille=1000, pas=100, ech=5) :
  # taille = 1000 : taille maximale des tableaux à trier
  # pas = 100 : pas entre les tailles des tableaux à trier
  # ech = 5 : taille de l'échantillon pris pour faire la moyenne
  for tri in algos :
      if testeQueLaFonctionTrie(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")
  print()
  print("Comparaison à l'aide de randomPerm")
  tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de randomPerm")
  print()
  
  print("Comparaison à l'aide de randomTab")
  tableaux = [[i, [randomTab(i,0,1000000) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de randomTab")
  print()

  print("Comparaison à l'aide de derangeUnPeu (rev = True)")
  tableaux = [[i, [derangeUnPeu(i,10,True) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = True)")
  print()

  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  tableaux = [[i, [derangeUnPeu(i,10,False) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
  print()

def compareAlgosSurTableauxTries (algos, taille=20000, pas=1000, ech=10) :
  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  tableaux = [[i, [derangeUnPeu(i,10,False) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
  
##############################################################
#
# Main
#

if __name__ == '__main__':
  trisInsertion = [ triInsertionEchange, triInsertionRotation, triInsertionRapide ]
  trisLents = [ triSelection, triBulles ]

  sys.setrecursionlimit(4000)

  # Question 1.6
  
  print("Exercice 1")
  algos = [triSelection]
  compareAlgos(algos)
  
  # Question 2.4
  
  print("Exercice 2")
  algos += trisInsertion + [triFusion, triBulles]
  compareAlgos(algos)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # On remarque que l'algorithme le moins efficace est celui de triBulles et le plus efficace est triFusion
  # ce qui reflete les resultats vues en cours dans le sens ou la complixité de triFusion est O(nlog(n)) et 
  # de triBulles à O(n^2) qui fait enormement d'echanges(affectations) en seconde position (en finction de l'efficacité)
  # on remarque que c'est l'algorithme de triInsertionRapide qui vient apres le triFusion apres c'est le triSelection
  # et on remarque que le triInsertionEchange est moins efficace sur des tableaux triées à l'envers et il est plus efficace sur
  # des tableaux presque triés contrairement au triSelection 
  ###################################################################
  
  # Question 3.3
  
  print("Exercice 3")
  algos = [triShell]
  compareAlgos(algos)


  # Question 3.4

  print("Comparaisons de tous les algos")
  algos = trisInsertion + trisLents + [ triFusion, triShell ]
  compareAlgos(algos, taille=2000, pas=200)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # On remarque que le triShell est aussi efficace que le triFusion
  # il est meme un peu plus efficace sur des tableaux preque triés à l'envers
  # et le triFusion est moins efficace sur des tableaux presque triés à l'envers
  ###################################################################
  
  #compare les tris fusions et Shell

  print("Comparaisons des tris fusion et Shell")
  algos = [ triFusion, triShell ]
  compareAlgos(algos, taille=10000, pas=500)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # On voit ici que le triFusion est en moyenne un peu plus efficace que le triShell
  # mais sur des tableaux presque triés c'est le triShell qui est plus efficace
  ###################################################################
  
  # comparaison sur tableaux presque triés
  
  print("\nComparaisons sur tableaux presque triés")
  algos = trisInsertion + [ triFusion, triShell ]
  compareAlgosSurTableauxTries (algos)

  ###################################################################
  ##### Commentez ici les résultats obtenus pour les différents #####
  ##### algorithmes sur les différents types de tableaux ############
  ###################################################################
  # Ça confirme les resultats annoncés dans les remarques precedentes
  ###################################################################
