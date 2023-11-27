def app_fonction(liste, fonction): #déclaration de la fonction 

    resultat = [fonction(element) for element in liste]
    return resultat

the_list = [1, 2, 3, 4, 5]

def carre(x):   # Définition de la fonction qui élève au carré
    return x**2

resultat_final = app_fonction(the_list, carre) #application de la fonction carré à chaque élément de la liste

print("La liste initiale :", the_list)
print("Résultat :", resultat_final)