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
    """
    But : Créer une classe ennemi servant définir l'ennemi, à le créer
        et à le déplacer.
    """
    
    """Initialisation de la classe
    ------------------------------------------------------------------------"""
    def __init__(self, X, Y, jeu):
        """
        But : Initialisation des élément de la classe ennemi
        Entrée : Les coordonnées d'apparition de l'ennemi (X et Y),
            La classe jeu (jeu)
        Sortie :
        """
        
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = X
        self.Y = Y
        self.camp = 'mechant'
        self.status = "ennemi"
        self.direction_tire = "S" #Définition de l'orientation du tire (vers le sud)
        
        self.dx = 2
        self.dy = 15
        self.score = 1
        self.argent = 1
        
        self.img_boom = PhotoImage(file = "data/image/boom.gif")
        self.img_mechant = PhotoImage(file = "data/image/mechant.gif")
        self.canvas_propre = self.canvas.create_image(self.X, self.Y, image = self.img_mechant)
        
        self.vivant = True 
        
    """---------------------------------------------------------------------"""
    
    
    
    """Fonctions de déplacement, de tire et de mort de l'ennemis bonus
    ------------------------------------------------------------------------"""
    def deplacement_vertical(self):
        """
        But : Faire se déplacer l'ennemi verticalement
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        self.Y += self.dy #Actualisation de la position Y (verticale)
        self.canvas.move(self.canvas_propre,0,self.dy) #Déplacement vertical
        
        if self.Y >= 490: #Vérifiation de si les ennemis n'ont pas atteint le joueur
            self.jeu.affichage_fin() #Si oui, le joueur à perdu
        
    def deplacement_horizontal(self):
        """
        But : Faire se déplacer l'ennemi horizontalement
            et lancer la fonction de déplacement verticale lorsque le groupe d'ennemis est arriver au bord de la zone de jeu.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        nb_ennemis = len(self.jeu.groupe_ennemis) #Nombre d'ennemi restant
        if nb_ennemis > 0 and self.vivant:
            
            self.X += self.dx #Actualisation de la position X (horizontale)
            
            #Vérification position du groupe ennemi
            groupe_x = []
            for e in self.jeu.groupe_ennemis: #Récupération de toutes les coordonnées x des ennemis vivants
                groupe_x.append(e.X)
            
            #Détermination du min et du max des x des ennemis vivants
            min_x_groupe = min(groupe_x)
            max_x_groupe = max(groupe_x)
            
            if min_x_groupe < 40 and self.dx != int(2): #Détermination de sa direction de déplacement vers la droite si le groupe d'ennemis est à gauche de l'écran
                self.deplacement_vertical()
                self.dx = int(2)
            
            elif max_x_groupe > 540 and self.dx != int(-2): #Détermination de sa direction de déplacement vers la gauche si le groupe d'ennemis est à droite de l'écran
                self.deplacement_vertical()
                self.dx = int(-2)
                
            self.canvas.move(self.canvas_propre,self.dx,0) #Déplacement du canvas de l'ennemi
            self.app_jeu.after(50, self.deplacement_horizontal) #Réitération toutes les 50 ms.
    
    def tirer(self):
        """
        But : Si l'ennemi est vivant, lui faire tirer un projectile
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant: #L'ennemi ne tire que si il est vivant
            
            tire = p.projectile(self.jeu, self) #Création d'un projectile aux coordonnées de l'ennemi
            tire.deplacement_projectile() #Déplacement du projectile créé
            
    def mort(self):
        """
        But : Quand il est touché, remplacer l'image de l'ennemi par une explosion
            pendant une demi-seconde.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant == True: #Vrai au début
            self.canvas.itemconfigure(self.canvas_propre, image = self.img_boom) #Changement de l'illustration
            self.app_jeu.after(500,self.mort) #Après 0.5 s, l'ennemi et mort.
            
            
    def __del__(self):
        """
        But : Supprimer l'item ennemi à sa mort
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        self.canvas.delete(self.app_jeu,self.canvas_propre)
        
    """---------------------------------------------------------------------"""