from abc import ABC, abstractmethod
from tp6_redef_heritage import LivrePapier, LivreNumerique


class Sortie(ABC):
    def __init__(self, date, livre):
        self._date = date
        self._livre = livre

    @abstractmethod
    def get_montant(self):
        pass


class Emprunt(Sortie):

    def __init__(self, date, livre, duree_emprunt):
        super().__init__(date, livre)
        self._duree_emprunt = duree_emprunt

    def get_montant(self):
        if isinstance(self._livre, LivrePapier):
            return self._duree_emprunt * 0.5
        elif isinstance(self._livre, LivreNumerique):
            return self._duree_emprunt * 0.25
        else:
            return 0


class Achat(Sortie):
    def __init__(self, date, livre, montant):
        super().__init__(date, livre)
        self._montant = montant

    def get_montant(self):
        if isinstance(self._livre, LivrePapier):
            return self._montant
        elif isinstance(self._livre, LivreNumerique):
            return self._montant
        else:
            return 0

    def __str__(self):
        return f"{super().__str__()} _ Montant : {self._montant}"


livre1 = Emprunt("Le 12 Décembre 2023", LivrePapier("L'enfant noir", "Camara Laye", "moyen", True), 15)
livre2 = Achat("Le 15 Novembre 2023", LivreNumerique("La richesse", "Charles", "PDF", True), 125)
liste_sorties = [livre1, livre2]


def montant_total():
    return sum(l.get_montant() for l in liste_sorties)


print("Montant global des sorties : ", montant_total())


def montant_total_par_type(liste_sorties):
    montants = {'achat': 0, 'emprunt': 0}
    for sortie in liste_sorties:
        if isinstance(sortie, Achat):
            montants['achat'] += sortie.get_montant()
        elif isinstance(sortie, Emprunt):
            montants['emprunt'] += sortie.get_montant()
    return montants


print(montant_total_par_type(liste_sorties))
