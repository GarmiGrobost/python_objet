class AdressePostale:
    def __init__(self, numero_rue: int, libelle_rue: str, code_postal: str, ville: str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville

    def __str__(self):
        return f"Numero:{self.numero_rue} Rue:{self.libelle_rue} Cp:{self.code_postal} Ville:{self.ville}"

    def __repr__(self):
        return f"Numero: {self.numero_rue} Rue:{self.libelle_rue} Cp:{self.code_postal} Ville:{self.ville}"

    def __eq__(self, other):
        if not isinstance(other, AdressePostale):
            return False
        return self.numero_rue == other.numero_rue and self.libelle_rue == other.libelle_rue and self.code_postal == other.code_postal and self.ville == other.ville


adresse1 = AdressePostale(18, "Rue Pierre", 27200, "Gisors")
adresse2 = AdressePostale(12, "Rue Danton", 27200, "Gisors")
adresse3 = AdressePostale(24, "Rue libre", 37000, "Montpellier")


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

    def __str__(self):
        return f"Nom :{self.nom} Prenom :{self.prenom}"

    def __repr__(self):
        return f"Prenom :{self.prenom} Nom :{self.nom} Adresse :{self.adresse}"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self.nom == other.nom and self.prenom == other.prenom and self.adresse == other.adresse


personne1 = Personne("DUPONT", "David", adresse1)
personne2 = Personne("DUPONT", "David", adresse2)
personne3 = Personne("GUEDJI", "David", adresse3)
liste_personne = [personne1]
print(str(personne1))
print(repr(personne2))
print(str(liste_personne))
print(personne1 == personne2)
