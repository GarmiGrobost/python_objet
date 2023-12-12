class Zoo:
    animaux = []
    nb_total_animaux = 0

    @classmethod
    def ajouter_animaux(cls, espece: str, nb_animaux: int):
        if espece not in cls.animaux:
            cls.animaux.append(espece)
        cls.nb_total_animaux += nb_animaux

    @classmethod
    def afficher_animaux(cls):
        print(cls.animaux)
        print(cls.nb_total_animaux)


Zoo.ajouter_animaux("Lion", 1)
Zoo.ajouter_animaux("Tigre", 1)
Zoo.ajouter_animaux("Elephant", 2)
Zoo.afficher_animaux()
