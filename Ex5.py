def remplace_maj(chaine):
   
    # Utilisation de la compréhension de chaîne pour remplacer chaque lettre majuscule par un tiret
    chaine_modif = ''.join(['-' if lettre.isupper() else lettre for lettre in chaine])
    
    return chaine_modif

# Exemple d'utilisation
ma_chaine = "Bonjour Le Monde"
chaine_modif = remplace_maj(ma_chaine)
print("Chaîne initiale :", ma_chaine)
print("Chaîne modifiée :", chaine_modif)