# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe projectile qui gère la création et le déplacement des tires
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""


class projectile:
    
    def __init__(self, jeu, tireur):
        self.jeu = jeu
        
        self.canvas = jeu.canvas
        self.app_jeu = jeu.app_jeu
        
        #self.detruit = 0
        self.X = tireur.X
        self.Y = tireur.Y
        
        self.camp = tireur.camp
        
        # if self.camp == "gentil":
        #     self.jeu.groupe_projectile_gentil.append(self)
        # if self.camp == "mechant":
        #     self.jeu.groupe_projectile_mechant.append(self)
        
        self.direction = tireur.direction_tire
               
        if self.direction == 'N':
            self.tire = self.canvas.create_rectangle(self.X-2,self.Y-5,self.X+2,self.Y-25,fill="yellow")
        elif self.direction == "S":
            self.tire = self.canvas.create_rectangle(self.X-2,self.Y+5,self.X+2,self.Y+25,fill="red")
    
    
    def deplacement_projectile(self):
        
        if self.direction == "N":
            dy = int(-5)
            dx = 0
        
        elif self.direction == "S":
            dy = int(5)
            dx = 0

        if self.Y > 10 and self.Y < 550:
            self.canvas.move(self.tire,dx,dy)
            self.Y += dy
            self.Y += dx            
            self.app_jeu.after(20,self.deplacement_projectile)
    
        self.collision(self.jeu)
    
    
    def collision(self, jeu):
        en_collision = self.canvas.find_overlapping(self.X-2,self.Y-5,self.X+2,self.Y-25)
        if len(en_collision)>1:
            jeu.tuer(self, self.camp, en_collision[0:len(en_collision)-1])
    
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.tire)