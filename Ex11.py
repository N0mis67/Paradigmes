mtht = float(input("Entrez le montant hors taxe :")) #permet d'entrer une valeur pour le montant total hors taxe
tva = float(input("Entrez le taux de TVA :")) #permet d'entrer une valeur pour la tva

mttc = mtht * (1 + tva) #calcul du montant total net toutes taxes comprises 


if mttc < 100 : 
    nttc = mttc     # Si le mttc est inférieur à 100, alors le mttc à la même valeur que le nttc
else :
      if 100 < mttc < 200 : # Si le mttc est situé entre 100 et 200, alors le nttc = mttc x 0.85
           nttc = mttc * 0.85
      else : 
           nttc = mttc * 0.6 # Si le mttc est supérieur à 200, alors nttc = mttc x 0.6
    
print("nttc = ", nttc)  # Affichez le résultat