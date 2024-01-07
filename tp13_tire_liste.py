class AdressePostale:
    def __init__(self, numero_rue: int, libelle_rue: str, code_postal: str, ville: str):
        self._numero_rue = numero_rue
        self._libelle_rue = libelle_rue
        self._code_postal = code_postal
        self._ville = ville

    @property
    def numero_rue(self):
        return self._numero_rue

    @numero_rue.setter
    def nom(self, numero_rue):
        self._numero_rue = numero_rue

    @property
    def libelle_rue(self):
        return self._libelle_rue

    @libelle_rue.setter
    def libelle_rue(self, libelle_rue):
        self._libelle_rue = libelle_rue

    @property
    def code_postal(self):
        return self._code_postal

    @code_postal.setter
    def code_postal(self, code_postal):
        self._code_postal = code_postal

    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, ville):
        self._ville = ville

    def __str__(self):
        return f"Numero:{self._numero_rue} Rue:{self._libelle_rue} Cp:{self._code_postal} Ville:{self._ville}"

    def __repr__(self):
        return f"Numero: {self._numero_rue} Rue:{self._libelle_rue} Cp:{self._code_postal} Ville:{self._ville}"

    def __eq__(self, other):
        if not isinstance(other, AdressePostale):
            return False
        return self._numero_rue == other._numero_rue and self._libelle_rue == other._libelle_rue and self._code_postal == other._code_postal and self._ville == other._ville

    def __hash__(self):
        return hash((self._numero_rue, self._libelle_rue, self._code_postal, self._ville))


adresse1 = AdressePostale(18, "Rue Pierre", 27200, "Gisors")
adresse2 = AdressePostale(12, "Rue Danton", 27200, "Gisors")
adresse3 = AdressePostale(24, "Rue libre", 37000, "Montpellier")


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse

    def afficher_identite(self):
        print(f"Je m'appelle {self._nom.upper()} {self._prenom}")

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, adresse):
        self._adresse = adresse

    def __str__(self):
        return f"Nom :{self._nom} Prenom :{self._prenom} Adresse : {self._adresse}"

    def __repr__(self):
        return f"Prenom :{self._prenom} Nom :{self._nom} Adresse :{self._adresse}"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self._nom == other._nom and self._prenom == other._prenom and self._adresse == other._adresse

    def __hash__(self):
        return hash((self._nom, self._prenom, self._adresse))


personne1 = Personne("BAMBA", "David", adresse1)
personne2 = Personne("POISSON", "Marie", adresse2)
personne3 = Personne("DABY", "Sophie", adresse3)
liste_personne = [personne1, personne2, personne3]


def tri_nom(personne):
    return personne.nom


liste_trie = sorted(liste_personne, key=tri_nom)
for t in liste_trie:
    print(t)
