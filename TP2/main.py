# -*- coding: utf-8 -*-

"""
Header:
    Objectif : Concevoir un jeu du pendu
    Date de réalisation : 30/11/2020
    Par Elliot GARCIA (Gr C)
"""

import fonctions as fct

def jouer_au_pendu(listes_de_mots):
    """
    But : Programme principal qui va simuler dans la console un jeu du pendu
    Entrée : Le nom du fichier où est la liste de mot .txt
    Sortie : 'Gagné' ou 'Perdu' (str) -> le résultat de la partie
    """
    jouer = True
    meilleur_score = 0
    
    while jouer:
        chances = 8 #On définie le nombre d'erreur autorisé
        victoire = False #True si le joueur gagne
        
        nb_mots = fct.initialisation_list_mots(listes_de_mots)
        mot = fct.determination_mot(nb_mots)
        liste_lettre_dites = [[],[]]
        
        affichage = fct.initialisation_affichage_mot(mot)
        
        print(affichage)
        
        while chances !=0 and victoire != True:
            
            lettre = input('Proposez une lettre : ')
            
            liste_lettre_dites = fct.lettre_dite(liste_lettre_dites[1], lettre)
            verification = fct.verification_lettre_dans_mot(mot, lettre)
            
            if liste_lettre_dites[0]:
                print('Lettre déjà dites')
                
            elif verification[0]:
                affichage = fct.actualiser_affichage_mot(affichage, lettre, verification[1])
                victoire = fct.verification_victoire(affichage)
                print(affichage)
                
            else:
                chances -= 1 #Si la lettre proposée n'est pas dans le mot, le joueur perds une chance.
                print(lettre + ' n\'est pas dans le mot')
                print('il vous reste ', chances, ' chances')
        
        score = chances
        if victoire:
            print('Bravo vous avez trouvé. Le mot était bien : ' + mot)
        
            if score > meilleur_score:
                meilleur_score = score
        
        else: print('Perdu, le mot était : ', mot)
        
        print('Votre score est de ', score)
        
        rejouer = input('voulez-vous rejouer (oui/non) : ')
        if rejouer == 'non':
            jouer = False
    
    print('Votre meilleur score a été :')
    return meilleur_score