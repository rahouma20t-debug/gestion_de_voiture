from employe import Employe
from voiture import Voiture


e1 = Employe("12345", "Difi", "Nouah")
e2 = Employe("67890", "Chirifi", "Hasna")


v1 = Voiture("Ab12C3", 2022, "Toyota", 10000)
v2 = Voiture("BR14Q6", 2021, "Bmw", 20000)


e1.afficherInformations()
v1.afficher_Informations()


print("------ Affectation voiture ------")

e1.affecterVoiture(v1)

e1.afficherInformations()
v1.afficher_Informations()


print("------ Retirer voiture ------")

e1.retirerVoiture()

e1.afficherInformations()

# commit 3
