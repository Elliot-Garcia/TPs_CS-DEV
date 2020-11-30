# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Calculer ce que l'on doit payer aux impots selon les revenus annuel
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

import fonctions_impots as impots


def mes_impots(revenu):
    """
    But : Calculer ses impots en fonction de ses revenus annuel
    Entrée : revenu = revenu annuel (float)
    Sortie : somme des impots à payer
    """
    
    num_tranche = impots.trouver_tranche(revenu)
        #on récupère la valeurs de la tranche d'imposition
    
    impots_a_payer = impots.calcul_impots_tranche(revenu, num_tranche) +\
                    impots.calcul_impots_sup(num_tranche)
    
    return impots_a_payer