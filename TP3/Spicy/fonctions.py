# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:32:11 2020

@author: ellig
"""

import jeu as jeu
import ennemi as e

def lecture_niveau(num_niveau):
    f = open('data/niveaux/niveau'+str(num_niveau)+'.txt')
    L = []
    l = f.readline()
    while l != '':
        L.append(l.strip())
        l = f.readline()
    f.close()
    return L

def generation_niveau(liste_niveau, jeu):
    largeur = len(liste_niveau[0])
    hauteur = len(liste_niveau)
    
    place_largeur = 580
    place_hauteur = 200
    
    repartition_largeur = place_largeur / (largeur+1)
    repartition_hauteur = place_hauteur / (hauteur+1)
    
    for i in range(hauteur):
        for j in range(largeur):
            if liste_niveau[i][j] != "_":
                jeu.groupe_ennemis.append(e.ennemi(repartition_largeur*(j+1), repartition_hauteur*(i+1), jeu))