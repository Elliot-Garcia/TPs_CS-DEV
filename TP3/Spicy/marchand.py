# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe marchand qui calcul le prix et les améliorations que le joueur peut acheter avec son argent gagné
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""


class marchand:
    
    def __init__(self, jeu):
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.up_cooldown = 0
        self.prix_up_cooldown = 2
        
        self.up_rapidite = 0
        self.prix_up_rapidite = 2
        
        self.up_multiplicateur_ennemis = 0
        self.prix_up_multiplicateur_ennemis = 2
        
        self.up_multiplicateur_bonus = 0
        self.prix_up_multiplicateur_bonus = 2
    
    def amelioration_cooldown(self, joueur, argent):
        #self.prix_up_cooldown = self.prix_up_cooldown ** (self.up_cooldown+1)
        
        if argent >= self.prix_up_cooldown:
            joueur.cooldown -= 0.1
            self.up_cooldown += 1