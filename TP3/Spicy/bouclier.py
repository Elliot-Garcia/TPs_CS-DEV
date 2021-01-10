# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe bouclier qui va initialiser et mettre en place les boucliers pour le joueur
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage

class bouclier:
    
    def __init__(self, X, Y, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.X = X
        self.Y = Y
        self.camp = 'gentil'
        self.status = "bouclier"
        self.img_boom = PhotoImage(file = "data/image/boom.gif")
        
        self.canvas_propre = jeu.canvas.create_rectangle(self.X-10,self.Y-10,self.X+10,self.Y+10,fill="gray")
        self.vivant = True
        
    def __del__(self):
        self.canvas.delete(self.app_jeu,self.canvas_propre)