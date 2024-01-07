class Livre:

    def __init__(self, titre, auteur, achetable=False):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable

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

    @property
    def achetable(self):
        return self._achetable

    @achetable.setter
    def achetable(self, achetable):
        self._achetable = achetable

    def afficher_infos(self):
        return f"Titre :{self._titre}, Auteur : {self._auteur}, Achetable :{self._achetable}"


livre1 = Livre("L'espoir", "Buda")
livre1.titre = "La Finance"
livre1.auteur = "Assane"


# print(livre1.afficher_infos())


class LivrePapier(Livre):

    def __init__(self, titre, auteur, etat, achetable):
        super().__init__(titre, auteur, achetable)
        self._etat = etat

    @property
    def etat(self):
        return self._etat

    @etat.setter
    def etat(self, etat):
        self._etat = etat

    def afficher_infos(self):
        return super().afficher_infos() + f", Etat :{self._etat}"


class LivreNumerique(Livre):

    def __init__(self, titre, auteur, format, achetable):
        super().__init__(titre, auteur, achetable)
        self._format = format

    def afficher_infos(self):
        return super().afficher_infos() + f", Format : {self._format}"

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format):
        self._format = format


if __name__ == "__main__":
    livre_papier1 = LivrePapier("L'enfant noir", "Camara Laye", "moyen", True)
    livre_papier2 = LivrePapier("Le dauphin", "Binjamin", "occasion", False)
    livre_numerique1 = LivreNumerique("La richesse", "Charles", "PDF", True)
    livre_numerique2 = LivreNumerique("Le fleuve", "Jacques", "kindle", True)
    liste_livres = [livre_papier1, livre_papier2, livre_numerique1, livre_numerique2]
    for livre in liste_livres:
        print(livre.afficher_infos())
