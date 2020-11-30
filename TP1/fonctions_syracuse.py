# -*- coding: utf-8 -*-
"""
    Objectif : Etudier la suite de Syracuse
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

def syracuse(N):
    """
    But : calculer la suite de syracuse
    Entrées : n = un entier (int)
    Sortie : liste (suite de syracuse) jusqu'au premier 1
    """
    
    S = [N] #Initialisation de notre suite de Syracuse
    
    while N != 1:
        if N%2 == 0:
            N = N / 2
            S.append(N)
        
        else:
            N = (N * 3) + 1
            S.append(N)
    
    return S

def altitude(S):
    """
    But : trouver l'altitude maximal d'une suite de Syracuse
    Entrées : S = suite de Syracuse (liste)
    Sortie : altitude maximal (int)
    """
    
    return max(S)

def temps_de_vol(S):
    """
    But : trouver le temps de vol d'une suite de Syracuse
    Entrées : S = suite de Syracuse (liste)
    Sortie : temps de vol (int)
    """
    
    return len(S)-1