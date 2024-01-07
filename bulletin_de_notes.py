class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Note:
    def __init__(self, valeur, date, categorie):
        self.valeur = valeur
        self.date = date
        self.categorie = categorie


class Discipline:
    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes

    def calculer_moyenne(self):
        return sum(note.valeur for note in self.notes) / len(self.notes)


class Bulletin:
    def __init__(self, etudiant, disciplines):
        self.etudiant = etudiant
        self.disciplines = disciplines

    def calculer_moyenne(self):
        return [discipline.calculer_moyenne() for discipline in self.disciplines]

    def afficher_moyenne(self):
        for discipline in self.disciplines:
            print(f"{discipline.nom}: {discipline.calculer_moyenne()}")


etudiant = Etudiant("Dupont", "Jean")
notes_maths = [Note(12, "01/01/2022", "DS1"), Note(14, "01/02/2022", "DS2")]
notes_physique = [Note(10, "01/01/2022", "DS1"), Note(16, "01/02/2022", "DS2")]
discipline_maths = Discipline("Mathématiques", notes_maths)
discipline_physique = Discipline("Physique", notes_physique)
bulletin = Bulletin(etudiant, [discipline_maths, discipline_physique])
bulletin.afficher_moyenne()
