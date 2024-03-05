import os
def reportes(equiposligaa:dict):
    golesmax = max(equiposligaa.values(), key=lambda x: x['GF'])
    return golesmax['nombre']
    
def maxpts(equipossligaa:dict):
    ptsmax = max(equipossligaa.values(), key=lambda x: x['TP'])
    return ptsmax['nombre']
        
def  maxprtwin(equipossliga:dict):
    winmax = max(equipossliga.values(), key=lambda x: x['PG'])
    return winmax['nombre']

def totalgol(equipossliga:dict):
    golesto = 0
    for key,value in equipossliga.items():
        golesto += value['GF'] 
    return golesto 

def totalgolpro(equipossliga:dict):
    golespro = 0
    for key,value in equipossliga.items():
        golespro += value['GF'] 
    cantidadTeam = len(equipossliga)
    golpromedio = golespro * 1000 // cantidadTeam / 1000
    
    return golpromedio