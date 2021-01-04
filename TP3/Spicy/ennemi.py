# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe ennemi qui initialise les ennemis et les déplacent dans l'espace
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

import projectile as p


class ennemi:
    
    def __init__(self, X, Y, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = X
        self.Y = Y
        self.camp = 'mechant'
        self.niveau = 1
        self.direction_tire = "S"
        
        self.dx = 2
        self.score = 5
        
        self.ennemi = jeu.canvas.create_oval(self.X-10,self.Y-10,self.X+10,self.Y+10,fill="red")
    
    def deplacement_vertical(self):
        self.canvas.move(self.ennemi,0,5)
        
    def deplacement_horizontal(self):
        
        if len(self.jeu.groupe_ennemis) > 0:
            
            dy = 0
            self.X += self.dx
            
            #Vérification position du groupe ennemi
            groupe_x = []
            for e in self.jeu.groupe_ennemis:
                groupe_x.append(e.X)
            min_x_groupe = min(groupe_x)
            max_x_groupe = max(groupe_x)
            
            if min_x_groupe < 20 and self.dx != int(2):
                self.deplacement_vertical()
                self.dx = int(2)
            
            elif max_x_groupe > 560 and self.dx != int(-2):
                self.deplacement_vertical()
                self.dx = int(-2)
                
            self.canvas.move(self.ennemi,self.dx,dy)
            self.app_jeu.after(50,self.deplacement_horizontal)
    
    def tirer(self):
        if self in self.jeu.groupe_ennemis:
            tire = p.projectile(self.jeu, self)
            tire.deplacement_projectile()
    
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.ennemi)