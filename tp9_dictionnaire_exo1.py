dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}
# Mettre en place une boucle pour afficher l'ensemble des clés contenues dans le
# dictionnaire
for k in dicoVilles:
    print(k)

# Mettre en place une boucle pour afficher l'ensemble des valeurs contenues dans le
# dictionnaire
for v in dicoVilles:
    print(dicoVilles.get(v))

# Afficher la taille du dictionnaire
print(len(dicoVilles))
