def concat(*args):

    resultat = ''.join(map(str, args)) # join permet de concaténer les arguments en une chaîne
    return resultat

resultat_final = concat("Bonjour", " ", "le", " ", "monde") # Appel de la fonction concat avec les arguments "Bonjour", "tout", "le", "monde"

print("Le résultat de la concaténation est :", resultat_final)