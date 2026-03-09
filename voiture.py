class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None


    def afficher_Informations(self):
        print("Voiture:", self.marque)
        print("Matricule:", self.matricule)
        print("Année:", self.annee)
        print("Kilométrage:", self.kilometrage)

        if self.chauffeur:
            print("Chauffeur:", self.chauffeur.nom)
        else:
            print("Pas de chauffeur")