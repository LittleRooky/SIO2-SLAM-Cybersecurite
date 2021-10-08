
#!/usr/bin/python3

# =============================================================================
# Importation des librairies
# =============================================================================

import csv
import datetime

# =============================================================================
# Déclaration des variables globales
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat(" ", "minutes")

### Configuration
repEntree = "/home/gd/Workspace/dev/SIO2-SLAM-Cybersecurite/workspace/database" # Chemin du repertoire d'entree
repSortie = "/home/gd/Workspace/dev/SIO2-SLAM-Cybersecurite/workspace/tmp" # Chemin du repertoire de sortie
#nom_fichier = 'agile.txt'
nom_fichier = 'villes_guadeloupe.csv'
fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.' + date # Chemin complet vers le fichier de sortie

# =============================================================================
# Declaration des fonctions
# =============================================================================

### Methode 1 avec read : Fichier ==> chaine de caractere
def ouvir_fichier_read(fichier):
    """
    Ouvir fichier et stocker tout son contenu dans une chaine de caractere.
    Méthode classique d'ouverture de fichier.
    """

    filin = open(fichier, 'r')  # Ouverture du fichier, filin est un descripteur de fichier
    strFichier = filin.read()   # Appel la méthode read() de l'objet filin
    filin.close()               # Fermeture du fichier  
 
    return strFichier           # Retourne la variable de type chaine de caratere (string) contenant le

### Methode 1bis (pour info) avec read :  Fichier ==> chaine de caractere (string)
def ouvir_fichier_read_bis(fichier):
    """
    Ouvir fichier et stocker tout son contenu dans une chaine de caractere.
    Methode "with open" pour ouvrir le fichier. Pas besoin de le clore avec filin.close().
    """

    with open(fichier, "r") as filin:  # Methode alternative d'ouverture du fichier (pas besoin de clore le fichier)
        strFichier = filin.read()      # Appel la méthode read() de l'objet filin  

    return strFichier                  # Retourne la variable de type chaine de caratere (string) contenant le

### Methode 2 (pour info) avec readline : Fichier ==> ligne par ligne dans une chaine de caractere
def ouvir_fichier_readline(fichier):
    """
    Ouvir fichier, le parcourir ligne par ligne et stocker le contenu de la ligne courante dans une chaine de caractere
    """
    with open(fichier, "r") as filin:   # Ouvrir le fichier, filin est un descripteur de fichier
        strLigne = filin.readline()     # La méthode readline() lis la premiere ligne du fichier et fait pointer filin sur la ligne suivante 
        while strLigne != "":           # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")
            strLigne = filin.readline() # Recuperer la ligne courante du ficher et on la stock dans strLigne
    
    # return strLigne                   # Le return ici n'est pas trés utile car strLigne ne contient que ""

### Methode 2bis avec readline : Fichier ==> chaque ligne du ficher dans une colonne de tableau (liste)
def ouvir_fichier_readline_tab(fichier):
    """
    Ouvir fichier, le parcourir ligne par ligne et stocker ajouter la ligne courante a la fin tableau
    """
    lstFichier = []                         # Déclaration d'un tableau vide
    with open(fichier, "r") as filin:       # Ouvrir du fichier, filin est un descripteur de fichier      
        strLigne = filin.readline().rstrip()          # La méthode readline() lis la premiere ligne du fichier et fait pointer filin sur la ligne suivante 
        lstFichier.append(strLigne)         # Ajouter avec append la ligne courante a la fin du tableau
        while strLigne != "":               # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")
            strLigne = filin.readline().rstrip()     # Recuperer la ligne courante du ficher et on la stack dans strLigne
            lstFichier.append(strLigne)     # Ajouter avec append la ligne courante a la fin du tableau
    return lstFichier                       # Retourner lstFichier, un tableau de chaine de caractere contenant toute les lignes du fichier

### Methode 3 avec readlines : Fichier ==> chaque ligne du ficher dans une colonne de tableau (liste)
def ouvir_fichier_readlines(fichier):
    """
    Ouvrir le fichier et placer directement chaque ligne du fichier dans une case de tableau
    """
    with open(fichEntree, 'r') as filin:
        strFichier = filin.readlines()  # La methode readlines placer directement chaque ligne du fichier dans une case de tableau

    return strFichier

##############################################################################
# MAIN : Partie principal du programme
##############################################################################
""" 
C'est ici que se trouve la partie principale du code. Dans cette partie on va, 
suivant notre besoin, appeller toutes les fonctions et variables déclarées ci-dessus.
"""

### READ() 
print("\nMethode 1 avec read : Fichier ==> chaine de caractere :\n")
fichier_string = ouvir_fichier_read(fichEntree)
print(fichier_string)
print("type de la variable :", type(fichier_string))

### READLINE
print("\nMethode 2bis avec readline :\n")
fichier_liste = ouvir_fichier_readline_tab(fichEntree)
print(fichier_liste)
print("type de la variable :", type(fichier_liste))

### READLINES
print("\nMethode 3 avec readlines :\n")
fichier_liste2 = ouvir_fichier_readlines(fichEntree)
print(fichier_liste2)
print("type de la variable :", type(fichier_liste2))

#print(ouvir_fichier_read_bis.doc)