# -*- coding: utf-8 -*-
"""
Header:
    Lien GIT : https://github.com/Elliot-Garcia/TPs_CS-DEV
    Objectif : Concevoir un jeu "Spaceinvader"
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
"""

from tkinter import Tk, Label, Button, Frame, Canvas


def deplacement():
    """
    
    """
    
    dx = 5
    dy = 5
    canvas_jeu.move(ennemi_1,dx,dy)
    jeu.after(20,deplacement)

#Création fenetre principale du jeu
jeu = Tk()
jeu.title("Spicy'nvader")
#Fenetre en 720x480 et en premier plan
jeu.geometry("820x580")
jeu.attributes('-topmost', 1)

#Création de la zone de jeu
canvas_jeu = Canvas(jeu, width=580, height=580, bg="blue", bd=5)
canvas_jeu.pack(anchor="w")

ennemi_1 = canvas_jeu.create_oval(250,250,280,280,fill="red")

deplacement()

jeu.mainloop()