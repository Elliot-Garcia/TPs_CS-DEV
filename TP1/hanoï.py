# -*- coding: utf-8 -*-
"""
    Objectif : Résoudre le problème des tours d'Hanoï
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""


def hanoi(n,x=1,y=2,z=3,deplacement=0):
    """
    But : résoudre le problème des tours d'Hanoï de façon récursive
    Entrées : n = nombre de palets
            x = n° du premier plot
            y = n° du deuxième plot
            z = n° du troisième plot
            deplacement = nombre de déplacement
    Sortie : Pas de sortie
    """

    if n == 1:
        deplacement += 1
        print("Deplacer le disque du plot",x,"vers le plot",y)
        
    
    else:
        deplacement += 1
        hanoi(n-1,x,z,y, deplacement)
        deplacement += 1
        hanoi(1,x,y,z, deplacement)
        deplacement += 1
        hanoi(n-1,z,y,x, deplacement)