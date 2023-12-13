class Livre:

    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._achetable = False

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, titre):
        self._titre = titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur


livre1 = Livre("L'espoir", "Buda")
livre1.titre = "La Finance"
livre1.auteur = "Assane"
print(f"Titre :{livre1.titre }, Auteur: {livre1.auteur}")
