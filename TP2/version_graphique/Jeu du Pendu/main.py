# -*- coding: utf-8 -*-

"""
Header:
    Lien GIT : https://github.com/Elliot-Garcia/TPs_CS-DEV
    Objectif : Concevoir un jeu du pendu graphique
    Date de réalisation : 05/12/2020
    Par Elliot GARCIA (Gr C)
    A faire : Actualiser l'image lorsque l'on perds une vie, ajouter des niveau différent
        ajouter un menu de choix du jeu, ajouter un système de meilleur score, rendre la version graphique plus esthétique
"""

from tkinter import Tk, Label, Button, Frame, IntVar, StringVar, Entry, Canvas, PhotoImage, BooleanVar, font


import fonctions as fct


def verification_actualisation_lettre():
    """
    But : Prélever la lettre de Entry et vérifier si elle est est correcte pour ensuite actualiser l affichage
    Entrée : Rien
    Sortie : Rien
    """
    
    global liste_lettre_dites
    global affichage
    global chances
    global victoire
    
    lettre = str(champ_lettre.get())
    
    if len(lettre) == 1:
    
        liste_lettre_dites = fct.lettre_dite(liste_lettre_dites[1], lettre)
        verification = fct.verification_lettre_dans_mot(mot, lettre)
        
        if liste_lettre_dites[0]:
            info.set('Lettre déjà dites')

        elif verification[0]:
            #actualisation de la variable affichage
            affichage.set(fct.actualiser_affichage_mot(affichage.get(), lettre, verification[1]))
            
            victoire.set(fct.verification_victoire(affichage.get()))
            if victoire.get():
                info.set('Bravo vous avez gagné')
            
        else:
            chances.set(chances.get()-1) #Si la lettre proposée n'est pas dans le mot, le joueur perds une chance.
            info.set(lettre + ' n\'est pas dans le mot')
            
            # source_image.set(lien_img + str(chances.get()) + '.gif')
            # canevas_pendu.delete(ALL)
            # img = PhotoImage(file = str(source_image.get()))
            # creation_img = canevas_pendu.create_image(80, 80, image = img)
            
            if chances.get() == 0:
                info.set('perdu')
    
    else:
        info.set('saisie incorrecte')

                


#Création fenetre principale du jeu
app_pendu = Tk()
app_pendu.title('Jeu du Pendu')
#Fenetre en 720x480 et en premier plan
app_pendu.geometry("720x480")
app_pendu.attributes('-topmost', 1)


fct.tri_list_mots() #On tri toutes les listes de mots.
    
jouer = True
meilleur_score = 0
listes_de_mots = 'data/mots/mots.txt'


#True si le joueur gagne
victoire = BooleanVar()
victoire.set(False)

#Determination d'un mot à faire deviner
nb_mots = fct.initialisation_list_mots(listes_de_mots)
mot = fct.determination_mot(nb_mots, listes_de_mots)
liste_lettre_dites = [[],[]]

#initialisation nombre d'erreur autorisé
chances = IntVar()
chances.set(8) 

#création label chances
label_chances_text = Label(app_pendu, text = 'Chances restantes : ')
label_chances = Label(app_pendu, textvariable = chances)


#initialisation de l'affichage
affichage = StringVar()
affichage.set(fct.initialisation_affichage_mot(mot))

#création label affichage
label_affichage = Label(app_pendu, textvariable = affichage, font=(30))


#initialisation image pendu
lien_img = 'data/img_pendu/bonhomme'
source_image = StringVar()
source_image.set(lien_img + str(chances.get()) + '.gif')

#Création Canvas contenant l'image
canevas_pendu = Canvas(app_pendu, width = 200, height = 200)
img = PhotoImage(file = str(source_image.get()))
creation_img = canevas_pendu.create_image(80, 80, image = img)

#Champ d'entrée pour la saisie
champ_lettre = Entry(app_pendu)
champ_lettre.focus_set()

#Bouton de proposition de la saisie
bouton_proposition = Button(app_pendu, text='Proposer', command = verification_actualisation_lettre)


#initialisation de message info
info = StringVar()
info.set('')

#création label info
label_info = Label(app_pendu, textvariable = info)


#Mise en page de tous les widget
label_chances_text.grid(row = 1, column = 2, sticky = 'E')
label_chances.grid(row = 1, column = 3, sticky = 'W')
label_affichage.grid(row = 2, column = 1)
champ_lettre.grid(row = 3, column = 1) 
bouton_proposition.grid(row = 3, column = 2)
canevas_pendu.grid(column = 3)
label_info.grid(row = 4, column = 1)





app_pendu.mainloop()

