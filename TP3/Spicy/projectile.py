# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe projectile qui gère la création et le déplacement des tires
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

class projectile:
    
    def __init__(self, jeu, tireur):
        self.jeu = jeu
        
        self.canvas = jeu.canvas
        self.app_jeu = jeu.app_jeu
        
        #self.detruit = 0
        self.X = tireur.X
        self.Y = tireur.Y
        
        self.score = 0
        self.argent = 0
        self.status = "projectile"
        
        self.camp = tireur.camp
        self.vivant = True
        
        self.direction = tireur.direction_tire
        
        if self.direction == 'N':
            self.img_projectile = PhotoImage(file = "data/image/projectile_heros.gif")
            self.canvas_propre = self.canvas.create_image(self.X, self.Y-5, image = self.img_projectile)
            
        elif self.direction == "S":
            self.img_projectile = PhotoImage(file = "data/image/projectile_mechant.gif")
            self.canvas_propre = self.canvas.create_image(self.X, self.Y-5, image = self.img_projectile)
    
    
        if self.camp == "mechant":
            jeu.groupe_mechants.append(self)
                
    
    def deplacement_projectile(self):
        
        if self.vivant:
        
            if self.direction == "N":
                dy = int(-5)
                dx = 0
            
            elif self.direction == "S":
                dy = int(5)
                dx = 0
    
            if self.Y > 10 and self.Y < 550:
                self.canvas.move(self.canvas_propre,dx,dy)
                self.Y += dy
                self.Y += dx            
                self.app_jeu.after(20,self.deplacement_projectile)
            
            else:
                self.vivant = False
                
                if self.camp == "mechant":
                    self.jeu.groupe_mechants.remove(self)
                
        
            self.collision()
    
    
    def collision(self):
        
        if self.vivant:
            
            if self.direction == 'N':
                en_collision = self.canvas.find_overlapping(self.X-3,self.Y-5,self.X+3,self.Y-15)
            else: en_collision = self.canvas.find_overlapping(self.X-3,self.Y+5,self.X+3,self.Y+15)
            
            if len(en_collision) > 2:
                self.jeu.tuer(self, en_collision[1:len(en_collision)-1])
                # 1er = canvas de fond, dernier = canvas_propre
    
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.canvas_propre)