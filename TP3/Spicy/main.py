# -*- coding: utf-8 -*-
"""
Header:
    Lien GIT : https://github.com/Elliot-Garcia/TPs_CS-DEV
    Objectif : Concevoir un jeu "Spaceinvader"
    Date de réalisation : 14/12/2020
    Par Elliot GARCIA (Gr C)
    À Faire : (voir d'amélioration) Créer plus de niveau, ajouter des ennemis différents
               et pourquoi pas un boss final avec un crédit de fin.
"""


from tkinter import Tk, Label, Button, Canvas, StringVar, PhotoImage, Toplevel, Entry, Menu
from tkinter.filedialog import askopenfilename
from os import listdir

import jeu as jeu
import marchand as m



"""Fonction de lancement de la partie
---------------------------------------------------------------------------"""       
def lancer_partie():
    """
    But : Lancer la partie en affichant le premier niveau et en enlevant le bouton "Commencer la partie" et le bouton "Charger une partie"
    Entrée :
    Sortie :
    """
    bouton_jouer.grid_forget()
    bouton_charger.grid_forget()
    j.lancer_niveau()


"""------------------------------------------------------------------------"""



"""Chargement des scores
---------------------------------------------------------------------------"""       
def liste_scores_et_joueur():
    """
    But : Trouver dans les dossiers de Sauvegardes tous les scores avec les pseudos
    Entrée :
    Sortie : Liste de liste contenant les pseudos et les scores trier du meilleur score au moins bon [[score1, pseudo1], [...], ...]
    """
    liste_scores = []
    
    fichiers = [f for f in listdir("data/sauvegardes")]
    for i in range(len(fichiers)):
        sauv = fichiers[i]
        f = open("data/sauvegardes/" + sauv, "r")
        f.readline()
        f.readline()
        score = f.readline().split("\n")
        score = score[0]
        f.close()
        
        liste_scores.append([int(score),sauv])
        
    return sorted(liste_scores, reverse = True)

"""------------------------------------------------------------------------"""



"""Fonction de contrôle de l'avatar en fonction des touches saisies par le joueur
---------------------------------------------------------------------------"""       
def clavier(event):
    """
    But : Récupérer les touches du clavier entrées par le joueur pour les traiter
        dans la classe jeu.
    Entrée : event "appuyer sur une touche"
    Sortie :
    """
    touche = event.keysym
    j.controle_joueur(touche)

"""------------------------------------------------------------------------"""

entre_pseudo = "" #Initialisation de ce qui sera l'Entry pour le pseudo
    
"""Fonctionnalités du menu de sauvegarde et pour quitter le jeu
---------------------------------------------------------------------------"""

def sauvegarde():
    """
    But : Si le joueur choisi de Sauvegarder, récupère le pseudo choisi et va écrire
        les informations du joueur dans un fichier .txt au nom de son pseudo dans
        le dossier "sauvegardes" dans le data. Puis fermeture du jeu
    Entrée :
    Sortie :
    """
    
    global entre_pseudo
    global pseudo
    
    pseudo.set(entre_pseudo.get())
    
    if pseudo.get() != "":
        f = open("data/sauvegardes/" + pseudo.get() + ".txt", "w")
        #Récupération des infos du joueur :
        niv = j.niveau
        vie = j.vie.get()
        score = j.score.get()
        argent = j.argent_tot #On utilise info tot comme ça le joueur perdra toute ses améliorations mais pourra les racheter à sa guise
        
        liste_infos_joueur = [niv,vie,score,argent]
        
        for i in range (len(liste_infos_joueur)):
            f.write(str(liste_infos_joueur[i]) + "\n")
            
        f.close()
        
        app_jeu.destroy()
        
def sauvegarde_etou_quitter():
    """
    But : Lance le processus de sauvegarde et quitte le jeu (le joueur garde le
            choix de ne pas sauvegarder)
    Entrée :
    Sortie :
    """
    
    global entre_pseudo
    global pseudo
    
    sauv_et_quit = Toplevel(bg = "black")
    Label(sauv_et_quit, font = 80, fg="white", bg = "black", text="Menu de sauvegarde de la progression", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    entre_pseudo = Entry(sauv_et_quit, bg = "gray")
    entre_pseudo.grid(row=2, column = 2)
    
    sauv_et_quit.attributes("-topmost", True)
    
    sauv_et_quit.grab_set()
    sauv_et_quit.transient(app_jeu)
    
    #Elements pour quitter en sauvegardant
    Label(sauv_et_quit, fg = "white", bg = "black", text = "Entrez un pseudo pour sauvegarder votre progression").grid(row=2, column = 1)
    Label(sauv_et_quit, font = 40, fg = "red", bg = "black", text = "Attention, si vous entrez un pseudo déjà existant, vous écraserez la précédante sauvegarde du pseudo", padx = 20, pady = 20).grid(row=3, column = 1,columnspan=4)
    
    Button(sauv_et_quit, fg = "white", bg = "black", text = "Sauvegarder et quitter", padx = 20, pady = 20, command = sauvegarde).grid(row=2, column=4)
    #Elements pour quitter sans sauvegarder
    Button(sauv_et_quit, fg = "white", bg = "black", text = "Quitter sans sauvegarder", command = app_jeu.destroy).grid(row=4, column=1)
    
    #Elements pour ne finalement pas quitter le jeu
    Button(sauv_et_quit, fg = "white", bg = "black", text = "Annuler", command = sauv_et_quit.destroy).grid(row=4, column=3)

"""------------------------------------------------------------------------"""



"""Création des différentes fenêtre du jeu
---------------------------------------------------------------------------"""
#Création fenetre principale du jeu
app_jeu = Tk()
app_jeu.title("Spicy'nvader")
#Fenetre en 720x480 et en premier plan
app_jeu.geometry("820x581")
app_jeu.attributes('-topmost', 1)

#Initialisation de la variable pseudo
pseudo = StringVar()
pseudo.set("")

#Création de la zone de jeu (Canevas + Image de fond)
canvas_jeu = Canvas(app_jeu, width=580, height=580)
img_fond = PhotoImage(file = "data/image/bg_espace.gif")
canvas_jeu.create_image(290, 290, image = img_fond)
canvas_jeu.grid(row=1, column=1, rowspan=16,sticky="w")

"""------------------------------------------------------------------------"""



"""Initialisation des éléments dynamiques du jeu
---------------------------------------------------------------------------"""
j = jeu.jeu(app_jeu, canvas_jeu)

"""------------------------------------------------------------------------"""



"""Fonction de chargement d'une sauvegarde
---------------------------------------------------------------------------"""
def chargement_sauv():
    """
    But : Ouvre une 'popup' de choix de dossier directement dans le dossier
        sauvegarde pour faire choisir au joueur une sauvegarde à charger.
        Puis chargement de la partie choisi en commençant par le menu marchand.
    Entrée :
    Sortie :
    """
    
    file = askopenfilename(title="Choisir une sauvegarde", 
                           initialdir = r"data/sauvegardes",
                           multiple = False,
                           filetypes = [("Sauvegardes", ".txt")])
    
    bouton_jouer.grid_forget()
    bouton_charger.grid_forget()
    
    sauv_choisi = open(file, "r")
    j.niveau = int(sauv_choisi.readline())
    j.vie.set(int(sauv_choisi.readline()))
    j.score.set(int(sauv_choisi.readline()))
    j.argent = float(sauv_choisi.readline())
    j.txt_argent.set(str(j.argent) + " $€")
    
    sauv_choisi.close()
    
    j.cooldown = 1
    j.rapidite = 5
    j.multiplicateur_ennemis = 1
    j.multiplicateur_bonus = 1
    
    j.M = m.marchand(j)
    j.affichage_fin()

"""------------------------------------------------------------------------"""


"""Création des éléments hors de la zone de jeu
---------------------------------------------------------------------------"""
#Création de la zone hors du jeu
canvas_menu = Canvas(app_jeu, width=240, height=580, bg="black", bd=0)
canvas_menu.grid(row=1, column=2, rowspan=12, columnspan=3, sticky="W")

#Initialisation du vie/score/argent et Création affichage du score/argent

Label(app_jeu, font=150, fg="red", bg = "black", text = "Spicy'nvader").grid(row=1, column=2, columnspan=3)

label_vies = Label(app_jeu, font=50, fg="white", bg = "black", text = "Vies restantes : ")
label_vies.grid(row=2, column=2)
aff_vies = Label(app_jeu, font=50, fg="white", bg = "black", textvariable = j.vie)
aff_vies.grid(row=2, column=3)

label_score = Label(app_jeu, fg="white", bg = "black", text = "Votre score est de :")
label_score.grid(row=4, column=2)
aff_score = Label(app_jeu, fg="white", bg = "black", textvariable = j.score)
aff_score.grid(row=4, column=3)

label_argent = Label(app_jeu, fg="white", bg = "black", text = "Spicy-cash : ")
label_argent.grid(row=5, column=2)
aff_argent = Label(app_jeu, fg="white", bg = "black", textvariable = j.txt_argent)
aff_argent.grid(row=5, column=3)

#Création du bouton jouer
bouton_jouer = Button(app_jeu, anchor="center", fg="white", bg = "black", text = "Commencer une nouvelle partie", command = lancer_partie)
bouton_jouer.grid(row=6, column=1)

#Création du bouton pour charger une partie
bouton_charger = Button(app_jeu, anchor="center", fg="white", bg = "black", text = "Charger une partie", command = chargement_sauv)
bouton_charger.grid(row=7, column=1)

#Création du bouton quitter
quitter = Button(app_jeu, fg="white", bg = "black", text = "Quitter", command = sauvegarde_etou_quitter)
quitter.grid(row=10, column=2)

"""------------------------------------------------------------------------"""



"""Création des fonctions pour le menu
---------------------------------------------------------------------------"""
def notice_jeu_controle():
    """
    But : Afficher la "popup" dans le menu "notice_jeu" contenant un label expliquant les contrôles du jeu
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="Les contrôles du jeu sont :\n --> Droite : Pour aller à droite\n <-- Gauche : Pour aller à gauche\n [    ] Espace : Pour tirer", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Ok!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)

def notice_jeu_heros():
    """
    But : Afficher la "popup" dans le menu "notice_jeu" contenant un label expliquant qui est votre avatar
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="Vous êtes un grand aventurier galactique bien maladroit au début.\n En effet vous êtes lent, vous tirez molement... mais vous allez vous\n améliorer afin de vaincre les méchants (cf Magasin) !", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Ok!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)

def notice_jeu_ennemis():
    """
    But : Afficher la "popup" dans le menu "notice_jeu" contenant un label expliquant les différents ennemis
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="Les ennemis sont méchants avec leur chapka (dessiné par mes soins) blablabla ils sont méchant méchant\n En bref, vous avez des lances missiles, tuez TOUT!\n Vos ennemis sont de deux types : \n Vous aurez les ennemis simples et les ennemis bonus (à la chapka doré).\n Ces derniers sont rapide mais ils rapporte plein de points !", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Ok!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)

def notice_jeu_magasin():
    """
    But : Afficher la "popup" dans le menu "notice_jeu" contenant un label expliquant le magasin
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="En tuant des ennemis, vous allez gagner du Spicy-Cash ($€).\n Cet argent vous sert à chaque fin de niveau pour acheter des améliorations qui sont :\n -> Amélioration de la vitesse de tire\n -> Amélioration de la vitesse de déplacement\n -> Amélioration des multiplicateurs de point", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Ok!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)

def a_propos_space():
    """
    But : Afficher la "popup" dans le menu "à propos" contenant un label l'histoire de Space Invader
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="Space Invader est un jeu inventé par Taito en 1978 (d'après wikipédia XD)\n et voilà... c'est à peu près tout...\n ça ne vous direz pas de jouer plutôt ?", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Ok!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)

def a_propos_spicy():
    """
    But : Afficher la "popup" dans le menu "à propos" contenant un label l'histoire de Spicy industry
    Entrée :
    Sortie :
    """
    
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.grab_set()
    pop.transient(app_jeu)
    
    Label(pop, text="La spicy company !\n Nait d'une blague entre ami(e)s, cette entreprise a déjà à son actif un magnifique site web d'agence de voyage.\n L'entreprise (initialement composée de 3 patrons/employés) est malheureusement aujourd'hui scindée en trois groupes.\n Cependant elle continue de vous vendre du rêve et des expériences Spicyyy dans ce tout nouveau jeu : Spicy'nvader !!!", padx = 20, pady = 40).grid(row=1, column=1, columnspan=3)
    Button(pop, text = "Fantastique!", padx = 20, command=pop.destroy).grid(row = 2, column = 2)
    
"""------------------------------------------------------------------------"""



"""Création des éléments du menu
---------------------------------------------------------------------------"""
menu_app = Menu(app_jeu)

#Partie scores trier du meilleur au moins bon
aff_liste_scores = Menu(menu_app, tearoff = 0)
liste_scores = liste_scores_et_joueur()
for i in range(len(liste_scores)):
    aff_liste_scores.add_command(label = liste_scores[i][1][0:-4] + " : " + str(liste_scores[i][0]))

#Partie notice du jeu
notice_jeu = Menu(menu_app, tearoff = 0)
notice_jeu.add_command(label = "Les contrôles", command = notice_jeu_controle)
notice_jeu.add_command(label = "Votre héros", command = notice_jeu_heros)
notice_jeu.add_command(label = "Les ennemis", command = notice_jeu_ennemis)
notice_jeu.add_command(label = "Le magasin", command = notice_jeu_magasin)

#Partie à propos
a_propos = Menu(menu_app, tearoff = 0)
a_propos.add_command(label = "Space invader", command = a_propos_space)
a_propos.add_command(label = "Spicy company", command = a_propos_spicy)

#Partie skins
skins = Menu(menu_app, tearoff = 0)
skins.add_command(label = "Standard", command = j.skin1)
skins.add_command(label = "Force VIOLETTE", command = j.skin2)
skins.add_command(label = "Vegan", command = j.skin3)
skins.add_command(label = "Non Binaire", command = j.skin4)


menu_app.add_cascade(label = "Listes des scores", menu = aff_liste_scores)
menu_app.add_cascade(label = "Notices du jeu", menu = notice_jeu)
menu_app.add_cascade(label = "À propos", menu = a_propos)
menu_app.add_cascade(label = "Changer de skin", menu = skins)


app_jeu.config(menu = menu_app)
"""------------------------------------------------------------------------"""



"""Détection de la pression d'une touche du clavier
---------------------------------------------------------------------------"""
#détection touche enfoncée
canvas_jeu.focus_set()
canvas_jeu.bind("<KeyPress>", clavier)

"""------------------------------------------------------------------------"""

app_jeu.mainloop()