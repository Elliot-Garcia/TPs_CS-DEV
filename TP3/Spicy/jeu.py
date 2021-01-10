# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe jeu qui initialise la fenêtre de jeu et gère toutes les classes du jeu
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import IntVar, StringVar, Button, Label, Toplevel
import random as rd
import time as tps

import joueur as j
import projectile as p
import bonus as b
import marchand as m

import fonctions as fct


class jeu:

    
    def __init__(self, app_jeu, canvas):
        self.app_jeu = app_jeu
        self.canvas = canvas
        
        self.groupe_gentils = []
        self.groupe_mechants = []
        self.groupe_ennemis = []
        
        self.bonus = False
        self.bonus_init = False
        self.tire_ennemi_init = False
        
        self.tps_dernier_tire = 0 #Initialisation de son cooldown
        
        self.niveau = 1
        
        """ Caractéristiques du joueur """
        self.score = IntVar()
        self.score.set(0)
        self.txt_argent = StringVar()
        self.argent = 0
        self.argent_tot = self.argent
        self.txt_argent.set(str(self.argent) + " $€")
        
        self.cooldown = 1
        self.rapidite = 5
        self.multiplicateur_ennemis = 1
        self.multiplicateur_bonus = 1
        
        self.vie = IntVar()
        self.vie.set(3)
        
        """ -------------------------------- """
        
        self.M = m.marchand(self)
        
        #Initialisation des états dans le jeu
        self.jouer = False
        self.victoire = False
        
    def lancer_niveau(self):
        
        self.jouer = True #Le joueur joue
        self.victoire = False #Le joueur n'a pas encore gagné ce niveau
        self.bonus_init = False #Initialisation de l'ennemi bonus pas encore faites
        self.bonus = False
        self.tire_ennemi_init = False
        
        self.P = j.joueur(self) #Création de l'avatar du joueur
        
        self.M.frame_marchand.grid_forget() #Le joueur n'a plus accès au magasin
        
        fct.generation_niveau(fct.lecture_niveau(self.niveau), self)
        
        self.groupe_mechants += self.groupe_ennemis
        
        for ennemi in self.groupe_ennemis:
            ennemi.deplacement_horizontal()
            
        self.tire_ennemis()
        self.nouveau_bonus()
            
    def controle_joueur(self, touche):
        
        if self.jouer == True and self.P.vivant: #Le joueur a le contrôle de son avatar que lorsqu'il joue ou est vivant
            
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

    def nouveau_bonus(self):
        
        if self.bonus == False and self.jouer: #Pour n'avoir qu'un seul bonus à la fois et pas pendant qu'on est au magasin
            
            if self.bonus_init == False:
                tps_bonus = rd.randrange(30,60)*1000 #Ennemi bonus apparaittra aléatoirement entre 10 et 30 sec
                self.bonus_init = True
                self.app_jeu.after(tps_bonus,self.nouveau_bonus)#Ici pour qu'il n'y est q'un ennemi abattu par niveau car bonus_init remit à False uniquement si Bonus disparait naturellement
            
            else: 
                self.bonus = True #Si il n'y en avait pas avant, maintenant il y a un ennemi bonus
                ennemi_bonus = b.bonus(-40, 60, self)
                self.groupe_mechants.append(ennemi_bonus)
                ennemi_bonus.deplacement_et_fin()
                

    def tire_ennemis(self):
        
        nb_ennemis = len(self.groupe_ennemis)
        nouveau_tire = rd.randrange(1000,5000) #Tire toutes les 1 à 5 secondes
        
        if nb_ennemis > 0:
            if self.tire_ennemi_init == True:
                ennemi = rd.randrange(0,nb_ennemis)
                self.groupe_ennemis[ennemi].tirer()
                self.app_jeu.after(nouveau_tire,self.tire_ennemis)
            
            else:
                self.tire_ennemi_init = True
                self.app_jeu.after(nouveau_tire,self.tire_ennemis)


    def tuer(self, projectile, en_collision):
        
        camp_projectile = projectile.camp
        canvas_id = en_collision[0]
        
        if camp_projectile == "gentil":
            
            for mechant in self.groupe_mechants:
                if mechant.canvas_propre == canvas_id:
                    
                    self.groupe_mechants.remove(mechant)
                    
                    if mechant.status == "ennemi":
                        self.groupe_ennemis.remove(mechant)
                        mechant.mort()
                        
                    elif mechant.status == "bonus":
                        mechant.mort()
                        
                        
                    if len(self.groupe_ennemis) == 0:
                        self.jouer = False #Le joueur perd le contrôle de son avatar
                        self.victoire = True
                        self.affichage_fin()
                    
                    
                    mechant.vivant = False
                    projectile.vivant = False
                    
                    self.score.set(self.score.get() + mechant.score)
                    self.argent = round(self.argent + (mechant.argent * self.P.multiplicateur_ennemis), 2)
                    self.argent_tot += round(mechant.argent * self.P.multiplicateur_ennemis, 2)
                    self.txt_argent.set(str(self.argent) + " $€")
                    
                    break
                
            for gentil in self.groupe_gentils:
                if gentil.canvas_propre == canvas_id:
                    projectile.vivant = False
                        
        else:
            
            if canvas_id == self.P.canvas_propre:
                
                self.groupe_mechants.remove(projectile)
                projectile.vivant = False
                self.joueur_touche()
                
            
            else:
                for gentil in self.groupe_gentils:
                    if gentil.canvas_propre == canvas_id:
                        
                        self.groupe_gentils.remove(gentil)
                        self.groupe_mechants.remove(projectile)
                        
                        gentil.vivant = False
                        projectile.vivant = False
                        
                        break
    
    
    def joueur_touche(self):
        
        if self.vie.get() == 0:
            self.vie.set(3)
            self.affichage_fin()
            
        else:
            self.vie.set(self.vie.get() - 1)
            self.P.vivant = False
            self.P.degats()
    
    
    def resurection_joueur(self):
        
        self.P = j.joueur(self)
    
    def affichage_fin(self):
        
        for mechant in self.groupe_mechants: mechant.vivant = False
        for gentil in self.groupe_gentils: gentil.vivant = False
        self.groupe_mechants = []
        self.groupe_ennemis = []
        self.groupe_gentils = []
        self.M.frame_marchand.grid(row=1, column=1, rowspan=10)
        
        if self.victoire:
            fin = Toplevel(bg = "black")
            Label(fin, fg="white", bg = "green", text="Bravo vous avez gagné !", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
            Label(fin, fg="white", bg = "black", text="Niveau " + str(self.niveau) + " réussi !", font = 50, padx = 100, pady = 20).grid(row=2, column=1, columnspan=3)
            
            self.niveau += 1
        else:
            fin = Toplevel(bg = "black")
            Label(fin, fg="white", bg = "red", text="Arrrggg ! Continuez ainsi, nous y sommes presque !", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
            Label(fin, fg="white", bg = "black", text="Niveau " + str(self.niveau) + " échoué", font = 50, padx = 100, pady = 20).grid(row=2, column=1, columnspan=3)
        
        fin.attributes("-topmost", True)
        
        fin.grab_set()
        fin.transient(self.app_jeu)
        
        Button(fin, fg="white", bg = "black", text="D'accord !", padx = 10, pady = 10, command = fin.destroy).grid(row = 4, column = 2)
        self.app_jeu.wait_window(fin)