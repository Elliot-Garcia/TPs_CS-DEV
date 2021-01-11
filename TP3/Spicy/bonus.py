# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe bonus qui initialise les ennemis bonus et les déplacent dans l'espace
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage


class bonus:
    """
    But : Créer une classe bonus servant définir l'ennemi "bonus", à le créer
        et à le déplacer.
    """
    
    """Initialisation de la classe
    ------------------------------------------------------------------------"""
    def __init__(self, X, Y, jeu):
        """
        But : Initialisation des élément de la classe bonus
        Entrée : Les coordonnées d'apparition de l'ennemi bonus (X et Y),
            La classe jeu (jeu)
        Sortie :
        """
        
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
     
    """---------------------------------------------------------------------"""
    
    
    
    """Fonctions de déplacement et de mort de l'ennemis bonus
    ------------------------------------------------------------------------"""
    def deplacement_et_fin(self):
        """
        But : Faire se déplacer le bonus horizontalement un nombre de fois limiter
            pour enfin le faire disparaitre.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant: #bonus ne se déplace que si il est vivants
            
            self.X += self.dx #Actualisation des coordonnées du bonus
            
            if self.nb_aller_retour >= 0: #Le bonus ne fait qu'un nombre d'aller-retour limité
            
                if self.X < 80 and self.dx != int(10): #Détermination de sa direction de déplacement vers la droite si bonus est à gauche de l'écran
                    self.dx = int(10)
                    self.nb_aller_retour -= 1
                
                elif self.X > 500 and self.dx != int(-10): #Détermination de sa direction de déplacement vers la gauche si bonus est à droite de l'écran
                    self.dx = int(-10)
                    
                self.canvas.move(self.canvas_propre,self.dx,0) #Déplacement du bonus après détermination de sa direction
                self.app_jeu.after(50, self.deplacement_et_fin) #Réitérer l'opération toutes les 50 ms.
            
            else: #Lorsque le bonus à fini de faire ses aller-retour
                self.jeu.groupe_mechants.remove(self) #Disparition du bonus
                self.jeu.bonus = False #Le bonus n'a pas était tué dans ce niveau (donc pourra réapparaitre)
                self.jeu.bonus_init = False #Besoin de réinitialiser le bonus
                self.jeu.nouveau_bonus() #On lance la création d'un nouveau bonus
            
            
    def mort(self):
        """
        But : Quand il est touché, remplacer l'image du bonus par une explosion
            pendant une demi-seconde.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant == True: #Vrai au début
            self.canvas.itemconfigure(self.canvas_propre, image = self.img_boom) #Changement de l'illustration
            self.app_jeu.after(500,self.mort) #Après 0.5 s, l'ennemi et mort.
            
            
    def __del__(self):
        """
        But : Supprimer l'item du bonus à sa mort
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        self.canvas.delete(self.app_jeu,self.canvas_propre)
    
    """---------------------------------------------------------------------"""