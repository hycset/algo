#python bulle

import time
import random


# Générer un tableau de n éléments aléatoires
def generer_donnees(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, 5000))  # valeurs entre 0 et 10000
    return tab

# Tri à bulles
def bulle(tab):
    for i in range(len(tab)-1):
        for j in range(len(tab)-1-i):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

# Créer un tableau déjà trié
def generer_tableau_trie(n):
    tab = generer_donnees(n)
    tab.sort()
    return tab

# Créer un tableau trié à l'envers
def generer_tableau_inverse(n):
    tab = generer_tableau_trie(n)
    tab.reverse()
    return tab

# Exemple aleatoire
donnees = generer_donnees(5000)  # petit tableau pour tester facilement
tab_test = donnees.copy() #pour eviter que les tableéu soit faussé
debut = time.perf_counter()
bulle(tab_test)
fin = time.perf_counter()
print(tab_test)
print((fin - debut)*1000, "ms")


# Exemple trie
donnees = generer_tableau_trie(5000)  # petit tableau pour tester facilement
tab_test = donnees.copy() #pour eviter que les tableéu soit faussé
debut = time.perf_counter()
bulle(tab_test)
fin = time.perf_counter()
print(tab_test)
print((fin - debut)*1000, "ms")


# Exemple inverse
donnees = generer_tableau_inverse(5000)  # petit tableau pour tester facilement
tab_test = donnees.copy() #pour eviter que les tableéu soit faussé
debut = time.perf_counter()
bulle(tab_test)
fin = time.perf_counter()
print(tab_test)
print((fin - debut)*1000, "ms")
