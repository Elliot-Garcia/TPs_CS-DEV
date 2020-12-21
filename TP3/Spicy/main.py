# -*- coding: utf-8 -*-
"""
Header:
    Lien GIT : https://github.com/Elliot-Garcia/TPs_CS-DEV
    Objectif : Concevoir un jeu "Spaceinvader"
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""


from tkinter import Tk, Label, Button, Canvas, IntVar


import jeu as jeu



"""Fonction de contrôle de l'avatar en fonction des touches saisies par le joueur
---------------------------------------------------------------------------"""       
def clavier(event):
    """
    But : Récupérer les touches du clavier entré par le joueur pour les traiter
        dans la classe jeu.
    Entrée : event "appuyer sur une touche"
    Sortie :
    """
    touche = event.keysym
    j.controle_joueur(touche)

"""------------------------------------------------------------------------"""



"""Création des différentes fenêtre du jeu
---------------------------------------------------------------------------"""
#Création fenetre principale du jeu
app_jeu = Tk()
app_jeu.title("Spicy'nvader")
#Fenetre en 720x480 et en premier plan
app_jeu.geometry("820x580")
app_jeu.attributes('-topmost', 1)


#Création de la zone de jeu
canvas_jeu = Canvas(app_jeu, width=580, height=580, bg="blue", bd=0)
canvas_jeu.grid(row=1, column=1, rowspan=3,sticky="W")

"""------------------------------------------------------------------------"""



"""Création des éléments hors de la zone de jeu
---------------------------------------------------------------------------"""
#Initialisation du score et Création affichage du score
score = IntVar()
aff_score = Label(app_jeu, textvariable = score)
aff_score.grid(row=1, column=2)

#Création du bouton quitter
jouer = Button(app_jeu, text = "Jouer", command = jeu.jeu)
jouer.grid(row=2, column=2)

#Création du bouton quitter
quitter = Button(app_jeu, text = "Quitter", command = app_jeu.destroy)
quitter.grid(row=3, column=2)

"""------------------------------------------------------------------------"""



"""Détection de la pression d'une touche du clavier
---------------------------------------------------------------------------"""
#détection touche enfoncée
canvas_jeu.focus_set()
canvas_jeu.bind("<KeyPress>", clavier)

"""------------------------------------------------------------------------"""



"""Initialisation des éléments dynamiques du jeu
---------------------------------------------------------------------------"""
j = jeu.jeu(app_jeu, canvas_jeu)

"""------------------------------------------------------------------------"""



app_jeu.mainloop()