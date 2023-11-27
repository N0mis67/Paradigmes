def tri(liste_nbre): # déclaration de la fonction tri

    #  sorted permet de trier la liste
    list_tri = sorted(liste_nbre)
    
    return list_tri

# Exemple d'utilisation
ma_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
list_tri = tri(ma_liste)
print("Liste initiale :", ma_liste)
print("Liste triée :", list_tri)