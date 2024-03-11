#!/usr/bin/env python3

import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

import random
from time import perf_counter as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")

############################################################
# Exercice 1.1
#
# Tri rapide avec mémoire auxiliaire et en place
#
def partition(T):
    pivot, milieu, gauche, droite = T[0], [], [], []
    for i in range(len(T)):
        if T[i] < pivot: gauche.append(T[i])
        elif T[i] > pivot: droite.append(T[i])
        else: milieu.append(T[i])
    return gauche, milieu, droite

def tri_rapide(T):
    if len(T) < 2: return T
    gauche, milieu, droite = partition(T)
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

def partition_en_place(T, debut, fin):
    pivot, gauche, droite = T[debut], debut+1, fin-1
    while gauche <= droite:
        if T[gauche] < pivot: gauche += 1
        elif T[droite] >= pivot: droite -= 1
        else: T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite

def tri_rapide_en_place(T, debut = 0, fin = None):
    if fin == None: fin = len(T)
    if fin - debut < 2: return
    pivot_index = partition_en_place(T, debut, fin)
    tri_rapide_en_place(T, debut, pivot_index)
    tri_rapide_en_place(T, pivot_index+1, fin)
    return T

"""
1.3 on voit que le tri rapide est dans la meme classe que le tri fusion en general
    mais sur des tableaux  triés à l'envers on voit que le tri insertion a une complexité
    linéaire mais le tri_rapide a une comlexité quadratique
"""

############################################################
# Exercice 1.2
#
# Tri rapide avec mémoire auxiliaire et en place avec pivot/usr/bin/python3: can't find '__main__' module in '/home/ala/Documents/S4/EA4/Python_workspace/TP4'

# aléatoire
#

def partition_aleatoire(T):
    pivot, milieu, gauche, droite = random.choice(T), [], [], []
    for i in range(len(T)):
        if T[i] < pivot: gauche.append(T[i])
        elif T[i] > pivot: droite.append(T[i])
        else: milieu.append(T[i])
    return gauche, milieu, droite

def tri_rapide_aleatoire(T):
    if len(T) < 2: return T
    gauche, milieu, droite = partition_aleatoire(T)
    return tri_rapide_aleatoire(gauche) + milieu + tri_rapide_aleatoire(droite)

def partition_en_place_aleatoire(T, debut, fin):
    pivot, gauche, droite = T[random.choice(range(debut, fin))], debut+1, fin-1
    while gauche <= droite:
        if T[gauche] < pivot: gauche += 1
        elif T[droite] >= pivot: droite -= 1
        else: T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite

def tri_rapide_en_place_aleatoire(T, debut = 0, fin = None):
    if fin == None: fin = len(T)
    if fin - debut < 2: return 
    pivot_index = partition_en_place(T, debut, fin)
    tri_rapide_en_place(T, debut, pivot_index)
    tri_rapide_en_place(T, pivot_index+1, fin)
    return T

############################################################
""" Exercice 1.3: Interprétation des courbes

	Le cas defavorable n'est plus problematique avec un pivot aleatoire (la probabilité que ça arrive est vraiment vraiment faible, il 
	faut pour cela choisir le plus grand ou le plus petit element comme pivot à chaque étape de partitionnement)
	
"""


############################################################
# Exercice 2.1
#
# Tri par insertion (voir TP3)
#

def tri_insertion(T):
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j-1] <= T[j]: break
            T[j-1], T[j] = T[j], T[j-1]
    return T


############################################################
# Exercice 2.2
#
# les tableaux de taille < 15 sont triés par insertion, le
# reste avec l'algo de tri rapide usuel.
#

def tri_insertion_indexes(arr, low, n):
        for i in range(low + 1, n + 1):
            val = arr[i]
            j = i
            while j>low and arr[j-1]>val:
                arr[j]= arr[j-1]
                j-= 1
            arr[j]= val

def tri_rapide_ameliore(T):
    if len(T) < 15: return tri_insertion(T)
    gauche, milieu, droite = partition(T)
    return tri_rapide_ameliore(gauche) + milieu + tri_rapide_ameliore(droite)

############################################################
#"""
#    if fin == None: fin = len(T)-1
#    while debut < fin:
#        if fin-debut+1 < 15:
#            #tri_insertion(T[debut:fin+1]) #ça ne marche pas
#            tri_insertion_indexes(T, debut, fin)
#            break
#        else:
#            pivot_index = partition_en_place(T, debut, fin)
#            if pivot_index - debut < fin - pivot_index:
#                tri_rapide_ameliore(T, debut, pivot_index-1)
#                debut = pivot_index + 1
#            else:
#               tri_rapide_ameliore(T, pivot_index+1, fin)
#               fin = pivot_index - 1
#"""
# Exercice 2.3
#
# Tri rapide seulement pour les tableaux de taille >= 15 et
# ne fait rien pour les tableaux de taille < 15
#

def tri_rapide_partiel(T):
    if len(T) < 15: return T
    gauche, milieu, droite = partition(T)
    return tri_rapide_partiel(gauche) + milieu + tri_rapide_partiel(droite)

############################################################
# Exercice 2.4
#
# Trie par insertion le résultat de tri_rapide_partiel(T).
#
def tri_sedgewick(T):
    return tri_insertion(tri_rapide_partiel(T))

############################################################
""" Exercice 2.5: Interprétation des courbes

# A COMPLETER

"""


############################################################
# Exercice 3.1
#
# Tris drapeau. Attention, les éléments du tableau ne peuvent pas
# avoir d'autres valeurs que 1, 2 ou 3.
#

BLEU, BLANC, ROUGE = 1, 2, 3

def tri_drapeau(T):
    x, y, z = [], [], []
    for elt in T:
        match elt:
            case 1: x.append(BLEU)
            case 2: y.append(BLANC)
            case 3: z.append(ROUGE)
    return x + y + z

def tri_drapeau_en_place(T):
    i_blanc, deb, fin = 0, 0, len(T)-1
    while i_blanc <= fin:
        match T[i_blanc]:
            case 1:
                T[deb], T[i_blanc] = T[i_blanc], T[deb]
                deb += 1
                i_blanc += 1
            case 2:
                i_blanc += 1
            case 3:
                T[i_blanc], T[fin] = T[fin], T[i_blanc]
                fin -= 1
    return T



############################################################
# Exercice 3.2
#
# Effectue un tri drapeau par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne trois tableaux, contenant respectivement les éléments de couleurs 1, 2 et 3.
#

def partition_drapeau(T, pivot):
    milieu, gauche, droite = [], [], []
    for i in range(len(T)):
        if T[i] < pivot: gauche.append(T[i])
        elif T[i] > pivot: droite.append(T[i])
        else: milieu.append(T[i])
    return gauche, milieu, droite

############################################################
# Exercice 3.2
#
# Tris rapide, pivot drapeau pour amélioration si le tableau en entrée
# est très répété.
#

def tri_rapide_drapeau(T):
    if len(T) < 2: return T
    gauche, milieu, droite = partition_drapeau(T, T[random.choice(range(0, len(T)))])
    return tri_rapide_aleatoire(gauche) + milieu + tri_rapide_aleatoire(droite)


############################################################
""" Exercice 3.3: Interprétation des courbes

# A COMPLETER

"""

############################################################
# Exercice 3.4
#
# Effectue un tri drapeau EN PLACE par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne l'indice du premier élement blanc et du premier element rouge dans le tableau.
# (le premier élément bleu étant à la position 0 si il existe, pas besoin de le préciser.)
#


def partition_drapeau_en_place(T, pivot, deb = 0, fin = None):
    if fin == None: fin = len(T)-1
    mid = deb
    while mid <= fin:
        if T[mid] < pivot:
            T[mid], T[deb] = T[deb], T[mid]
            mid += 1
            deb += 1
        elif T[mid] > pivot:
            T[mid], T[fin] = T[fin], T[mid]
            fin -= 1
        else: # c'est egal (comme si c'etait un blanc)
            mid += 1
    return deb, fin

############################################################
# Exercice 3.4
#
# Tri rapide en place utilisant un partitionnement drapeau
#

def tri_rapide_drapeau_en_place(T, debut=0, fin=None):
    if fin == None: fin = len(T)-1
    if debut >= fin: return T
    if fin - debut == 2:
        if T[fin] < T[debut]:
            T[debut], T[fin] = T[fin], T[debut]
            return T
    first_pivot, last_pivot = partition_drapeau_en_place(T, T[random.choice(range(debut, fin))], debut, fin)
    tri_rapide_drapeau_en_place(T, debut, first_pivot-1)
    tri_rapide_drapeau_en_place(T, last_pivot+1, fin)
    return T


##############################################################
#
# Tri Fusion, pour comparaison
#

def fusion(T1, T2):
    i = 0
    j = 0
    res = []
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1
    res += T1[i:]
    res += T2[j:]
    return res

def tri_fusion(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb <= 1:
        return T[deb:fin]
    m = (fin - deb)//2
    T1 = tri_fusion(T, deb, deb+m)
    T2 = tri_fusion(T, deb+m, fin)
    return fusion(T1, T2)

##############################################################
#
# Mesure du temps
#

def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut

def mesure_moyenne(algo, tableaux):
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-'):
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos):
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesure_moyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche(titre):
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution (sec)')
  plt.legend(loc='upper left')
  plt.title(titre)

def random_perm(n):
    T = list(range(n))
    random.shuffle(T)
    return T

def test_tri(f):
    for i in range(2, 101):
        T = random_perm(i)
        T_sorted = sorted(T)
        T_output = f(T)
        if T_output != T_sorted:
            print("Échec sur :")
            print(T)
            return False
    return True

def random_tab(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

def derange_un_peu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]
    for i in range(k):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        T[a], T[b] = T[b], T[a]
    return T


def compare_algos (algos):
  for tri in algos:
      if test_tri(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")
  taille = 1000 # taille maximale des tableaux à trier
  pas = 100 # pas entre les tailles des tableaux à trier
  ech = 5 # taille de l'échantillon pris pour faire la moyenne
  
  plt.subplot(221)
  print()
  print("Comparaison à l'aide de random_perm")
  tableaux = [[i, [random_perm(i) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de random_perm")
  
  plt.subplot(222)
  print()
  print("Comparaison à l'aide de random_tab")
  tableaux = [[i, [random_tab(i,0,1000000) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de random_tab")
  
  plt.subplot(223)
  print()
  print("Comparaison à l'aide de derange_un_peu (rev = False)")
  tableaux = [[i, [derange_un_peu(i,20,False) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derange_un_peu (rev = False)")
  
  plt.subplot(224)
  print()
  print("Comparaison à l'aide de derange_un_peu (rev = True)")
  tableaux = [[i, [derange_un_peu(i,20,True) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche("Comparaison à l'aide de derange_un_peu (rev = True)")

  plt.show()


def test_tri_non_perm(tri, maxVal=3):
    for size in range(2,101):
        T = random_tab(size, 1, maxVal)
        T2 = tri(T)
        for i in range(1, len(T2)):
            if T2[i-1] > T2[i]: return False
    return True


def compare_tableaux_repetes(algos, taille=20000, pas=1000, ech=15, maxVal=3):
    for tri in algos:
      if test_tri_non_perm(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")


    print("Comparaison à l'aide de random_tab")
    tableaux = [[i, [random_tab(i,1, 3) for j in range(ech)]] for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de random_tab")
    plt.show()


##############################################################
#
# Main
#

if __name__ == '__main__':
  trisRapides = [ tri_insertion, tri_fusion, tri_rapide, tri_rapide_en_place, tri_rapide_aleatoire, tri_rapide_en_place_aleatoire ]
  trisHybrides = [ tri_rapide_ameliore, tri_sedgewick ]
  trisDrapeaux = [ tri_drapeau, tri_drapeau_en_place ]
  trisRapidesDrapeaux = [ tri_fusion, tri_rapide_drapeau, tri_rapide_drapeau_en_place ]

  # exercice 1

  print("Exercice 1")
  algos = trisRapides
  compare_algos(algos)

  # exercice 2

  print("Exercice 2")
  algos = trisHybrides
  compare_algos(algos)
  algos = trisRapides + trisHybrides
  compare_algos(algos)

  # exercice 3

  print("Exercice 3")
  # comparaison des tris drapeaux
  #print("Comparaisons sur tableaux très répétés")
  #algos = trisDrapeaux
  #compare_tableaux_repetes(algos, maxVal=3)

  # comparaison des tris rapide drapeaux
  #print("Comparaisons sur tableaux très répétés")
  #algos = [tri_rapide, tri_rapide_en_place] + trisRapidesDrapeaux
  #compare_tableaux_repetes(algos, taille=1000, pas=100, ech=5, maxVal=5)
