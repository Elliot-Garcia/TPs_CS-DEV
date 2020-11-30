# -*- coding: utf-8 -*-
"""
    Objectif : Produits matriciel entre une matrice A et B
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

import fonctions_multiplication_matrices as prod_matr

A = [[1,2,3],
     [1,2,3],
     [1,2,3]]

B = [[1,2,3],
     [1,2,3],
     [1,2,3]]

C = prod_matr.multiplication(A,B)
print(C)

def produit_matriciel(A,B):
    return prod_matr.multiplication(A,B)