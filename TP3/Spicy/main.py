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


"""Fonction de lancement de la partie
---------------------------------------------------------------------------"""       
def lancer_partie():
    """
    But : Lancer la partie en affichant le premier niveau et en enlevant le bouton "Commencer la partie"
    Entrée :
    Sortie :
    """
    bouton_jouer.grid_forget()
    j.lancer_niveau()

"""------------------------------------------------------------------------"""



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
canvas_jeu.grid(row=1, column=1, rowspan=10,sticky="W")

"""------------------------------------------------------------------------"""



"""Initialisation des éléments dynamiques du jeu
---------------------------------------------------------------------------"""
j = jeu.jeu(app_jeu, canvas_jeu)

"""------------------------------------------------------------------------"""



"""Création des éléments hors de la zone de jeu
---------------------------------------------------------------------------"""
#Création de la zone hors du jeu
canvas_menu = Canvas(app_jeu, width=240, height=580, bg="black", bd=0)
canvas_menu.grid(row=1, column=2, rowspan=10, columnspan=3, sticky="W")

#Initialisation du score/argent et Création affichage du score/argent

label_score = Label(app_jeu, fg="white", bg = "black", text = "Votre score est de :")
label_score.grid(row=2, column=2)
aff_score = Label(app_jeu, fg="white", bg = "black", textvariable = j.score)
aff_score.grid(row=2, column=3)

label_argent = Label(app_jeu, fg="white", bg = "black", text = "Spicy-cash : ")
label_argent.grid(row=3, column=2)
aff_argent = Label(app_jeu, fg="white", bg = "black", textvariable = j.txt_argent)
aff_argent.grid(row=3, column=3)

#Création du bouton jouer
bouton_jouer = Button(app_jeu, anchor="center", fg="white", bg = "black", text = "Commencer la partie", command = lancer_partie)
bouton_jouer.grid(row=5, column=1)

#Création du bouton quitter
quitter = Button(app_jeu, fg="white", bg = "black", text = "Quitter", command = app_jeu.destroy)
quitter.grid(row=9, column=2)

"""------------------------------------------------------------------------"""



"""Détection de la pression d'une touche du clavier
---------------------------------------------------------------------------"""
#détection touche enfoncée
canvas_jeu.focus_set()
canvas_jeu.bind("<KeyPress>", clavier)

"""------------------------------------------------------------------------"""



app_jeu.mainloop()