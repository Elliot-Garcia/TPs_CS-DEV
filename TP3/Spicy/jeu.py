# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe jeu qui initialise la fenêtre de jeu et gère toutes les classes du jeu
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import PhotoImage, IntVar
import random as rd
import time as tps

import joueur as j
import projectile as p

import fonctions as fct


class jeu:

    
    def __init__(self, app_jeu, canvas):
        self.app_jeu = app_jeu
        self.canvas = canvas
        self.groupe_ennemis = []
        # self.groupe_projectile_mechant = []
        # self.groupe_projectile_gentil = []
        
        self.P = j.joueur(self) #Création de l'avatar du joueur
        self.tps_dernier_tire = 0 #Initialisation de son cooldown
        
        self.niveau = 0
        self.score = IntVar()
        
        self.score.set(0)
        

    def lancer_partie(self):
        if len(self.groupe_ennemis) == 0:
            self.niveau += 1
            
            fct.generation_niveau(fct.lecture_niveau(self.niveau), self)
            
            for ennemi in self.groupe_ennemis:
                ennemi.deplacement_horizontal()
            self.tire_ennemis()
            
    def controle_joueur(self, touche):
        
        tps_entre_tires = tps.time() - self.tps_dernier_tire
        
        if touche == "Left":
            self.P.gauche()
        
        if touche == "Right":
            self.P.droite()
            
        if touche == "space":
            if tps_entre_tires >= self.P.cooldown:
                self.tps_dernier_tire = tps.time()
                tire = p.projectile(self, self.P)
                tire.deplacement_projectile()


    def tire_ennemis(self):
        nb_ennemis = len(self.groupe_ennemis)
        if nb_ennemis > 0:
            nouveau_tire = rd.randrange(1000,5000) #Tire toutes les 1 à 5 secondes
            ennemi = rd.randrange(0,nb_ennemis)
            self.groupe_ennemis[ennemi].tirer()
            self.app_jeu.after(nouveau_tire,self.tire_ennemis)


    def tuer(self, projectile, camp_projectile, en_collision):
        if camp_projectile == "gentil":
            for canvas_id in en_collision:
                for ennemi in self.groupe_ennemis:
                    if ennemi.ennemi == canvas_id:
                        self.canvas.delete(self.app_jeu, ennemi.ennemi)
                        self.canvas.delete(self.app_jeu, projectile.tire)
                        self.groupe_ennemis.remove(ennemi)
                        self.score.set(self.score.get() + ennemi.score)
                # for proj in self.groupe_projectile_mechant:
                #     if proj.tire == canvas_id:
                #         p.delete(proj)
                        # proj.detruit = 1
                        # projectile.detruit = 1

        # elif camp_projectile == "mechant":
        #     for canvas_id in en_collision:
        #         for ennemi in self.groupe_ennemis:
        #             if ennemi.ennemi == canvas_id:
        #                 self.canvas.delete(self.app_jeu, ennemi.ennemi)
        #                 self.canvas.delete(self.app_jeu, projectile.tire)
        
    #     self.victoire()
    
    # def victoire(self):
        
    #     if len(self.groupe_ennemis) <= 0:
    #         self.niveau += 1
    #         jeu(self.app_jeu, self.canvas)