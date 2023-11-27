def calculer_moyenne(liste_nombres):
    if not liste_nombres:
        return None  # Retourne None si la liste est vide pour éviter une division par zéro
    
    somme = sum(liste_nombres)
    moyenne = somme / len(liste_nombres)
    return moyenne

ma_liste = [1, 2, 3, 4, 5]
resultat = calculer_moyenne(ma_liste)
print("La moyenne est :", resultat)