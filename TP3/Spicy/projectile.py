# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe projectile qui gère la création et le déplacement des tires
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

class projectile:
    """
    But : Créer une classe projectile servant définir le projectile, à le créer,
        à le déplacer et à détecter ses collision avec les autres items.
    """
    
    """Initialisation de la classe
    ------------------------------------------------------------------------"""
    def __init__(self, jeu, tireur):
        """
        But : Initialisation des élément de la classe projectile
        Entrée : informations de la classe jeu (jeu),
            informations sur le tireur (tireur)
        Sortie :
        """
        
        self.jeu = jeu
        
        self.canvas = jeu.canvas
        self.app_jeu = jeu.app_jeu
        
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
        
    """---------------------------------------------------------------------"""
    
    
    
    """Fonctions de déplacement, de collision et de mort du projectile
    ------------------------------------------------------------------------"""
    def deplacement_projectile(self):
        """
        But : Déplacer le projectile verticalement vers le N ou le S.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant: #Déplacement du projectile ssi il est "vivant"
        
            if self.direction == "N": #Déplacement du projectile vers le Nord
                dy = int(-5)
                dx = 0
            
            elif self.direction == "S": #Déplacement du projectile vers le Sud
                dy = int(5)
                dx = 0
    
            if self.Y > 10 and self.Y < 550: #Si le projectile n'est pas au bout de l'écran de jeu
                self.canvas.move(self.canvas_propre,dx,dy)
                self.Y += dy
                self.Y += dx            
                self.app_jeu.after(20,self.deplacement_projectile)
            
            else:
                self.vivant = False #Déstruction/Suppression du projectile lorsqu'il est au bout de l'écran (en bas ou en haut)
                
                if self.camp == "mechant": #Si le projectile était tiré par un méchant, on le retire du groupe des méchants
                    self.jeu.groupe_mechants.remove(self)
                
        
            self.collision() #Vérification des collisions à chaque déplacement
    
    
    def collision(self):
        """
        But : Détecter les collisions entre le projectile et les autres items
            sous forme d'une liste.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.vivant: #Si il est vivant, on vérifie les collisions du projectile
            
            #Création des zones de collision, aussi appelé "hitbox"
            if self.direction == 'N': #Les "hitbox" ne sont pas les mêmes selon la direction du projectile
                en_collision = self.canvas.find_overlapping(self.X-3,self.Y-5,self.X+3,self.Y-15)
            else: en_collision = self.canvas.find_overlapping(self.X-3,self.Y+5,self.X+3,self.Y+15)
            
            #Prise en compte de la collision que si elle concerne d'autre item que le canvas de fond et le canvas_propre
            if len(en_collision) > 2:
                self.jeu.tuer(self, en_collision[1:len(en_collision)-1])
                # 1er = canvas de fond, dernier = canvas_propre
                #Ainsi on ne prend que les collisions avec d'autres items
    
    def __del__(self):
        """
        But : Supprimer l'item projectile à sa mort
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        self.canvas.delete(self.app_jeu,self.canvas_propre)
        
    """---------------------------------------------------------------------"""