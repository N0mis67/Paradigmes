import time

def mesure_temps(fonction):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        duree = fin - debut
        print(f"Temps d'exécution de {fonction.__name__}: {duree} secondes")
        return resultat
    return wrapper

@mesure_temps
def fonction_simule_delai():
    print("début")
    time.sleep(5)
    print("fin")

fonction_simule_delai()
    