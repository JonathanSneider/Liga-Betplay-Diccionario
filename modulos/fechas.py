import os
def Fechass(equiposligaa:dict):
    IsErrornom = True
    while IsErrornom:
        Local = input('Ingrese el nombre del equipo que jugo de local :')
        Visitante = input('Ingrese el nombre del equipo que jugo de visitante :')
        if ((Local not in equiposligaa) or (Visitante not in equiposligaa)):
                print('Ingresaste un equipo que no se encuentra registrado')
                print('intentalo otra vez')
                os.system('pause')
                os.system('cls')
        else:
                
            IsErrornom = False
        
        
    golesvisitante = 0
    goleslocal = 0
        
        
        
    Errorgol = True
    while Errorgol:
        goleslocal = input(f'Ingrese los goles que metio el equipo {Local} :')
        golesvisitante = input(f'Ingrese los goles que metio el equipo {Visitante} :')
        if ((goleslocal.isdigit() == True) and (golesvisitante.isdigit() == True)):
                goleslocal = int(goleslocal)
                golesvisitante = int(golesvisitante)
                Errorgol = False
        elif ((goleslocal.isdigit() == False) or (golesvisitante.isdigit() == False)):
                print('Ingresaste un numero invalido Porfavor intentalo otra vez')
                os.system('Pause')
                os.system('cls')
                        
                        
       
        
                
    for key, value in equiposligaa.items():
        if ((Local not in equiposligaa) or (Visitante not in equiposligaa)):
            print('Ingresaste un equipo que no se encuentra registrado')
            
            
        if key == Local:
            equipolocal = equiposligaa[Local]
            equipolocal['GF'] += goleslocal
            equipolocal['GC'] += golesvisitante
            
            if (goleslocal > golesvisitante):
                    equipolocal['PG'] += 1
                    equipolocal['PJ'] += 1
                    equipolocal['TP'] += 3
            elif (goleslocal < golesvisitante):
                    equipolocal['PJ'] += 1 
                    equipolocal['PJ'] += 1
                    equipolocal['TP'] += 0
                    
            elif (goleslocal == golesvisitante):
                    equipolocal['PE'] += 1 
                    equipolocal['PJ'] += 1
                    equipolocal['TP'] += 1
                    
        if key == Visitante:
            
            equipovisitante = equiposligaa[Visitante]
            equipovisitante['GF'] += golesvisitante
            equipovisitante['GC'] += goleslocal
            
            if (goleslocal < golesvisitante):
                    equipovisitante['PG'] += 1
                    equipovisitante['PJ'] += 1
                    equipovisitante['TP'] += 3
                    
            if (goleslocal > golesvisitante):   
                    equipovisitante['PP'] += 1 
                    equipovisitante['PJ'] += 1
                    equipovisitante['TP'] += 0
                    
            if (goleslocal == golesvisitante):
                    equipovisitante['PE'] += 1 
                    equipovisitante['PJ'] += 1
                    equipovisitante['TP'] += 1
                
    
                       
                    
            
        
            
            
        
            
            
        
    
