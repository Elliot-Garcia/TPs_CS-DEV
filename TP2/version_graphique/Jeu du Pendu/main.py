# -*- coding: utf-8 -*-

"""
Header:
    Lien GIT : https://github.com/Elliot-Garcia/TPs_CS-DEV
    Objectif : Concevoir un jeu du pendu graphique
    Date de réalisation : 05/12/2020
    Par Elliot GARCIA (Gr C)
    A faire : Ajouter des niveau différent,
        Ajouter un menu de choix du jeu, 
        Ajouter un système de meilleur score,
        Créer une fenêtre affichant les scores,
        Rendre la version graphique plus esthétique.
"""

from tkinter import Tk, Label, Button, Frame, IntVar, StringVar, Entry, Canvas, PhotoImage, BooleanVar, font, END


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
    global source_image
    global lien_img
    global img
    global creation_img
    global mot
    
    lettre = str(champ_lettre.get())
    champ_lettre.delete(0,END)
    
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
                info.set('Bravo vous avez gagné, le mot était : '+ mot)
                perdu_victoire()
            
        else:
            chances.set(chances.get()-1) #Si la lettre proposée n'est pas dans le mot, le joueur perds une chance.
            info.set(lettre + ' n\'est pas dans le mot')
            
            if chances.get() == 0:
                info.set('perdu, le mot était : '+ mot)
                perdu_victoire()
            
            else:
                source_image.set(lien_img + str(chances.get()) + '.gif')
                canevas_pendu.delete('ALL')
                img = PhotoImage(file = str(source_image.get()))
                creation_img = canevas_pendu.create_image(150, 150, image = img)
    
    else:
        info.set('saisie incorrecte')

def perdu_victoire():
    """
    But : Actualiser l'affichage lorsque le joueur a perdu ou gagné
    Entrée : Rien
    Sortie : Rien
    """
    
    global source_image
    global img
    global creation_img
    global victoire
    global score
    global chances
    
    if victoire.get() == False:
        source_image.set('data/img_pendu/perdu.gif')
        canevas_pendu.delete('ALL')
        img = PhotoImage(file = str(source_image.get()))
        creation_img = canevas_pendu.create_image(150, 150, image = img)
    else:
        source_image.set('data/img_pendu/gagne.gif')
        canevas_pendu.delete('ALL')
        img = PhotoImage(file = str(source_image.get()))
        creation_img = canevas_pendu.create_image(150, 150, image = img)
        
        score.set(score.get()+chances.get()) #Cacul du score
    
    champ_lettre.grid_forget()
    bouton_proposition.grid_forget()
    bouton_rejouer.grid(row = 4, column = 2)

def save_quit():
    """
    But : Récupérer le score et le pseudo du joueur pour sauvegarder son score
    Entrée : Rien
    Sortie : Rien
    """
    
    global score
    
    pseudo = str(score_pseudo.get())
    if '*' in str(pseudo):
        info.set('Le pseudo ne doit pas contenir le symbole *')
    else:
        if str(pseudo) != '':
            fct.sauvegarde(str(pseudo),score.get())
            app_pendu.destroy()
        else:
            info.set('Pseudo invalide')

def init():
    """
    But : Initialiser le jeu
    Entrée : Rien
    Sortie : Rien
    """
    global affichage
    global chances
    global victoire
    global lien_img
    global source_image
    global img
    global creation_img
    global liste_lettre_dites
    global nb_mots
    global listes_de_mots
    global mot
    
    info.set('')
    
    mot = fct.determination_mot(nb_mots, listes_de_mots)
    mot_affiche = fct.initialisation_affichage_mot(mot)
    affichage.set(mot_affiche)
    chances.set(8) 
    victoire.set(False)
    liste_lettre_dites = [[],[]]

    bouton_rejouer.grid_forget()
    
    champ_lettre.grid(row = 3, column = 1) 
    bouton_proposition.grid(row = 3, column = 2)
    
    source_image.set(lien_img + str(chances.get()) + '.gif')
    canevas_pendu.delete('ALL')
    img = PhotoImage(file = str(source_image.get()))
    creation_img = canevas_pendu.create_image(150, 150, image = img)

#Création fenetre principale du jeu
app_pendu = Tk()
app_pendu.title('Jeu du Pendu')
#Fenetre en 720x480 et en premier plan
app_pendu.geometry("720x480")
app_pendu.attributes('-topmost', 1)


fct.tri_list_mots() #On tri toutes les listes de mots.

score = IntVar()
score.set(0)

listes_de_mots = 'data/mots/mots.txt'


#True si le joueur gagne
victoire = BooleanVar()

#Determination d'un mot à faire deviner
nb_mots = fct.initialisation_list_mots(listes_de_mots)
mot = fct.determination_mot(nb_mots, listes_de_mots)
liste_lettre_dites = [[],[]]

#initialisation nombre d'erreur autorisé
chances = IntVar()
chances.set(8)

#initialisation de l'affichage
affichage = StringVar()

#Bouton non affichés pendant la partie
bouton_rejouer = Button(app_pendu, text='Rejouer', command = init)


#Champ d'entrée pour la saisie
champ_lettre = Entry(app_pendu)
champ_lettre.focus_set()

#Bouton de proposition de la saisie
bouton_proposition = Button(app_pendu, text='Proposer', command = verification_actualisation_lettre)

#initialisation image pendu
lien_img = 'data/img_pendu/bonhomme'
source_image = StringVar()
source_image.set(lien_img + str(chances.get()) + '.gif')

#Création Canvas contenant l'image
canevas_pendu = Canvas(app_pendu, width = 300, height = 300)
img = PhotoImage(file = str(source_image.get()))
creation_img = canevas_pendu.create_image(150, 150, image = img)


#initialisation de message info
info = StringVar()
info.set('')

#création label info
label_info = Label(app_pendu, textvariable = info)

#Initialisation du pseudo
pseudo = StringVar()

#Bouton pour sauvegarder le score et quitter le jeu
bouton_sauvegarder_quitter = Button(app_pendu, text='Sauvegarder et Quitter', command = save_quit)

#Champ d'entrée pour la saisie
score_pseudo = Entry(app_pendu)

#Initialisation du jeu
init()


#création label chances
label_chances_text = Label(app_pendu, text = 'Chances restantes : ')
label_chances = Label(app_pendu, textvariable = chances)

#création label score et pseudo
label_score_text = Label(app_pendu, text = 'Score : ')
label_score = Label(app_pendu, textvariable = score)
label_pseudo = Label(app_pendu, text='Pour quitter, veuillez entrer un pseudo : ')

#création label affichage
label_affichage = Label(app_pendu, textvariable = affichage, font=(30))



#Création bouton rejouer
bouton_rejouer = Button(app_pendu, text='Rejouer', command = init)


#Mise en page de tous les widget
label_chances_text.grid(row = 1, column = 2, sticky = 'E')
label_chances.grid(row = 1, column = 3, sticky = 'W')
label_affichage.grid(row = 2, column = 1)
champ_lettre.grid(row = 3, column = 1) 
bouton_proposition.grid(row = 3, column = 2)
canevas_pendu.grid(column = 3)
label_info.grid(row = 4, column = 1)
bouton_rejouer.grid(row = 4, column = 2)
label_score_text.grid(row = 5, column = 2, sticky = 'E')
label_score.grid(row = 5, column = 3, sticky = 'W')
label_pseudo.grid(row = 6, column = 1) 
score_pseudo.grid(row = 6, column = 2) 
bouton_sauvegarder_quitter.grid(row = 6, column = 3)

bouton_rejouer.grid_forget()

app_pendu.mainloop()

