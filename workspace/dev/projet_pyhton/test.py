#!/usr/bin/python3

import csv


import datetime
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat(" ", "minutes")
print(date)

#chemin_rep = "../../database"
repEntree = "/home/gd/Workspace/dev/SIO2-SLAM-Cybersecurite/workspace/database"
repSortie = "/home/gd/Workspace/dev/SIO2-SLAM-Cybersecurite/workspace/tmp"

nom_fichier = 'liste_eleves.csv'
#nom_fichier = 'dico_donnees.csv'

fichEntree = repEntree + '/' + nom_fichier
fichSortie = repSortie + '/' + nom_fichier + '.' + str(date)

print(fichEntree)
print(fichSortie)


# # 1 #### Chaine de caractere (string)
# filin = open(fichier_entree, 'r')
# contenu = filin.read()
# filin.close()
# #print(type(contenu))

# # 2 #### Readline => Ligne par ligne du fichier dans une chaine de caractere (string)
# with open(fichier_entree, "r") as filin:
#     ligne = filin.readline()
#     while ligne != "":
#         #print(ligne)
#         #print(type(ligne))
#         ligne = filin.readline()
# #print(type(ligne))

# 3 #### Readlines => Tout le fichier dans une liste
with open(fichEntree, 'r') as filin:
    contenu2 = filin.readlines()

print(len(contenu2))
print("Avant", contenu2)


with open(fichSortie, 'w') as filout:

    for i in range(len(contenu2)):
        nligne = contenu2[i].replace('\n', '').replace('" ', '"').replace(' "', '"').lower()
        contenu2[i] = nligne
        filout.write(nligne + '\n')


print("Apres", contenu2)


print("ouverture fichier")

try:
    filin=open(fichSortie, "r")
    print("ouverture csv")
except:
    print("Le fichier", fichSortie, "est introuvable")
        
tableData=list(csv.reader(filin,delimiter=";"))

print(tableData)
print(len(tableData[0]))