# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe joueur qui initialise l'avatar et le déplace dans l'espace
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""


class joueur:
    
    def __init__(self, jeu):
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = 290
        self.Y = 520
        self.camp = 'gentil'
        self.direction_tire = "N"
        
        self.cooldown = 0.5
        
        self.spicy = self.canvas.create_rectangle(self.X-10,self.Y-10,self.X+10,self.Y+10,fill="yellow")
      
    def gauche(self):
        if self.X >= 15:
            self.canvas.move(self.spicy,int(-10),0)
            self.X -= 10
    
    def droite(self):
        if self.X <= 565:
            self.canvas.move(self.spicy,int(10),0)
            self.X += 10