
def afficher_dico2(keys: list):
    return {key: keys.count(key) for key in keys}


print(afficher_dico2(["Ananas", "Banane", "Orange", "Ananas", "Banane"]))
