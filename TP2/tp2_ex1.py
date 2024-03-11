#!/usr/bin/env python3

# Pour les fonctions mathématiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import legend, plot, show

# Pour l'affichage des résultats
from ea4lib import printcol

#Pour calculer le temps d'exécution
from time import process_time

# NE PAS MODIFIER
# Calcule
#    le n-ième terme de la suite de Fibonacci 
# par 3 méthodes

def fibo_1(n) :
  if n <= 0 : return 0
  if n <= 2 : return 1
  return fibo_1(n-1) + fibo_1(n-2)

def fibo_2(n) :
  if n <= 0 : return 0
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
  return liste[n]

def fibo_3(n) :
  if n <= 0 : return 0
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
  return last

# COMMENTAIRES - question 1.1
"""
  1.1- Dans la premiere fentre on voit que fibo_3 et fibo_2 on presque la meme courbe qui semble etre lineaire
  et la fonction fibo_1 colle avec la fonction phi^n ce qui permet de dire que fibo_1 a une complexite exponentielle
  Dans la deuxieme fenetre on voit que fibo_3 coincide avec la courbe de n^2 ce qui permet de dire que fibo_3 et fibo_2 ont une complexité 
  quadratique 
"""


###############################################################################
# Exercice 1.2
# 
# Calcule
#    le n-ième terme de la suite de Fibonacci et 
#    le nombre d'additions de (grands) entiers utilisées

# À COMPLÉTER
def fibo_1_adds(n) :
  if n <= 0: return 0, 0
  if n <= 2: return 1, 0 
  n_1, ops_1 = fibo_1_adds(n-1)
  n_2, ops_2 = fibo_1_adds(n-2) 
  return n_1 + n_2, ops_1 + ops_2 + 1

# À COMPLÉTER
def fibo_2_adds(n) :
  ops = 0
  if n <= 0 : return 0, ops
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
    ops += 1
  return liste[n], ops

# À COMPLÉTER
def fibo_3_adds(n) :
  ops = 0
  if n <= 0 : return 0, ops
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
    ops += 1
  return last, ops

# COMMENTAIRES - question 1.2
"""
 1.2- Oui ces resultats refletent les temps d'execution des 3 algos precedents
"""
 

###############################################################################
#
# LIRE, NE PAS MODIFIER
#
def colors(tous=True) :
  return ['red', 'green', 'cyan', 'black'] if tous else ['green', 'cyan', 'black']

def courbes_adds(n, tous=True, pas=1) :
  ''' affiche les courbes des additions effectuées pour le calcul de Fn par les différents algos
  (les trois si tous=True, valeur par défaut; seulement fibo_2 et fibo_3 si tous=False)'''

  algos = [fibo_1_adds, fibo_2_adds, fibo_3_adds] if tous else [fibo_2_adds, fibo_3_adds] 
  nb_ops = [ [ algo(i)[1] for i in range(0, n, pas) ] for algo in algos ]

  l = ['fibo_1_adds', 'fibo_2_adds', 'fibo_3_adds'] if tous else ['fibo_2_adds', 'fibo_3_adds'] 
  for valeurs, couleur in zip(nb_ops, colors(tous)) :
    plot(range(0,n,pas), valeurs, couleur)
  legend(l)
  show()

  
###############################################################################
# Exercice 1.4
#

# À COMPLÉTER
def nbOfBits(i) :
  return i.bit_length() #math.floor(math.log(i, 2.0)) + 1 

  
###############################################################################
# Exercice 1.5
#

# À COMPLÉTER
def fibo_1_bits(n) :
  if n <= 0: return 0, 0
  if n <= 2: return 1, 0 
  n_1, ops_1 = fibo_1_bits(n-1)
  n_2, ops_2 = fibo_1_bits(n-2) 
  return n_1 + n_2, nbOfBits(n_1+n_2) + ops_1 + ops_2

# À COMPLÉTER
def fibo_2_bits(n) :
  ops_bits = 0
  if n <= 0 : return 0, ops_bits
  liste = [0, 1] + [0] * (n-1)
  for i in range(2, n+1) :
    liste[i] = liste[i-1] + liste[i-2]
    ops_bits += nbOfBits(liste[i])
  return liste[n], ops_bits

# À COMPLÉTER
def fibo_3_bits(n) :
  ops_bits = 0
  if n <= 0 : return 0, ops_bits
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
    ops_bits += nbOfBits(last)
  return last, ops_bits                                                                         

# COMMENTAIRES - question 1.5
"""
 1.5- Oui les courbes obtenues reflétent exactement les conclusions du cours 
"""
###############################################################################################
###############################################################################################
########################### courbes - opérations sur les bits  ################################
  
#
# LIRE, NE PAS MODIFIER
#

phi = (1+math.sqrt(5))/2
def courbes_ops(n, tous=True, pas=1) :
  ''' affiche les courbes des opérations élémentaires effectuées pour le calcul de Fn par les différents algos '''

  algos = [fibo_1_bits, fibo_2_bits, fibo_3_bits] if tous else [fibo_2_bits, fibo_3_bits]
  nb_ops = [ [ algo(i)[1] for i in range(0, n, pas) ] for algo in algos ]

  if tous :
    renorm = nb_ops[0][-1] / (((n-1)//pas*pas)*phi**((n-1)//pas*pas)) 
    nb_ops += [[ i * phi**i * renorm  for i in range(0, n, pas) ]]
    #courbe témoin - complexité théorique de fibo_1_bits renormalisée
  else :
      renorm = nb_ops[-1][-1] / ((n-1)//pas*pas)**2
      nb_ops += [[(i)**2 * renorm for i in range(0, n, pas) ]]
      #courbe témoin - complexité théorique de fibo_3_bits renormalisée

  l = ['fibo_1_bits', 'fibo_2_bits', 'fibo_3_bits'] if tous else ['fibo_2_bits', 'fibo_3_bits']    
  for valeurs, couleur in zip(nb_ops, colors(tous)) :
    if couleur != 'black' :
      plot(range(0,n,pas), valeurs, couleur)
    else :
      plot(range(0,n,pas), valeurs, color=couleur, linestyle='dashed')
  if tous :
    l += ['courbe x * phi**x renormalisée']
  else :
    l += ['courbe x**2 renormalisée']
  legend(l)
  show()

###############################################################################################
###############################################################################################
############################## courbes - temps d'exécution  ###################################
  
#
# LIRE, NE PAS MODIFIER
#

def mesure(algo, n):
  ''' retourne le temps de calcul de Fn par l'algo en paramètre '''
  debut = process_time()
  algo(n)
  return (process_time()-debut)

def courbes_temps(n, tous=True, pas=1) :
  ''' affiche les courbes du temps de calcul de Fn par les différents algos '''
  temps = [[], []]
  if tous : temps += [[],[]]

  temps[0] = [ mesure(fibo_3, i) for i in range(0, n, pas) ]
    
  if tous :
    temps[1] = [ mesure(fibo_2, i) for i in range(0, n, pas) ]
    temps[2] = [ mesure(fibo_1, i) for i in range(0, n, pas) ]
 
    renorm = temps[2][-1] / ((n-1)//pas*pas * phi**((n-1)//pas*pas))
    temps[3] = [ i * phi**i * renorm for i in range(0, n, pas) ]  
    #courbe témoin - complexité théorique de fibo_1_bits renormalisée
  else :
    renorm =  temps[0][-1] / ((n-1)//pas*pas)**2
    temps[1] = [ (i)**2 * renorm for i in range(0, n, pas) ]    
    #courbe témoin - complexité théorique de fibo_3_bits
    
  plot(range(0,n,pas), temps[0], 'cyan')
  l = ['temps pour exécuter fibo_3']
  if tous :
    plot(range(0,n,pas), temps[1], 'green')
    plot(range(0,n,pas), temps[2], 'red')
    plot(range(0,n,pas), temps[3], 'black', linestyle='dashed')
    l += [ 'temps pour exécuter fibo_2', 'temps pour exécuter fibo_1'] 
  else :
    plot(range(0,n,pas), temps[1], 'black', linestyle='dashed')
  if tous :
    l += ['courbe x * phi**x renormalisée']
  else :
    l += ['courbe x**2 renormalisée']
  legend(l)
  show()


###############################################################################################
###############################################################################################
########################################## TESTS ##############################################
  
#
# NE PAS MODIFIER
#
def test_fibo_1_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 0)), (3, (2, 1)), (4, (3, 2)), (5, (5, 4)), (6, (8, 7)), (7, (13, 12)), (8, (21, 20)), (9, (34, 33)), (10, (55, 54)), (11, (89, 88)), (12, (144, 143)), (13, (233, 232)), (14, (377, 376)), (15, (610, 609))]

#
# NE PAS MODIFIER
#
def test_fibo_2_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 1)), (3, (2, 2)), (4, (3, 3)), (5, (5, 4)), (6, (8, 5)), (7, (13, 6)), (8, (21, 7)), (9, (34, 8)), (10, (55, 9)), (11, (89, 10)), (12, (144, 11)), (13, (233, 12)), (14, (377, 13)), (15, (610, 14))]

#
# NE PAS MODIFIER
#
def test_fibo_3_addsData() :
  return [(0, (0, 0)), (1, (1, 0)), (2, (1, 1)), (3, (2, 2)), (4, (3, 3)), (5, (5, 4)), (6, (8, 5)), (7, (13, 6)), (8, (21, 7)), (9, (34, 8)), (10, (55, 9)), (11, (89, 10)), (12, (144, 11)), (13, (233, 12)), (14, (377, 13)), (15, (610, 14))]

#
# NE PAS MODIFIER
#
def test_fibo_addsData(i) :
  if i == 1 : return test_fibo_1_addsData()
  elif i == 2 : return test_fibo_2_addsData()
  else : return test_fibo_3_addsData()

#
# NE PAS MODIFIER
#
def test_fibo_adds(num):
  algos = [fibo_1_adds, fibo_2_adds, fibo_3_adds]
  printcol('{Test %s:}' %  algos[num-1].__name__,'bold')
  score = 0
  data = test_fibo_addsData(num)
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %2d/%2d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    fb, ops = algos[num-1](n)
    if (fb == Tres and ops == Tops):
      score += 1
      printcol('{ok}','green')
    elif (fb == Tres):
      printcol('{Mauvais nombre d\'opérations}','yellow')
      print('    entree  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops) )
      print('    attendu : %d en %d ops' % (Tres,Tops) )
    else :
      printcol('{Mauvais résultat}','red')
      print('    entree  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops) )
      print('    attendu : %d en %d ops' % (Tres,Tops) )
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print()

#
# NE PAS MODIFIER
#
def test_nbOfBitsData() :
  return [[4, 3],
          [7, 3],
          [10, 4],
          [10 ** 2, 7],
          [10 ** 3, 10],
          [10 ** 4, 14]]

#
# NE PAS MODIFIER
#
def test_nbOfBits():
  printcol('{Test nbOfBits:}','bold')
  score = 0
  data = test_nbOfBitsData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %2d/%2d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[1]
    fb = nbOfBits(n)
    if fb == refr :
      score += 1
      printcol('{ok}','green')
    else :
      printcol('{Mauvais résultat}','red')
      print('    entree  : %s' % n)
      print('    calcule : %d' % (fb) )
      print('    attendu : %d' % (refr) )
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print()
  
#
# NE PAS MODIFIER
#
def test_fibo_1_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 0)), (4, (3, 4)), (8, (21, 52)), (10, (55, 146)), (16, (987, 2760))]

#
# NE PAS MODIFIER
#
def test_fibo_2_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 1)), (4, (3, 5)), (8, (21, 21)), (10, (55, 33)), (16, (987, 85))]

#
# NE PAS MODIFIER
#
def test_fibo_3_bits_Data() :
  return [(-1, (0, 0)), (2, (1, 1)), (4, (3, 5)), (8, (21, 21)), (10, (55, 33)), (16, (987, 85))]

#
# NE PAS MODIFIER
#
def test_fibo_bitsData(i) :
  if i == 1 : return test_fibo_1_bits_Data()
  elif i == 2 : return test_fibo_2_bits_Data()
  else : return test_fibo_3_bits_Data()

#
# NE PAS MODIFIER
#
def test_fibo_bits(num):
  algos = [fibo_1_bits, fibo_2_bits, fibo_3_bits]
  printcol('{Test %s:}' %  algos[num-1].__name__,'bold')
  score = 0
  data = test_fibo_bitsData(num)
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %2d/%2d : ' % (i + 1, ldata), end='')
    n = dt[0]
    Tres, Tops = dt[1]
    fb, ops = algos[num-1](n)
    if (fb == Tres and ops == Tops):
      score += 1
      printcol('{ok}','green')
    elif (fb == Tres):
      printcol('{Mauvais nombre d\'opérations}','yellow')
      print('    entree  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops) )
      print('    attendu : %d en %d ops' % (Tres,Tops) )
    else :
      printcol('Mauvais résultat','red')
      print('    entree  : %s' % n)
      print('    calcule : %d en %d ops' % (fb,ops))
      print('    attendu : %d en %d ops' % (Tres,Tops) )
  printcol('{** Score %d/%d : %s}' % (score, ldata, "super !" if score==ldata else "essaie encore !"),'bold')
  print()
  
if __name__ == '__main__':
  # courbes des temps d'exécution
  courbes_temps(30)                            # les 3 algos
  courbes_temps(100000, tous=False, pas=1000)  # seulement fibo_2 et fibo_3


  test_fibo_adds(1)
  test_fibo_adds(2)
  test_fibo_adds(3)
  # courbes du nombre d'additions d'entiers
  courbes_adds(30)                             # les 3 algos
  courbes_adds(1000, tous=False)               # seulement fibo_2_adds et fibo_3_adds

  
  test_nbOfBits()
  test_fibo_bits(1)
  test_fibo_bits(2)
  test_fibo_bits(3)
  # courbes du nombre d'opérations élémentaires sur les bits
  courbes_ops(30)                              # les 3 algos
  courbes_ops(50000, tous=False, pas=1000)     # seulement fibo_2_bits et fibo_3_bits
