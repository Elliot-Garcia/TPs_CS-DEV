# -*- coding: utf-8 -*-

"""
Header:
    Objectif : Fonction de mise en oeuvre d'un jeu du pendu
    Date de réalisation : 30/11/2020
    Par Elliot GARCIA (Gr C)
"""

import random as rd
import os


def tri_list_mots():
    """
    But : Trier les mots dans les fichiers dans l'ordre alphabétique du plus petit au plus grand'
    Entrée : Rien
    Sortie : Rien
    """
    
    for nom_f in os.listdir('data/mots'):
        lien_f = 'data/mots/' + nom_f
        f = open(lien_f,'r')
        liste_mots = f.readlines()
        
        if len(liste_mots) != 0:
            
            l_mots_avc_taille = []
            f.close()
            
            for i in range(len(liste_mots)):
                
                taille_mot = len(liste_mots[i])
                nb_carac = taille_mot-1
                
                if nb_carac > 9:
                    
                    nb_carac = int('9'+str(nb_carac))
                    
                l_mots_avc_taille.append([str(nb_carac) + liste_mots[i].strip(), nb_carac])
            
            l_mots_avc_taille.sort()
            
            f = open(lien_f, 'w') #Supprime tout le contenu du .txt
            f.close()
            
            for i in range(len(l_mots_avc_taille)-1):
                
                nb_chiffre = len(str(l_mots_avc_taille[i][1]))
                f = open(lien_f, 'a')
                f.write(l_mots_avc_taille[i][0][nb_chiffre:] + '\n')
                f.close()
             
            nb_chiffre = len(str(l_mots_avc_taille[-1][1]))
            f = open(lien_f, 'a')
            f.write(l_mots_avc_taille[-1][0][nb_chiffre:])
            f.close()
        


def initialisation_list_mots(nom_fichier):
    """
    But : Initialiser la liste de mots d'un fichier
    Entrée : le nom de fichier .txt
    Sortie : Le nombre de mots dans le fichier
    """
    
    f = open(nom_fichier,'r')
    mots = f.readlines()
    nb_mots = len(mots)
    f.close()
    
    return nb_mots



def determination_mot(nb_mots, nom_fichier):
    """
    But : Choisir aléatoirement un mot dans 'mots.txt'
    Entrée : Nombre de mots dans le fichier et nom du fichier
    Sortie : Un mot du fichier 'mots.txt' (str)
    """
    
    n_mot = rd.randrange(0, nb_mots, 1)
    f = open(nom_fichier,'r')
    
    for i in range(n_mot):
        f.readline()
    
    mot = f.readline()
    f.close()
    
    return mot.strip()



def initialisation_affichage_mot(mot):
    """
    But : Afficher la première lettre du mot à faire deviner, puis des '_' pour les autres lettres
    Entrée : le mot choisi aléatoirement (str)
    Sortie : chaîne de caractère de la forme 'X _ _ _ _' où X est la première lettre du mot (str)
    """
    
    long_mot = len(mot)
    a_deviner = mot[0]
    
    for i in range(long_mot-1):
        a_deviner += ' _'
    
    return a_deviner



def verification_lettre_dans_mot(mot, lettre):
    """
    But : Vérifier que la lettre choisi et dans le mot
    Entrée : Le mot (str) et la lettre (str)
    Sortie : Liste avec : Booléen (True si la lettre est dans le mot, False sinon)
            et, si True, les indices des positions de la lettre dans le mot
    """
    
    long_mot = len(mot)
    position_lettre = []
    
    for i in range(1, long_mot):
        if lettre == mot[i]:
            position_lettre.append(i)
    
    return [len(position_lettre)!=0, position_lettre]



def lettre_dite(liste_lettre_dites, lettre):
    """
    But : vérifier si la lettre n'est pas dans la liste des lettres déjà dites
            si non, ajouter la lettre dite à la liste
    Entrée : liste des lettres déjà dites
            lettre rentrée au dernier tour (str)
    Sortie : Booléen (True si déjà dite, False sinon)
            et liste des lettres déjà dites actualisé
    """
    
    if lettre in liste_lettre_dites:
        return [True, liste_lettre_dites]
    
    else:
        liste_lettre_dites.append(lettre)
        return [False, liste_lettre_dites]



def actualiser_affichage_mot(affichage, lettre, position_lettre):
    """
    But : Remplacer les '_' par la lettre correspondante
    Entrée : Le mot à trou déjà afficher (str)
            la lettre qui doit combler certain trou (str)
            et la/les position/s de la lettre (liste)
    Sortie : chaîne de caractère corrspondant au nouvel affichage du mot combler par la lettre entrée
    """
    
    #Comme on a un espace tous les nombre paire pour l'affichage pour des raisons de lisibilité
    #on fera bien attention à convertir les coordonnées de la lettre en nombre pair
    
    nb_position = len(position_lettre)
    for i in range(nb_position):
        position_lettre_affichage = 2*position_lettre[i] #nombre pair pour tomber sur un '_'
        
        #On scinde l'affichage autour de l'endroit où l'on doit remplacer par la lettre
        aff_1 = affichage[0:position_lettre_affichage]
        aff_2 = affichage[position_lettre_affichage+1:]
        
        #On reconstitue l'affichage avec la lettre
        affichage = aff_1 + lettre + aff_2
    
    return affichage



def verification_victoire(affichage):
    """
    But : Vérifier si le joueur a trouvé toutes les lettres et donc si il a gagné
    Entrée : affichage du jeu en cours (str) qui affiche les lettres trouvés
    Sortie : Un booléen (True si toutes les lettres ont été trouvés, False sinon)
    """
    
    long_affichage = len(affichage)
    
    for i in range(long_affichage):
        
        if affichage[i] == '_': #Toutes les lettres trouvés signifie plus de trou
            return False
    
    return True