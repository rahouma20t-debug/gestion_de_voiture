class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None


    def afficherInformations(self):
        print("Employe:", self.nom, self.prenom)
        print("Permis:", self.numeroPermis)

        if self.voitureService:
            print("Voiture:", self.voitureService.marque)
        else:
            print("Pas de voiture")


    def affecterVoiture(self, voiture):
        if self.voitureService is None and voiture.chauffeur is None:
            self.voitureService = voiture
            voiture.chauffeur = self
        else:
            print("Impossible d'affecter cette voiture")


    def retirerVoiture(self):
        if self.voitureService:
            self.voitureService.chauffeur = None
            self.voitureService = None