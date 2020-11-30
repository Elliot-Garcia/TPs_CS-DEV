# -*- coding: utf-8 -*-
"""
    Objectif : Mettre en place les fonctions de produits matriciel entre une
            matrice A et B
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

def multiplication(A,B):
    """
    But : multiplier les deux matrices (liste de liste) -> A*B
    Entrée : A = liste de liste
            B = liste de liste
    Sortie : la liste de liste correspondant à l'application C=A*B
    """
    
    if len(A[0]) != len(B):
        return 'Matrice non compatible'
    
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    #création de la matrice C=A*B aux bonnes dimension
    
    for i in range(len(C)):
        for j in range(len(C[0])):
            
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    
    return C