def afficher_dico(keys: list):
    return {key: len(key) for key in keys}


print(afficher_dico(["coucou", "hi"]))
