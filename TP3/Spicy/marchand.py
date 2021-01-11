# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Création de la classe marchand qui calcul le prix et les améliorations que le joueur peut acheter avec son argent gagné
    Date de réalisation : 04/01/2021
    Par Elliot GARCIA (Gr C)
"""

from tkinter import Frame, LabelFrame, Label, Button, StringVar, IntVar, PhotoImage, Canvas


class marchand:
    """
    But : Créer une classe marchand servant à contenir toutes les informations
        propre au marchand et à mettre en place l'interface graphique de la boutique
        ainsi que les fonctionnalité d'achat de celle-ci.
    """
    
    """Initialisation de la classe
    ------------------------------------------------------------------------"""
    def __init__(self, jeu):
        """
        But : Initialisation des élément de la classe marchand
        Entrée : La classe jeu (jeu)
        Sortie :
        """
        
        self.jeu = jeu
        self.app_jeu = jeu.app_jeu
        self.canvas = jeu.canvas
        
        
        
        """Initialisation des variables de la boutique
        --------------------------------------------------------------------"""
        
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
        
        """----------------------------------------------------------------"""
        
        
        
        """Création de la frame du marchand avec les achats
        -------------------------------------------------------------------"""
        self.frame_marchand = Frame(self.app_jeu, bg = "#B17750", width=540, height=540)
        self.frame_marchand.propagate(0)
        
        Label(self.frame_marchand, bg = "#B17750", text = "Magasin d'amélioration", font=50, pady=20).pack()
        
        #Labels décrivants les achats possibles
        Label(self.frame_marchand, bg = "#B17750", text = "Temps entre chaque tire : ").place(x=10, y=100)
        Label(self.frame_marchand, bg = "#B17750", text = "Amélioration de la vitesse du vaisseau : ").place(x=10, y=150)
        Label(self.frame_marchand, bg = "#B17750", text = "Amélioration de l'argent gagné par ennemi tué : ").place(x=10, y=200)
        Label(self.frame_marchand, bg = "#B17750", text = "Amélioration de l'argent gagné par ennemi bonus tué : ").place(x=10, y=250)
        
        #Bouton d'achat d'amélioration
        Button(self.frame_marchand, bg = "#B17750", textvariable = self.txt_up_cooldown, command = self.amelioration_cooldown).place(x=350, y=100)
        Button(self.frame_marchand, bg = "#B17750", textvariable = self.txt_up_rapidite, command = self.amelioration_rapidite).place(x=350, y=150)
        Button(self.frame_marchand, bg = "#B17750", textvariable = self.txt_up_multiplicateur_ennemis, command = self.amelioration_multiplicateur_ennemis).place(x=350, y=200)
        Button(self.frame_marchand, bg = "#B17750", textvariable = self.txt_up_multiplicateur_bonus, command = self.amelioration_multiplicateur_bonus).place(x=350, y=250)
        
        #Labels récapitulatifs des améliorations du vaisseau
        Label(self.frame_marchand, bg = "#B17750", text = "Revue du vaisseau", font=30).place(x=100, y=320)
        Label(self.frame_marchand, bg = "#B17750", text = "Niveau des canons : ").place(x=60, y=360)
        Label(self.frame_marchand, bg = "#B17750", text = "Niveau des propulseurs : ").place(x=60, y=385)
        Label(self.frame_marchand, bg = "#B17750", text = "Niveau de cupidité pour les ennemis : ").place(x=60, y=410)
        Label(self.frame_marchand, bg = "#B17750", text = "Niveau de cupidité pour les bonus: ").place(x=60, y=435)
        
        Label(self.frame_marchand, bg = "#B17750", textvariable = self.up_cooldown).place(x=300, y=360)
        Label(self.frame_marchand, bg = "#B17750", textvariable = self.up_rapidite).place(x=300, y=385)
        Label(self.frame_marchand, bg = "#B17750", textvariable = self.up_multiplicateur_ennemis).place(x=300, y=410)
        Label(self.frame_marchand, bg = "#B17750", textvariable = self.up_multiplicateur_bonus).place(x=300, y=435)
        
        #Bouton de validation et de retour au jeu
        Button(self.frame_marchand, fg="white", bg = "black", text = "Continuer la partie", command = jeu.lancer_niveau).place(x=400, y=500)
        
        """----------------------------------------------------------------"""
    """---------------------------------------------------------------------"""
    
    
    
    """Fonctions mettants en place le système d'achat d'amélioration
    ------------------------------------------------------------------------"""
    def amelioration_cooldown(self):
        """
        But : Actualiser le prix de l'amélioration "cooldown" ainsi que l'argent
            restant au joueur après achat.
            Puis actualisation de la valeur du "cooldown" dans la classe jeu
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.jeu.argent >= self.prix_up_cooldown:
            
            self.jeu.argent -= self.prix_up_cooldown
            self.jeu.argent = round(self.jeu.argent,2)
            self.jeu.txt_argent.set(str(self.jeu.argent) + " $€")
            
            self.prix_up_cooldown += self.prix_up_cooldown*0.4
            self.prix_up_cooldown = round(self.prix_up_cooldown, 2)
            self.txt_up_cooldown.set("Améliorer pour " + str(self.prix_up_cooldown) + " $€")
            
            self.jeu.cooldown -= 0.1
            self.up_cooldown.set(self.up_cooldown.get()+1)
    
    def amelioration_rapidite(self):
        """
        But : Actualiser le prix de l'amélioration "rapidité" ainsi que l'argent
            restant au joueur après achat.
            Puis actualisation de la valeur du "rapidité" dans la classe jeu
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.jeu.argent >= self.prix_up_rapidite:
            
            self.jeu.argent -= self.prix_up_rapidite
            self.jeu.argent = round(self.jeu.argent,2)
            self.jeu.txt_argent.set(str(self.jeu.argent) + " $€")
            
            self.prix_up_rapidite += self.prix_up_rapidite*0.4
            self.prix_up_rapidite = round(self.prix_up_rapidite, 2)
            self.txt_up_rapidite.set("Améliorer pour " + str(self.prix_up_rapidite) + " $€")
            
            self.jeu.rapidite += 1
            self.up_rapidite.set(self.up_rapidite.get()+1)
    
    def amelioration_multiplicateur_ennemis(self):
        """
        But : Actualiser le prix de l'amélioration "multiplicateur ennemis"
            ainsi que l'argent restant au joueur après achat.
            Puis actualisation de la valeur du "multiplicateur ennemis" dans
            la classe jeu.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.jeu.argent >= self.prix_up_multiplicateur_ennemis:
            
            self.jeu.argent -= self.prix_up_multiplicateur_ennemis
            self.jeu.argent = round(self.jeu.argent,2)
            self.jeu.txt_argent.set(str(self.jeu.argent) + " $€")
            
            self.prix_up_multiplicateur_ennemis += self.prix_up_multiplicateur_ennemis*0.4
            self.prix_up_multiplicateur_ennemis = round(self.prix_up_multiplicateur_ennemis, 2)
            self.txt_up_multiplicateur_ennemis.set("Améliorer pour " + str(self.prix_up_multiplicateur_ennemis) + " $€")
            
            self.jeu.multiplicateur_ennemis *= 1.05 #Amélioration de 5% du multiplicateur du joueur
            self.up_multiplicateur_ennemis.set(self.up_multiplicateur_ennemis.get() + 1)
    
    def amelioration_multiplicateur_bonus(self):
        """
        But : Actualiser le prix de l'amélioration "multiplicateur ennemis"
            ainsi que l'argent restant au joueur après achat.
            Puis actualisation de la valeur du "multiplicateur ennemis" dans
            la classe jeu.
        Entrée : toutes les informations de la classe (self)
        Sortie :
        """
        
        if self.jeu.argent >= self.prix_up_multiplicateur_bonus:
            
            self.jeu.argent -= self.prix_up_multiplicateur_bonus
            self.jeu.argent = round(self.jeu.argent,2)
            self.jeu.txt_argent.set(str(self.jeu.argent) + " $€")
            
            self.prix_up_multiplicateur_bonus += self.prix_up_multiplicateur_bonus*0.4
            self.prix_up_multiplicateur_bonus = round(self.prix_up_multiplicateur_bonus, 2)
            self.txt_up_multiplicateur_bonus.set("Améliorer pour " + str(self.prix_up_multiplicateur_bonus) + " $€")
            
            self.jeu.multiplicateur_bonus *= 1.03 #Amélioration de 3% du multiplicateur du joueur
            self.up_multiplicateur_bonus.set(self.up_multiplicateur_bonus.get() + 1)
    
    """---------------------------------------------------------------------"""