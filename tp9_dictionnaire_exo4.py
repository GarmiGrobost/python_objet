class Salaries():
    def __init__(self, nom, matricule, service):
        self._nom = nom
        self._matricule = matricule
        self._service = service

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, matricule):
        self._matricule = matricule

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = service

    def __str__(self):
        return f"Nom :{self._nom} Matricule :{self._matricule} Service :{self._service}"


s1 = Salaries("Antoine Dupont", 127, "DSI/JAVA")
s2 = Salaries("Berthe Casa", 238, "DSI/PHP")
s3 = Salaries("Fatima Ouassa", 478, "DSI/JAVA")
s4 = Salaries("Cassian Andor", 156, "DSI/PYTHON")
s5 = Salaries("Lee Wu", 559, "DSI/PHP")
s6 = Salaries("Hassan Missen", 96, "DSI/PYTHON")
s7 = Salaries("Aurélien PIC", 889, "DSI/JAVA")
liste_salaries = [s1, s2, s3, s4, s5, s6, s7]

comptage_salaries_par_service = {}
for salarie in liste_salaries:
    if salarie.service in comptage_salaries_par_service:
        comptage_salaries_par_service[salarie.service] += 1
    else:
        comptage_salaries_par_service[salarie.service] = 1

print(comptage_salaries_par_service)
