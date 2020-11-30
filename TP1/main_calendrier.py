# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Vvalidité d'une date
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

import fonctions_calendrier as calendrier

jour = int(input('rentrer le jour de votre date :'))
mois = int(input('rentrer le mois de votre date :'))
annee = int(input('rentrer l\'année de votre date :'))

def date_valide_final(jour,mois,annee):
    """
    But : vérifier la validité d'une date et afficher le message souhaité en fonction
    Entrée : jour = le jour (int) de la date à vérifier
            mois = le mois (int) de la date à vérifier
            annee = l'annee (int) de la date à vérifier
    Sortie : "date valide" ou "date non valide"
    """
    
    if calendrier.date_valide(jour,mois,annee):
        return "date valide"
    
    return "date non valide"

print(date_valide_final(jour,mois,annee))