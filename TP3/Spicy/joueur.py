# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe joueur qui initialise l'avatar et le déplace dans l'espace
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

class joueur:
    """
    But : Créer une classe joueur servant définir l'avatar du joueur, à le créer,
        à le déplacer et à l'animer lorsqu'il prend des dégâts.
    """
    
    """Initialisation de la classe
    ------------------------------------------------------------------------"""
    def __init__(self, jeu):
        """
        But : Initialisation des élément de la classe joueur
        Entrée : Les informations de la classe jeu (jeu)
        Sortie :
        """
        
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
        
        #Chargement image de dégats
        self.img_joueur_degats = PhotoImage(file = "data/image/heros_degats.gif")
        
        #Définition du skin du joueur
        self.img_joueur = self.jeu.skin
        self.img_choisie = 0 #Sert dans la fonction dégats à changer d'image
        
        self.canvas_propre = self.canvas.create_image(self.X, self.Y, image = self.img_joueur)
    
    """---------------------------------------------------------------------"""
    
  
        
    """Fonctions de contrôle, de prise de dégat et de mort du joueur
    ------------------------------------------------------------------------"""
    def gauche(self):
        """
        But : Faire se déplacer l'item du joueur vers la gauche
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.X - self.rapidite >= 20:
            self.canvas.move(self.canvas_propre,int(-self.rapidite),0)
            self.X -= self.rapidite

    def droite(self):
        """
        But : Faire se déplacer l'item du joueur vers la droite
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.X + self.rapidite <= 560:
            self.canvas.move(self.canvas_propre,int(self.rapidite),0)
            self.X += self.rapidite
    
    def degats(self):
        """
        But : Animer l'avatar du joueur lorsqu'il se prend des dégats
            (item du joueur clignote en rouge)
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.img_choisie <= 5: #Le joueur ne clignote que 3 fois
            
            images = [self.img_joueur_degats, self.img_joueur]
            self.canvas.itemconfigure(self.canvas_propre, image = images[self.img_choisie%2]) #Alternance entre l'image normale et l'image rouge de dégat
            self.img_choisie += 1
            self.app_jeu.after(500,self.degats)
            
        else:
            self.jeu.resurection_joueur()
    
    def __del__(self):
        """
        But : Supprimer l'item joueur à sa mort
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        self.canvas.delete(self.app_jeu,self.canvas_propre)
    
    """---------------------------------------------------------------------"""