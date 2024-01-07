class Theatre:
    def __init__(self, nom, capacite_max):
        self._nom = nom
        self._capacite_max = capacite_max
        self._total_clients_inscrits = 0
        self._recette_totale = 0

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def capacite_max(self):
        return self._capacite_max

    @capacite_max.setter
    def capacite_max(self, capacite_max):
        self._capacite_max = capacite_max

    @property
    def recette_totale(self):
        return self._recette_totale

    @recette_totale.setter
    def recette_totale(self, recette_totale):
        self._recette_totale = recette_totale

    def __str__(self):
        return f"Nom: {self._nom} - Capacité maximale: {self._capacite_max}"

    def inscrire(self, nbre_clients, prix_place):
        if self._total_clients_inscrits + nbre_clients < self._capacite_max:
            self._total_clients_inscrits += nbre_clients
            self._recette_totale += nbre_clients * prix_place
        else:
            print("La capacité maximale du théâtre est atteinte. Impossible d'inscrire plus de clients.")

    @property
    def total_clients_inscrits(self):
        return self._total_clients_inscrits


# Créer une instance de Theatre
th1 = Theatre("Théatre de la mer", 150)
print(th1)

# Appeler plusieurs fois la méthode inscrire jusqu'à obtention du message d'erreur
th1.inscrire(50, 10.0)
th1.inscrire(30, 10.0)
th1.inscrire(30, 10.0)
th1.inscrire(50, 10.0)

# Afficher le total de clients inscrits
print(f"Total des clients inscrits : {th1.total_clients_inscrits}")
# Afficher la recette totale de l'établissement
print(f"Recette totale de l'établissement: {th1.recette_totale}")
