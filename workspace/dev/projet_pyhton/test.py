import datetime

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat("-", "minutes")

### Configuration
repEntree = "workspace/database" # Chemin du repertoire d'entree
repSortie = "workspace/tmp" # Chemin du repertoire de sortie

#nom_fichier = 'agile.txt'
nom_fichier = 'villes_guadeloupe.csv'
fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.txt' # Chemin complet vers le fichier de sortie


# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

def lire_traiter_ecrire_fichier(fEntree, fSortie):
    """
    Ouvir le fichier fichEntree, le parcourir ligne par ligne, effectuer un traitement sur le contenu de 
    la ligne courante puis écrire le résultat dans le fichier de sortie fichSortie
    """

    # test = open((fSortie+'.txt'), "x")
    # test2 = open(fEntree, "r")
    # print(test2.readline())
    # test.write('tzqt s  s')
    # test.close()

    with open(fSortie, "w") as filout: # Ouvir le fichier de sortie en écriture
        
        with open(fEntree, "r") as filin:  # Ouvrir le fichier d'entrée en lecture
            
            strLigne = filin.readline()  # La méthode readline() lis la premiere ligne du fichier et fait pointer filin sur la ligne suivante 
            
            # TRAITEMENT A FAIRE (initialisation avant le while) :
            strNewLigne  = strLigne # Remplacer des carateres et mettre en minuscule
            filout.write(strNewLigne) # Ecrire la ligne traitée dans le fichier de sortie

            while strLigne != "": # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")
       
                strLigne = filin.readline() # Recuperer la ligne courante du ficher et on la stack dans strLigne
                    
                # TRAITEMENT A FAIRE à chaque itération :
                tabNewLigne  = strLigne.split(';') # Remplacer des carateres et mettre en minuscule
                if tabNewLigne != ['']:
                    print(tabNewLigne[2] + ' | ' + tabNewLigne[5])
                    filout.write(tabNewLigne[2] + ' | ' + tabNewLigne[5] + '\n') # Ecrire la ligne traitée dans le fichier de sortie
    
    # return foo # Suivant le traitement on mettra ou non un return


lire_traiter_ecrire_fichier(fichEntree, fichSortie)
# print("\nfichier généré : \n", fichSortie)