import numpy as np

def dtw(ts1=[], ts2=[]):
    #le nombre de vecteur pour le 1er audio
    m = len(ts1)
    #le nombre de vecteur pour le 2eme audio
    n = len(ts2)
    #on va creer n matrice de n ligne et m colonne
    DTW = np.zeros((n, m), dtype=float)
    # on remplit le premier ligne du matrice pour le 1er audio
    for i in range(1, m):
        DTW[0, i] = distance(ts1[i], ts2[0]) + DTW[0, i - 1]
    # on remplit le premier ligne du matrice pour le 2eme audio
    for i in range(1, n):
        DTW[i, 0] = distance(ts1[0], ts2[i]) + DTW[i - 1, 0]
    # on remplit les autres element du matrice
    for i in range(1, n):
        for j in range(1, m):
            cost = distance(ts1[j], ts2[i])
            DTW[i, j] = cost + np.min([DTW[i - 1, j],DTW[i, j - 1],DTW[i - 1, j - 1]])


    path = dict()

    #on accosie la valeur dtw(n-1,m-1) a la variable path pour le depart
    path[0] = (n - 1, m - 1, DTW[n - 1, m - 1])
    c = 0
    finished = False
    i = n - 1
    j = m - 1
    while (not finished):
        #on recupere les 3 valeur de (i-1,j) ,(i-1,j-1) et (i,j-1) du matrice et on les affecte au vecteur v
        v = np.array([DTW[i - 1, j], DTW[i - 1, j - 1], DTW[i, j - 1]])
        # on va recuperer le minimum de ces valeur et on l'affect au variable cost
        cost = np.min(v)
        # on va voir ou il existe la valeur minimal
        k = np.where(v == cost)[0][0]

        if k == 0:  # si le minimum existe dans la case (i-1,j)
            #on  va affecter cette valeur avec son indice
            path[c] = (i - 1, j, cost)
            i = i - 1
        elif k == 1: # si le minimum existe dans la case (i-1,j-1)
            # on  va affecter cette valeur avec son indice
            path[c] = (i - 1, j - 1, cost)
            j = j - 1
            i = i - 1
        else: # si le minimum existe dans la case (i-1,j-1)
            path[c] = (i, j - 1, cost)
            j = j - 1
        #la condition d'arret c'est qu'on est arrivé a la position (0,0) dans la matrice DTW
        if path[c][0] == 0 and path[c][1] == 0:
            finished = True
        c += 1
    #on a creer un vecteur pour stocker les valeur du cout du chemin
    cost = np.array([])
    for k in path.keys():
        cost = np.append(cost, path[k][2])
    #on calcule la somme des cout
    S = np.sum(cost)
    # on normalise cette valeur et on la retourne
    D = np.sqrt(S)
    return D

def distance(p1, p2):
    return (p1 - p2) ** 2
