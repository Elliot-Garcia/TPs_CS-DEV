# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe bonus qui initialise les ennemis bonus et les déplacent dans l'espace
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage


class bonus:
    
    def __init__(self, X, Y, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = X
        self.Y = Y
        self.camp = 'mechant'
        self.status = "bonus"
        self.nb_aller_retour = 4
        
        self.dx = 10
        self.score = 10
        self.argent = 15
        
        self.img_boom = PhotoImage(file = "data/image/boom.gif")
        self.img_mechant = PhotoImage(file = "data/image/bonus.gif")
        self.canvas_propre = self.canvas.create_image(self.X, self.Y, image = self.img_mechant)
        
        self.vivant = True
        
    def deplacement_et_fin(self):
        
        if self.vivant:
            
            self.X += self.dx
            
            if self.nb_aller_retour >= 0:
            
                if self.X < 80 and self.dx != int(10):
                    self.dx = int(10)
                    self.nb_aller_retour -= 1
                
                elif self.X > 500 and self.dx != int(-10):
                    self.dx = int(-10)
                    
                self.canvas.move(self.canvas_propre,self.dx,0)
                self.app_jeu.after(50, self.deplacement_et_fin)
            
            else:
                self.jeu.groupe_mechants.remove(self)
                self.jeu.bonus = False
                self.jeu.bonus_init = False
                self.jeu.nouveau_bonus()
            
            
    def mort(self):
        
        if self.vivant == True: #Vrai au début
            self.canvas.itemconfigure(self.canvas_propre, image = self.img_boom)
            self.app_jeu.after(500,self.mort)
            
            
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.canvas_propre)