# -*- coding: utf-8 -*-
"""
Header:
    Objectif : Mettre en place les fonctions qui permettront de calculer ce que
                l'on doit payer aux impots selon les revenus annuel
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

tranche = [0,9964,27519,73779,156244,-1]
taux_imposition = [0,0.14,0.3,0.41,0.45] #Taux d'imposition en fonction des tranches :
        #tranche 1 = 0%, tranche 2 = 14%, ...

def trouver_tranche(revenu):
    """
    But : trouver la tranche d'imposition qui correspond au revenu
    Entrée : revenu = Revenu annuel (float)
    Sortie : i = numéro de la tranche d'imposition
    """
    
    i = 0
    while i < 5 and revenu > tranche[i]:
        i += 1
    return i

def calcul_impots_tranche(revenu, num_tranche):
    """
    But : calculer les impots de la tranche à partir des revenus et de la tranche d'imposition correspondant
    Entrée : revenu = Revenu annuel 
            num_tranche = Numéro de la tranche d'imposition correspondant au revenu
    Sortie : Les impots à payer pour la tranche
    """
    
    return (revenu - tranche[num_tranche-1])*taux_imposition[num_tranche-1]

def calcul_impots_sup(num_tranche):
    """
    But : Calculer la somme supplémentaire lié aux tranches inférieur à celle correspondant au revenu annuel
    Entrée : num_tranche = Numéro de la tranche d'imposition correspondant au revenu
    Sortie : Les impots supplémentaire à payer par rapport aux tranches inférieur
    """
    
    impots_sup = 0
    
    while num_tranche > 2:
        num_tranche -= 1
        impots_sup += (tranche[num_tranche] - tranche[num_tranche-1])*taux_imposition[num_tranche-1]
    
    return impots_sup