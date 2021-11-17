import numpy as np

tableau_de_zeros = np.zeros((2, 3)) # 2 lignes, 3 colonnes
#print(tableau_de_zeros)

tableau = np.array([[1, 2, 3], [4, 5, 6]])
#print(tableau.shape) -> (2, 3)
#print(tableau.shape[0]) -> 2
#print(tableau.shape[1]) -> 3

vect = np.arange(5) # [0 1 2 3 4]
#print(vect)

vecteur = np.linspace(0, 10, 4) # 4 nombres répartis uniformément de 0 à 10
#print(vecteur)

mon_tableau = np.array([5, 3, 4, 1, 2])
# print(mon_tableau.min())
# print(mon_tableau.max())
# print(mon_tableau.mean())
# print(mon_tableau.sum())
print(np.sort(mon_tableau))

