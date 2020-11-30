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
    Entrée : Rien
    Sortie : 'Gagné' ou 'Perdu' (str) -> le résultat de la partie
    """
    
    chances = 8 #On définie le nombre d'erreur autorisé
    victoire = False #True si le joueur gagne
    
    mot = fct.determination_mot()
    
    affichage = fct.initialisation_affichage_mot(mot)
    
    print(affichage)
    
    while chances !=0 and victoire != True:
        
        lettre = input('Proposez une lettre : ')
        
        verification = fct.verification_lettre_dans_mot(mot, lettre)
        
        if verification[0]:
            affichage = fct.actualiser_affichage_mot(affichage, lettre, verification[1])
            victoire = fct.verification_victoire(affichage)
            print(affichage)
        else:
            chances -= 1 #Si la lettre proposée n'est pas dans le mot, le joueur perds une chance.
            print(lettre + ' n\'est pas dans le mot')
            print('il vous reste ', chances, ' chances')
    
    if victoire:
        return 'Bravo vous avez trouvé. Le mot était bien : ', mot
    
    return 'Perdu, le mot était : ', mot