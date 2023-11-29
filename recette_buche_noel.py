def preparer_genoise(qtite_farine, qtite_sucre, qtite_oeufs):
    # Instructions pour préparer la génoise
    print("Préparer la génoise")
    print(f"Ingrédients : farine, sucre, œufs")
    print(f"Quantités : {qtite_farine}g de farine, {qtite_sucre}g de sucre, {qtite_oeufs} œufs")
    temps_prepa = 20
    temps_cuisson = 15
    print(f"Temps de préparation : {temps_prepa} minutes")
    print(f"Temps de cuisson : {temps_cuisson} minutes")
    return temps_prepa + temps_cuisson

# Fonction pour préparer la crème au beurre
def preparer_creme_au_beurre(qtite_beurre, qtite_sucre_glace, extrait_vanille):
    # Instructions pour préparer la crème au beurre
    print("Préparer la crème au beurre")
    print("Ingrédients : beurre, sucre glace, extrait de vanille")
    print(f"Quantités : {qtite_beurre}g de beurre, {qtite_sucre_glace}g de sucre glace, {extrait_vanille} cuillère à café d'extrait de vanille")
    temps_prepa = 15
    print(f"Temps de préparation : {temps_prepa} minutes")
    return temps_prepa

# Fonction pour assembler la bûche
def assembler_buche(garniture):
    # Instructions pour assembler la bûche
    print("Assembler la bûche")
    print(f"garniture: {garniture}")
    tps_assemblage = 10
    print(f"Temps d'assemblage : {tps_assemblage} minutes")
    return tps_assemblage

# Fonction pour décorer la bûche
def decorer_buche(decoration):
    # Instructions pour décorer la bûche
    print("décorer cette putain de bûche")
    print(f"décoration : {decoration}")
    tps_deco = 15
    print(f"Temps de décoration : {tps_deco} minutes")
    return tps_deco

# Fonction principale pour créer la bûche de Noël
def creer_buche():
    # Définir les ingrédients nécessaires
    quantite_farine = 200
    quantite_sucre = 150
    quantite_oeufs = 4

    quantite_beurre = 250
    quantite_sucre_glace = 300
    extrait_vanille = 1

    garniture = "ganache au chocolat"
    decoration = "sucre glace, décorations en sucre"

     # Préparer la génoise
    temps_genoise = preparer_genoise(quantite_farine, quantite_sucre, quantite_oeufs)

    # Préparer la crème au beurre
    temps_creme = preparer_creme_au_beurre(quantite_beurre, quantite_sucre_glace, extrait_vanille)

    # Assembler la bûche
    temps_assemblage = assembler_buche(garniture)

    # Décorer la bûche
    temps_decoration = decorer_buche(decoration)

    # Calculer le temps total
    temps_total = temps_genoise + temps_creme + temps_assemblage + temps_decoration

    # Réfrigérer la bûche (étape facultative)
    print("Réfrigérer la bûche")

    # Servir la bûche
    print("Servir la bûche")

    # Afficher le temps total
    print(f"Temps total de préparation : {temps_total} minutes")

# Appeler la fonction principale pour créer la bûche de Noël
creer_buche()