def app_fois_deux(fonction):

    def new_fonction(x):

        resultat = fonction(fonction(x)) #Application de la fonction d'entrée deux fois à l'argument x
        return resultat
    
    return new_fonction


def multi_fois_deux(x): #définition d'une fonction qui multiplie par 2
    return x * 2

double_fonction = app_fois_deux(multi_fois_deux) #application de la fonction app_fois_deux à la fonction multi_fois_deux

resultat_final = double_fonction(5) #utilisation de la nouvelle fonction

print("Résultat :", resultat_final)