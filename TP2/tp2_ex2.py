#!/usr/bin/env python3

# Pour les tests
import tp2_ex1

# Pour le log à base 2
from math import log2

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, legend, show

# Pour l'affichage des résultats
from ea4lib import printcol

###############################################################################
#
# NE PAS MODIFIER !!!
#
def produit_matrice_2_2 (M1, M2) :
  '''Effectue le produit de deux matrices 2x2'''
  res = [ [0, 0], [0, 0] ]
  
  res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
  res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
  res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
  res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]

  return res
  


###############################################################################
# Exercice 2.1
#

# À COMPLÉTER
#
def puissance_matrice_2_2 (M, n) :
  '''Élève la matrice M à la puissance n par exponentiation rapide'''
  if n == 0: return [[1, 0], [0, 1]]
  else:
    tmp = puissance_matrice_2_2(M, n//2)
    carre = produit_matrice_2_2(tmp, tmp)
    if n % 2 == 0: return carre 
    else: return produit_matrice_2_2(carre, M)


#
# NE PAS MODIFIER !!!
#
def fibo_4(n) :
  '''Calcule le n-ième terme de la suite de Fibonacci 
     par exponentiation de matrice'''
  if n <= 0 : return 0
  if n <= 2 : return 1
  M = [ [1, 1], [1, 0] ]
  N = puissance_matrice_2_2 (M, n-1)
  return N[0][0]

# COMMENTAIRES - question 2.2
"""
  L'algorithme qui utilise la puissance de la matrice est plus efficace que fibo_3(nombre d'ops logarithmique)
"""


###############################################################################
# Exercice 2.3
#

# À COMPLÉTER
#
def produit_matrice_2_2_ops (M1, M2) :
  ''' produit_matrice_2_2 avec calcul du nombre d'opérations arithmétiques'''
  res = [ [0, 0], [0, 0] ]

  res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
  res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
  res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
  res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
  
  return res, 12

# À COMPLÉTER
#
def puissance_matrice_2_2_ops (M, n) :
  ''' puissance_matrice_2_2 avec calcul du nombre d'opérations arithmétiques'''
  if n == 0: return [[1, 0], [0, 1]], 0
  if n == 1: return M, 0
  else:
    tmp, ops_puis = puissance_matrice_2_2_ops(M, n//2)
    carre, ops_prod = produit_matrice_2_2_ops(tmp, tmp)
    if n % 2 == 0: 
      return carre, (ops_puis+ops_prod) 
    else: 
      res, ops_prod2 = produit_matrice_2_2_ops(carre, M)
      return res, (ops_prod2 + ops_prod + ops_puis)  

# À COMPLÉTER
#
def fibo_4_ops(n) :
  '''fibo_4 avec calcul du nombre d'opérations arithmétiques'''
  if n <= 0 : return 0, 0
  if n <= 2 : return 1, 0
  M = [ [1, 1], [1, 0] ]
  N, ops = puissance_matrice_2_2_ops (M, n-1)
  return N[0][0], ops

# COMMENTAIRES - question 2.3
# 
"""
  Elles refletent exactement les resultats vues en cours
"""

###############################################################################
#
# NE PAS MODIFIER !!!
#
def courbes_ops(n, pas=1) :
  ''' affiche les courbes des additions d'entiers effectuées par fibo_3 
      et des opérations arithmétiques effectuées par fibo_4 '''
  ops = [[]] * 2

  ops[0] = [ tp2_ex1.fibo_3_adds(i)[1] for i in range(0, n, pas) ]
  ops[1] = [ fibo_4_ops(i)[1] for i in range(0, n, pas) ]
  
  plot(range(0,n,pas), ops[0], 'cyan')
  plot(range(0,n,pas), ops[1], 'magenta')
  l = [ 'fibo_3_ops', 'fibo_4_ops']
  legend(l)
  show()

###############################################################################
# Exercice 2.4
#

from tp2_ex1 import nbOfBits

# À COMPLÉTER
#
def decompte_naif (a, b, c, d, e) :
  # cout de l'opération a = b*c+d*e lorsque la multiplication d'entiers est quadratique
  return nbOfBits(b) * nbOfBits(c) + nbOfBits(d) * nbOfBits(e) + nbOfBits(a)

# À COMPLÉTER
#
def decompte_karatsuba (a, b, c, d, e) :
  # cout de l'opération a = b*c+d*e lorsque la multiplication d'entiers utilise l'algorithme de Karatsuba
  return max(nbOfBits(b), nbOfBits(c)) ** log2(3) + max(nbOfBits(d), nbOfBits(e)) ** log2(3) + nbOfBits(a)

# À COMPLÉTER
#
def produit_matrice_2_2_bits (M1, M2, compte = decompte_naif) :
  ''' produit_matrice_2_2 avec calcul du nombre d'opérations sur les bits'''
  res = [ [0, 0], [0, 0] ]

  res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
  a = compte(res[0][0],  M1[0][0], M2[0][0], M1[0][1], M2[1][0])
  res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
  b = compte(res[1][0],  M1[1][0], M2[0][0], M1[1][1], M2[1][0])
  res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
  c = compte(res[0][1],  M1[0][0], M2[0][1], M1[0][1], M2[1][1])
  res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
  d = compte(res[1][1],  M1[1][0], M2[0][1], M1[1][1], M2[1][1])

  return res, a+b+c+d

# À COMPLÉTER
#
def puissance_matrice_2_2_bits (M, n, compte = decompte_naif) :
  '''puissance_matrice_2_2 avec calcul du nombre d'opérations sur les bits''' 
  if n == 0: return [[1, 0], [0, 1]], 0
  if n == 1: return M, 0
  else:
    tmp, ops_puis = puissance_matrice_2_2_bits(M, n//2, compte)
    carre, ops_prod = produit_matrice_2_2_bits(tmp, tmp, compte)
    if n % 2 == 0: 
      return carre, ops_puis + ops_prod
    else: 
      res, ops_prod2 = produit_matrice_2_2_bits(carre, M, compte)
      return res, (ops_prod + ops_prod2 + ops_puis)  


def fibo_4_bits(n, compte = decompte_naif) :
  '''fibo_4 avec calcul du nombre d'opérations sur les bits'''
  if n <= 0 : return 0, 0
  if n <= 2 : return 1, 0
  M = [ [1, 1], [1, 0] ]
  N, ops = puissance_matrice_2_2_bits(M, n-1, compte)  
  return N[0][0], ops

# COMMENTAIRES - question 2.4
"""
  En utilisant la multiplication de karatsuba on a un algo plus efficace que celui qui utilise la methode de multiplication naive
"""

###############################################################################################
###############################################################################################
########################### courbes - opérations sur les bits  ################################
  
#
# LIRE, NE PAS MODIFIER
#

def courbes_bits(n, tous=True, pas=1, compte=decompte_naif) :
  ''' affiche les courbes des opérations élémentaires effectuées 
      pour le calcul de Fn par les différents algos '''

  ops = [[]] * 2
  if tous :
    ops += [[]]
    ops[0] = [ tp2_ex1.fibo_3_bits(i)[1] for i in range(0, n, pas) ]
    ind = 1
  else :
    ind = 0
  ops[ind] = [ fibo_4_bits(i, compte)[1] for i in range(0, n, pas) ]
  if tous:
    renorm = ops[ind][(n//pas)//2] / ((((n//pas)//2)*pas)**(log2(3)))
  else :
    renorm = ops[ind][-1] / (((n-1)//pas*pas)**(log2(3)))
  ops[ind+1] = [ i**(log2(3)) * renorm  for i in range(0, n, pas) ]  
  # courbe témoin - complexité théorique de fibo_4_bits renormalisée

  l = []
  if tous :
    plot(range(0,n,pas), ops[0], 'cyan')
    l += [ 'fibo_3_bits' ]
  plot(range(0,n,pas), ops[ind], 'magenta')
  plot(range(0,n,pas), ops[ind+1], 'black', linestyle='dashed')
  if compte == decompte_naif :
      l += ['fibo_4_bits - avec multiplication quadratique']
  else :
      l += ['fibo_4_bits - avec multiplication par l\'algo de Karatsuba' ]
  l += [ 'courbe de x**log2(3) renormalisée' ]
  legend(l)
  show()

###############################################################################################
###############################################################################################
############################## courbes - temps d'exécution  ###################################
  
#
# LIRE, NE PAS MODIFIER
#

def courbes_temps(n, tous=True, pas=1) :
  ''' affiche les courbes du temps de calcul de Fn par les différents algos '''
  
  temps = [[], []]

  if tous:
    temps += [[]]
    temps[0] = [ tp2_ex1.mesure(tp2_ex1.fibo_3, i) for i in range(0, n, pas) ]
    ind = 1
  else :
    ind = 0
    
  temps[ind] = [ tp2_ex1.mesure(fibo_4, i) for i in range(0, n, pas) ]
  renorm = temps[ind][-1] / (((n-1)//pas*pas)**(log2(3)))
  temps[ind+1] = [ i**(log2(3)) * renorm for i in range(0, n, pas) ]    
  # courbe témoin - complexité théorique de fibo_4_bits renormalisée

  l = []
  if tous :
    plot(range(0,n,pas), temps[0], 'cyan')
    l += ['temps pour exécuter fibo_3']
  plot(range(0,n,pas), temps[ind], 'magenta')
  plot(range(0,n,pas), temps[ind+1], 'black', linestyle='dashed')
  l += [ 'temps pour exécuter fibo_4', 'courbe de x**log2(3) renormalisée']
  legend(l)
  show()

  
#####################################################################################
#####################################################################################
################# TESTS #############################################################
#
# NE PAS MODIFIER
#

def test_prod22Data() :
  return [ [ [ [3, 0], [5, 6] ], [ [1, 4], [2, 1] ], [ [3, 12 ], [ 17 , 26 ] ] ] ,
           [ [ [20, 16], [ 5, 10 ]  ],  [ [10, 7], [2, 3] ],  [ [232, 188], [70, 65] ] ],
           [ [  [60, 5], [4, 1]  ], [ [54, 30], [11, 4]  ], [ [3295, 1820], [227, 124]] ],
           [ [ [34, 70], [2, 18] ], [ [56, 29], [10, 16] ], [ [2604, 2106], [292, 346]] ],
          [ [ [54, 30], [11, 4] ], [ [60, 5], [4, 1] ] , [ [3360, 300], [676, 59] ] ]
  ]

def test_prod22():
  printcol('{Test produit_matrice_2_2:}','bold')
  score = 0
  data = test_prod22Data()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[ 2 ]
    fb = produit_matrice_2_2 ( dt[0], dt[1] )
    if fb == refr :
      score += 1
      printcol('{ok}','green')
    else :
      printcol('{Mauvais résultat}','red')
      print('    entrée  : %s x %s' % (n,dt[1]))
      print('    calcule : %s' % fb)
      print('    attendu : %s' % refr)
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print() 

def test_puissanceData() :
  return [ [ [ [1, 4], [2, 1] ], 2, [[9, 8], [4, 9]]],
           [ [ [3, 0], [5, 6] ], 3, [[27, 0], [315, 216]] ],
           [ [ [3, 12 ], [ 17 , 26 ] ], 8, [[252018687525, 442324154508], [626625885553, 1099806650332]] ],
           [ [ [20, 16], [ 5, 10 ]  ], 6,  [[192672000, 202176000], [63180000, 66312000]] ],
           [ [ [232, 188], [70, 65] ], 5, [[1640021237352, 1367968885308], [509350116870, 424857387105]] ],
           [ [ [10, 7], [2, 3] ], 4, [[15362, 12467], [3562, 2895]] ],
           [ [  [60, 5], [4, 1]  ], 7 , [[2894868940020, 243934318805], [195147455044, 16443978121]] ],
           [ [ [54, 30], [11, 4]  ], 10, [[538139813380894176, 288789026527531200], [105889309726761440, 56824769168342176]] ],
           [ [ [34, 70], [2, 18] ], 3,  [[51344, 156240], [4464, 15632]] ],
           [ [ [56, 29], [10, 16] ], 2, [[3426, 2088], [720, 546]] ],
           [ [ [54, 30], [11, 4] ], 5 ,  [[697669224, 374399400], [137279780, 73670224]] ],
           [ [ [60, 5], [4, 1] ], 9, [[10538945536660820, 888057647401005], [710446117920804, 59865297328961]] ]
  ]


#
# NE PAS MODIFIER
#
def test_puissance():
  printcol('{Test puissance_matrice_2_2:}','bold')
  score = 0
  data = test_puissanceData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %2d/%2d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[ 2 ]
    fb = puissance_matrice_2_2 ( dt[0], dt[1] )
    if fb == refr :
      score += 1
      printcol('{ok}','green')
    else :
      printcol('{Mauvais résultat}','red')
      print('    entrée  : %s ^ %d' % (n,dt[1]))
      print('    calcule : %s' % fb)
      print('    attendu : %s' % refr)
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print()

#
# AJOUTER D'AUTRES DONNEES DE TEST
# [<valeur n>, (<valeur F_n> , <nb ops possibles>) ]
def test_fibo_4_opsData() :
  return [
 (0,  (0,    {0})),
 (1,  (1,    {0})),
 (2,  (1,    {0})),
 (3,  (2,    {12,14,16,18})),
 (4,  (3,    {24,26,32,34})),
 (5,  (5,    {24,28,32,36})),
 (6,  (8,    {36,40,48,52})),
 (7,  (13,   {36,40,48,52})),
 (8,  (21,   {48,52,64,68})),
 (9,  (34,   {36,42,48,54})),
 (10, (55,   {48,54,64,70})),
 (11, (89,   {48,54,64,70})),
 (12, (144,  {60,66,80,86})),
 (13, (233,  {48,54,64,70})),
 (14, (377,  {60,66,80,86})),
 (15, (610,  {60,66,80,86})),
 (16, (987,  {72,78,96,102})),
 (17, (1597, {48,56,64,72})),
 (18, (2584, {60,68,80,88})),
 (19, (4181, {60,68,80,88}))]

#
# NE PAS MODIFIER
#
def test_fibo_4():
  printcol('{Test fibo_4_ops:}','bold')
  score = 0
  data = test_fibo_4_opsData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %2d/%2d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    Tops=sorted(list(Tops))
    fb, ops = fibo_4_ops(n)
    if (fb == Tres and ops in Tops):
      score += 1
      printcol('{ok}','green')
    elif (fb == Tres):
      printcol('{Mauvais nombre d\'opérations}','yellow')
      print('    entrée  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops) )
      print('    attendu : %d en %s ops' % (Tres,(" ou ".join([str(i) for i in Tops])) ) )
    else :
      printcol('{Mauvais résultat}','red')
      print('    entrée  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops) )
      print('    attendu : %d en %s ops' % (Tres,(" ou ".join([str(i) for i in Tops])) ) )
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print()
  

if __name__ == '__main__':
  # courbes des temps d'exécution
  courbes_temps(100000, pas=1000)              # fibo_3 et fibo_4
  courbes_temps(100000, tous=False, pas=1000)  # seulement fibo_4

  test_puissance()
  test_fibo_4()

  # courbes du nombre d'additions d'entiers
  courbes_ops(1000, 1)      # fibo_3 et fibo_4

  # courbes du nombre d'opérations élémentaires sur les bit
  courbes_bits(10000, pas=10)                                          # fibo_3 et fibo_4, mltiplication naïve
  courbes_bits(10000, pas=10, compte=decompte_karatsuba)               # fibo_3 et fibo_4, mltiplication par Karatsuba
  courbes_bits(10000, tous=False, pas=10, compte=decompte_karatsuba)   # seulement fibo_4, mltiplication par Karatsuba
