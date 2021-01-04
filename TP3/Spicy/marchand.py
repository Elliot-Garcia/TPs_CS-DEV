# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe marchand qui calcul le prix et les améliorations que le joueur peut acheter avec son argent gagné
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""

from tkinter import Frame, LabelFrame, Label, Button, StringVar, IntVar


class marchand:
    
    def __init__(self, jeu):
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        self.up_cooldown = IntVar()
        self.up_cooldown.set(0)
        self.prix_up_cooldown = 2
        self.txt_up_cooldown = StringVar()
        self.txt_up_cooldown.set("Améliorer pour " + str(self.prix_up_cooldown) + " $€")
        
        self.up_rapidite = IntVar()
        self.up_rapidite.set(0)
        self.prix_up_rapidite = 2
        self.txt_up_rapidite = StringVar()
        self.txt_up_rapidite.set("Améliorer pour " + str(self.prix_up_rapidite) + " $€")
        
        self.up_multiplicateur_ennemis = IntVar()
        self.up_multiplicateur_ennemis.set(0)
        self.prix_up_multiplicateur_ennemis = 2
        self.txt_up_multiplicateur_ennemis = StringVar()
        self.txt_up_multiplicateur_ennemis.set("Améliorer pour " + str(self.prix_up_multiplicateur_ennemis) + " $€")
        
        self.up_multiplicateur_bonus = IntVar()
        self.up_multiplicateur_bonus.set(0)
        self.prix_up_multiplicateur_bonus = 2
        self.txt_up_multiplicateur_bonus = StringVar()
        self.txt_up_multiplicateur_bonus.set("Améliorer pour " + str(self.prix_up_multiplicateur_bonus) + " $€")
        
        """Création de la frame du marchand avec les achats
        -------------------------------------------------------------------"""
        self.frame_marchand = Frame(self.app_jeu, width=540, height=540, bg="pink")
        self.frame_marchand.propagate(0)
        
        Label(self.frame_marchand, text = "Magasin d'amélioration", font=50, pady=20).pack()
        
        #Labels décrivants les achats possibles
        Label(self.frame_marchand, text = "Temps entre chaque tire : ").place(x=10, y=100)
        Label(self.frame_marchand, text = "Amélioration de la vitesse du vaisseau : ").place(x=10, y=150)
        Label(self.frame_marchand, text = "Amélioration de l'argent gagné par ennemi tué : ").place(x=10, y=200)
        Label(self.frame_marchand, text = "Amélioration de l'argent gagné par ennemi bonus tué : ").place(x=10, y=250)
        
        #Bouton d'achat d'amélioration
        Button(self.frame_marchand, textvariable = self.txt_up_cooldown, command = self.amelioration_cooldown).place(x=350, y=100)
        Button(self.frame_marchand, textvariable = self.txt_up_rapidite, command = self.amelioration_cooldown).place(x=350, y=150)
        Button(self.frame_marchand, textvariable = self.txt_up_multiplicateur_ennemis, command = self.amelioration_cooldown).place(x=350, y=200)
        Button(self.frame_marchand, textvariable = self.txt_up_multiplicateur_bonus, command = self.amelioration_cooldown).place(x=350, y=250)
        
        #Labels récapitulatifs des améliorations du vaisseau
        Label(self.frame_marchand, text = "Revue du vaisseau", font=30).place(x=100, y=320)
        Label(self.frame_marchand, text = "Niveau des canons : ").place(x=60, y=360)
        Label(self.frame_marchand, text = "Niveau des propulseurs : ").place(x=60, y=385)
        Label(self.frame_marchand, text = "Niveau de cupidité pour les ennemis : ").place(x=60, y=410)
        Label(self.frame_marchand, text = "Niveau de cupidité pour les bonus: ").place(x=60, y=435)
        
        Label(self.frame_marchand, textvariable = self.up_cooldown).place(x=300, y=360)
        Label(self.frame_marchand, textvariable = self.up_rapidite).place(x=300, y=385)
        Label(self.frame_marchand, textvariable = self.up_multiplicateur_ennemis).place(x=300, y=410)
        Label(self.frame_marchand, textvariable = self.up_multiplicateur_bonus).place(x=300, y=435)
        
        #Bouton de validation et de retour au jeu
        Button(self.frame_marchand, fg="white", bg = "black", text = "Continuer la partie", command = jeu.lancer_niveau).place(x=400, y=500)
        """----------------------------------------------------------------"""
    
    def amelioration_cooldown(self):
        
        if self.jeu.argent >= self.prix_up_cooldown:
            
            self.jeu.argent -= self.prix_up_cooldown
            self.jeu.argent = round(self.jeu.argent,2)
            self.jeu.txt_argent.set(str(self.jeu.argent) + " $€")
            
            self.prix_up_cooldown += round(self.prix_up_cooldown*0.4, 2)
            self.txt_up_cooldown.set("Améliorer pour " + str(self.prix_up_cooldown) + " $€")
            
            #jeu.P.cooldown -= 0.1
            self.up_cooldown.set(self.up_cooldown.get()+1)
            print(self.up_cooldown.get())