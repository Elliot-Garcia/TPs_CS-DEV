# -*- coding: utf-8 -*-
"""
    Objectif : Reconnaitre et lister les nombre dit 'tricolore'
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

def taille_nombre(n):
    """
    But : calculer le nombre de chiffre dans le nombre n
    Entrées : n = un entier (int)
    Sortie : un entier = le nombre de chiffre dans le nombre
    """
    taille_nombre = 0 #la taille du nombre
    
    while int(n/(10**taille_nombre)) != 0:
        taille_nombre += 1
    
    return taille_nombre

def decoupage_de_n(n,taille_n):
    """
    But : découper n en une liste de chacun des chiffre qui le compose
    Entrées : n = un entier (int)
            taille_n = le nombre de chiffre qui compose n (int)
    Sortie : liste composée des chiffre composant n
    """

    L = []
    for i in range(taille_n):
        L.append(int(n/(10**(taille_n-i-1))))
        n = n - L[i]*(10**(taille_n-i-1))

    return L

def tricolore(n):
    """
    But : vérifier qu'un nombre est tricolore
    Entrées : n = un entier (int)
    Sortie : un booléen (True si n tricolore, False sinon)
    """
    
    n = n**2
    
    taille_n = taille_nombre(n)
    L = decoupage_de_n(n,taille_n) #la liste de chiffre qui compose n**2
    for i in range(len(L)):
        if L[i] != 1 and L[i] != 4 and L[i] != 9:
            return False
    return True

def tout_les_tricolores(N):
    """
    But : trouver tous les nombres tricolores inferieur à N
    Entrées : N = un entier (int)
    Sortie : une liste d'entier tricolore
    """
    
    L=[]
    
    for i in range(N):
        if tricolore(i+1):
            L.append(i+1)
    
    return L