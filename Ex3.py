def maj(chaine):

    # split permet de diviser la chaîne en une liste de mots
    mots = chaine.split()

    #filtrer les mots majuscules à l'aide de la compréhension de liste
    mots_majuscules = [mot for mot in mots if mot[0].isupper()]

    return mots_majuscules

# Exemple d'utilisation
exemple = "Python est le meilleur langage du monde"
resultat = maj(exemple)
print("Mots commençant par une majuscule :", resultat)