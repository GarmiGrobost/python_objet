class AdressePostale :

    def __init__(self, numero_rue:int, libelle_rue:str, code_postal:str, ville:str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville

adresse1 = AdressePostale(18, "Rue Pierre", 27200, "Gisors")
adresse2 = AdressePostale(12, "Rue Danton", 78100, "Plaisir")

class Personne :

    def __init__(self, nom:str, prenom:str, adresse:AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

personne1 = Personne("POISSON", "David", adresse1)
personne2 = Personne("DUPONT", "Rija", adresse2)

print(personne1.nom, personne1.prenom, personne1.adresse.numero_rue, personne1.adresse.libelle_rue, personne1.adresse.code_postal, personne1.adresse.ville)
print(personne2)
