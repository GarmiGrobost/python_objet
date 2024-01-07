class PersonneException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: str):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse

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


class PersonneService:

    @staticmethod
    def valider(personne):
        if not personne.nom:
            raise PersonneException("Le nom est obligatoire")
        if len(personne.nom.strip()) < 2:
            raise PersonneException("Le nom doit faire au moins 2 caractères.")
        if not personne.prenom:
            raise PersonneException("Le prénom n'est pas renseigné")
        if len(personne.prenom.strip()) < 2:
            raise PersonneException("Le prénom doit faire au moins 2 caractères.")
        if not personne.adresse:
            raise PersonneException("L'adresse doit être renseigné")


# Créer des instances de Personne avec ou sans erreurs
personnes = [Personne("", "Marcel", "1 rue de la Paix"), Personne("D", "Jean", "2 rue de la Liberté"),
             Personne("Martin", "", "18 rue de la libération"), Personne("Poisson", "Sophie", ""), Personne("Durand", "Sophie", "3 rue de la Joie")]
# Mettre en œuvre la méthode valider avec try / catch / else pour vérifier que les bons messages d'erreur sont affichés
for personne in personnes:
    try:
        PersonneService.valider(personne)
    except PersonneException as e:
        print(f"Erreur: {e}")
    else:
        print("Personne valide.")
