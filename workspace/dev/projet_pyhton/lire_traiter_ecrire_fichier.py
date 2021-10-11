#!/usr/bin/python3
#
# @File : lire_traiter_ecrire_fichier.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 01/10/2021
#
# @Version : V1.0
#
# @Synopsis : 
#       
#       Ouverture d'un fichier en lecture : open(fichier, "r")
#           => Méthodes readline()
#       Méthode de modification des listes : replace(), lower()
#       Ouverture d'un fichier en écriture : open(fichier, "w") ou open(fichier, "a")
#           => Méthode write()
#

# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================

import datetime

# =============================================================================
# DECLARATION DES VARIABLES GLOBALES
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat(" ", "minutes")

### Configuration
repEntree = "/home/gyom/GD_W®12x/gd_workspace/dev/repositories/SIO2-SLAM-Cybersecurite/workspace/database" # Chemin du repertoire d'entree
repSortie = "/home/gyom/GD_W®12x/gd_workspace/dev/repositories/SIO2-SLAM-Cybersecurite/workspace/tmp" # Chemin du repertoire de sortie
#nom_fichier = 'agile.txt'
nom_fichier = 'villes_guadeloupe.csv'
fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.' + date # Chemin complet vers le fichier de sortie


# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

def lire_traiter_ecrire_fichier(fEntree, fSortie):
    """
    Ouvir le fichier fichEntree, le parcourir ligne par ligne, effectuer un traitement sur le contenu de 
    la ligne courante puis écrire le résultat dans le fichier de sortie fichSortie
    """

    with open(fSortie, "w") as filout: # Ouvir le fichier de sortie en écriture
        
        with open(fEntree, "r") as filin:  # Ouvrir le fichier d'entrée en lecture
            
            strLigne = filin.readline()  # La méthode readline() lis la premiere ligne du fichier et fait pointer filin sur la ligne suivante 
            
            # TRAITEMENT A FAIRE (initialisation avant le while) :
            strNewLigne  = strLigne.replace('a', 'z').replace('e', 'o').lower() # Remplacer des carateres et mettre en minuscule
            filout.write(strNewLigne) # Ecrire la ligne traitée dans le fichier de sortie

            while strLigne != "":                    # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")
       
                strLigne = filin.readline() # Recuperer la ligne courante du ficher et on la stack dans strLigne
                    
                # TRAITEMENT A FAIRE à chaque itération :
                strNewLigne  = strLigne.replace('a', 'z').replace('e', 'o').lower() # Remplacer des carateres et mettre en minuscule
                filout.write(strNewLigne) # Ecrire la ligne traitée dans le fichier de sortie
    
    # return foo # Suivant le traitement on mettra ou non un return

##############################################################################
# MAIN : Partie principal du programme
##############################################################################

lire_traiter_ecrire_fichier(fichEntree, fichSortie)
print("\nfichier généré : \n", fichSortie)

