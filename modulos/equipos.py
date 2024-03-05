import os
equiposligaa = dict
def AddTeam(equiposligaa:dict):
    nombree = input('ingrese el nombre del equipo :')
    equiposligaa[nombree] = {
        'nombre': nombree,
        'PJ': 0,
        'PG': 0,
        'PP': 0,
        'PE': 0,
        'GF': 0,
        'GC': 0,
        'TP': 0
    }     
    
