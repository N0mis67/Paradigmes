def app_fonction(list_fonction, valeur):

    results = [fonction(valeur) for fonction in list_fonction] # utilisation d'une compréhension de liste pour appliquer chaque fonction à la valeur
    return results

fonctions = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2] # Définition d'une liste de fonctions

final_results = app_fonction(fonctions, 3) # Application des fonctions à une valeur (le 3 est un exemple)

print("Résultats finaux", final_results)