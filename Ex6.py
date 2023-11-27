x = 5 # déclaration de la variable x à l'intérieur de la fonction

def addition(a, b): #déclaration de la fonction addition

    global x

    x = 10 #modification de la valeur de x à 10

    result = a + b + x
    return result

resultat_final = addition(3, 2) #Appel de la fonction avec les arguments 3 et 2

print("Le résultat final de l'addition =", resultat_final)

