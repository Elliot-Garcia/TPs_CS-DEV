# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe joueur qui initialise l'avatar et le déplace dans l'espace
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

class joueur:
    
    def __init__(self, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = 290
        self.Y = 520
        self.camp = 'gentil'
        self.direction_tire = "N"
        
        self.vivant = True
        
        #Caractéristiques du vaisseau du joueur au début
        self.cooldown = jeu.cooldown
        self.rapidite = jeu.rapidite
        self.multiplicateur_ennemis = jeu.multiplicateur_ennemis
        self.multiplicateur_bonus = jeu.multiplicateur_bonus
        
        #self.canvas_propre = self.canvas.create_rectangle(self.X-10, self.Y-10, self.X+10, self.Y+10, fill="yellow")
        
        self.img_joueur = PhotoImage(file = "data/image/heros.gif")
        self.img_joueur_degats = PhotoImage(file = "data/image/heros_degats.gif")
        self.img_choisie = 0 #Sert dans la fonction dégats à changer d'image
        
        self.canvas_propre = self.canvas.create_image(self.X, self.Y, image = self.img_joueur)
        
        
      
    def gauche(self):
        if self.X - self.rapidite >= 20:
            self.canvas.move(self.canvas_propre,int(-self.rapidite),0)
            self.X -= self.rapidite

    def droite(self):
        if self.X + self.rapidite <= 560:
            self.canvas.move(self.canvas_propre,int(self.rapidite),0)
            self.X += self.rapidite
    
    def degats(self):
        
        if self.img_choisie <= 5:
            
            images = [self.img_joueur_degats, self.img_joueur]
            self.canvas.itemconfigure(self.canvas_propre, image = images[self.img_choisie%2])
            self.img_choisie += 1
            self.app_jeu.after(500,self.degats)
            
        else:
            self.jeu.resurection_joueur()
    
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.canvas_propre)