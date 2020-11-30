# -*- coding: utf-8 -*-

"""
Header:
    Objectif : Mettre en place les fonctions qui permettront de vérifier 
            la validité d'une date
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

def bissextile(annee):
    """
    But : vérifier qu'une année est bissextile ou non
    Entrée : annee = une année (int)
    Sortie : un booléen (True si l'année est bissextile, False sinon)
    """
    
    if annee%100 == 0: #Si annee finit par 00
        return annee%400 == 0 #Si annee est un multiple de 400 -> rend True (False sinon)
    else:
        return annee%4==0 #Si annee est un multiple de 4 -> rend True (False sinon)

def nb_de_jour(mois, annee):
    """
    But : rendre le nombre de jour dans le mois
    Entrée : mois = le numéro d'un mois (int) compris normalement entre 1 et 12
            annee = l'annee (int)
    Sortie : le nombre de jour du mois correspondant à l'entrée (int)
    """
    
    mois_31 = [1,3,5,7,8,10,12] #Liste des mois de 31 jours
    mois_30 = [4,6,9,11] #Liste des mois de 30 jours
    
    if mois <= 12 and mois >= 1: #Vérification validité du paramètre d'entrée
        
        if mois in mois_31:
            return 31
        
        elif mois in mois_30:
            return 30
        
        else: #Il ne reste comme seul possibilité 2 (février) grâce à la
            #la vérification faite au début.
            if bissextile(annee): #Si l'annee est bissextile
                return 29
            return 28 #Si elle n'est pas bissextile février possède 28 jours
    
    return False #Renvoyer s'il y a un problème dans les paramètres d'entrées

def date_valide(jour,mois,annee):
    """
    But : vérifier la validité d'une date
    Entrée : jour = le jour (int) de la date à vérifier
            mois = le mois (int) de la date à vérifier
            annee = l'annee (int) de la date à vérifier
    Sortie : un booléen (True si date valide, False sinon)
    """
    if nb_de_jour(mois, annee) == False:
        return False
    
    if jour <= nb_de_jour(mois, annee) and jour > 0: #vérification que le nombre le jour est logique
        return True
    
    return False #Rend False en cas d'érreur sur le mois (vérifié dans la fonction nb_de_jour)
                #ou le jour

