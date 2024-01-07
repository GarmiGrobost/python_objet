chaine = "Durand;Marcel;2 523.5"

# Affichez le premier caractère de la chaine de caractères
premier_caractere = chaine[0]
print("Premier caractère: " + premier_caractere)

# Utilisez la fonction len() pour afficher la longueur de la chaine de caractères
print(len(chaine))

#  Utilisez la méthode index(c) pour afficher l’index du premier « ; » contenu dans la
# chaine de caractères.
print(chaine.index(";"))

#  Utilisez l’opérateur [indexmin :indexmax] pour extraire une portion de chaine de
# caractères comprise entre un index de début (inclus) et un index de fin (exclu)
print(chaine[7:13])

# Combinez la méthode index(c) et l’opérateur [indexmin :indexmax] pour extraire le
# nom de famille de la personne
index_point_virgule = chaine.index(";")
nom_de_famille = chaine[:index_point_virgule]
print(nom_de_famille)

# Utilisez la méthode upper() pour afficher le nom de famille en majuscules
up_nom_de_famille = nom_de_famille.upper()
print(up_nom_de_famille)

# Utilisez la méthode split(string) pour découper la chaine de caractères en morceaux.
liste_morceaux = chaine.split(";")
print(liste_morceaux)
