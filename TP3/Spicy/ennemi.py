# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe ennemi qui initialise les ennemis et les déplacent dans l'espace
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

import projectile as p


class ennemi:
    
    def __init__(self, X, Y, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = X
        self.Y = Y
        self.camp = 'mechant'
        self.status = "ennemi"
        
        self.direction_tire = "S"
        
        
        self.dx = 2
        self.dy = 15
        self.score = 1
        self.argent = 1
        
        self.img_boom = PhotoImage(file = "data/image/boom.gif")
        self.img_mechant = PhotoImage(file = "data/image/mechant.gif")
        self.canvas_propre = self.canvas.create_image(self.X, self.Y, image = self.img_mechant)
        
        self.vivant = True
    
    def deplacement_vertical(self):
        self.Y += self.dy
        self.canvas.move(self.canvas_propre,0,self.dy)
        
        if self.Y >= 490:
            self.jeu.affichage_fin()
        
    def deplacement_horizontal(self):
        
        nb_ennemis = len(self.jeu.groupe_ennemis)
        if nb_ennemis > 0 and self.vivant:
            
            self.X += self.dx
            
            #Vérification position du groupe ennemi
            groupe_x = []
            for e in self.jeu.groupe_ennemis:
                groupe_x.append(e.X)
                
            min_x_groupe = min(groupe_x)
            max_x_groupe = max(groupe_x)
            
            if min_x_groupe < 40 and self.dx != int(2):
                self.deplacement_vertical()
                self.dx = int(2)
            
            elif max_x_groupe > 540 and self.dx != int(-2):
                self.deplacement_vertical()
                self.dx = int(-2)
                
            self.canvas.move(self.canvas_propre,self.dx,0)
            self.app_jeu.after(50, self.deplacement_horizontal)
    
    def tirer(self):
        if self.vivant:
            
            tire = p.projectile(self.jeu, self)
            tire.deplacement_projectile()
            
    def mort(self):
        
        if self.vivant == True: #Vrai au début
            self.canvas.itemconfigure(self.canvas_propre, image = self.img_boom)
            self.app_jeu.after(500,self.mort)
            
            
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.canvas_propre)