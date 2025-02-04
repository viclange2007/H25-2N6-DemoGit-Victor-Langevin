# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os
os.chdir("C:\\Users\\2469827\\OneDrive - Cégep Édouard-Montpetit\\Programmation 2\\R03 Exercices Depart\\Ex3 Videos")
for dossier in os.listdir() :
    extension = os.path.splitext(dossier)[1]
    filename = os.path.splitext(dossier)[0]
    nom = filename.split("_")
    titre = nom[0]
    cours = nom[1]
    numero = nom[2]
    titre2 = titre.strip(" ")
    numero2 = numero.strip(" ")
    numero4 = numero2[1:]
    print(titre2)
    print(cours)
    print(numero2)
    numero3 = numero4.zfill(2)
    print(numero3)
os.rename("Ex3 Videos", "fnsjafna")
    