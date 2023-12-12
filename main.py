class AdressePostale:
    def __init__(self, numero_rue: int, libelle_rue: str, code_postal: str, ville: str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville


adresse1 = AdressePostale(18, "Rue Pierre", 27200, "Gisors")
adresse2 = AdressePostale(12, "Rue Danton", 78100, "Plaisir")


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def afficher_identite(self):
        print(f"Je m'appelle {self.nom.upper()} {self.prenom}")

    def set_nom(self, nom: str):
        self.nom = nom

    def set_prenom(self, prenom: str):
        self.prenom = prenom

    def set_adresse(self, adresse: AdressePostale):
        self.adresse = adresse

    def get_nom(self, nom: str):
        return self.nom

    def get_prenom(self, prenom: str):
        return self.prenom

    def get_adresse(self, adresse: AdressePostale):
        return self.adresse

    def afficher(self):
        print(self.nom, self.prenom, self.adresse.numero_rue, self.adresse.libelle_rue, self.adresse.code_postal,
              self.adresse.ville)


personne1 = Personne("Poisson", "David", adresse1)
personne2 = Personne("DUPONT", "Raja", adresse2)
print(personne1.afficher_identite())
personne1.set_prenom("Amin")
print(personne1.afficher_identite())
