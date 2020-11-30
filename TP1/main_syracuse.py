# -*- coding: utf-8 -*-
"""
    Objectif : Trouver N entre 1 et 1000 pour lequel le temps de vol de
                la suite de Syracuse est le plus long
                et trouver N entre 1 et 1000 pour lequel l'altitude de
                la suite de Syracuse et le plus haut
    Date de réalisation : 23/11/2020
    Par Elliot GARCIA (Gr C)
"""

import fonctions_syracuse as syr

S = syr.syracuse(1)
tps_de_vol = syr.temps_de_vol(S)
alt = syr.altitude(S)

N_temps_de_vol_max = [1, tps_de_vol]
N_altitude_max = [1, alt]


for i  in range(1,1000):
    
    S = syr.syracuse(i+1)
    
    tps_de_vol = syr.temps_de_vol(S)
    alt = syr.altitude(S)
    
    if tps_de_vol > N_temps_de_vol_max[1]:
        N_temps_de_vol_max = [i+1,tps_de_vol]
    
    if alt > N_altitude_max[1]:
        N_altitude_max = [i+1, alt]

print('le temps de vol max est',N_temps_de_vol_max[1],'atteint pour N =',N_temps_de_vol_max[0])
print('l\'altitude max est',N_altitude_max[1],'atteint pour N =',N_altitude_max[0])