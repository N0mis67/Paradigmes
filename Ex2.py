def pair(liste_nbre):
    return [nombre for nombre in liste_nbre if nombre % 2 == 0]

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = pair(ma_liste)
print(resultat)