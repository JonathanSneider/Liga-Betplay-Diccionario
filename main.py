import os
import modulos.menu as mn
import modulos.equipos as eq
import modulos.fechas as fe
import modulos.tabla as tb
import modulos.menureportes as mnr
import modulos.repotes as re

if __name__ == '__main__':
    equiposliga = {}
    isAppRun = True
    while isAppRun:
        op = mn.CrearMenu()
        if op == '1':
            os.system('cls')
            runAddTeam = True
            while runAddTeam:
                os.system('cls')                
                eq.AddTeam(equiposliga)
                runAddTeam = bool(input('Desea Agregar otro equipo? S(Si) o ESTER(No) :'))
        elif op  == '2':
            os.system('cls')
            runFecha = True
            while runFecha:
                os.system('cls')
                fe.Fechass(equiposliga)
                runFecha = bool(input('Desea agregar otra fecha? S(Si) o ENTER(No)'))
        elif op == '3':
            os.system('cls')
            runTabla = True
            while runTabla:
                tb.Tabla(equiposliga)
                runTabla = bool(input('Para continuar presiones ENTER'))
        elif op == '4':
            os.system('cls')
            IsRunMn = True
            while IsRunMn:
                kkk = mnr.menuReportes()
                if kkk == 'A':
                    IsTeamMaxgol = True
                    while IsTeamMaxgol:
                        re.os.system('cls')
                        re.reportes(equiposliga)
                        maxequipo = re.reportes(equiposliga)
                        print(f'El equipo que mas goles anoto fue el equipo {maxequipo}')
                        IsTeamMaxgol = bool(input('Presione ENTER para continuar :'))
                        
                if kkk == 'B':
                    IsTeamMaxPts = True
                    while IsTeamMaxPts:
                        re.os.system('cls')
                        re.maxpts(equiposliga)
                        maxpts = re.maxpts(equiposliga)
                        print(f'El equipo que mas puntos tuvo fue el equipo {maxpts}')
                        IsTeamMaxPts = bool(input('Presione ENTER para continuar :'))
                
                if kkk == 'C':
                    IsTeamMaxwin = True
                    while IsTeamMaxwin:
                        re.os.system('cls')
                        re.maxprtwin(equiposliga)
                        maxwins = re.maxprtwin(equiposliga)
                        print(f'El equipo que mas partidos gano fue el equipo {maxwins}')
                        IsTeamMaxwin = bool(input('Presione ENTER para continuar :'))
                        
                if kkk == 'D':
                    IsTogoles = True
                    while IsTogoles:
                        re.os.system('cls')
                        re.totalgol(equiposliga)
                        maxtogol = re.totalgol(equiposliga)
                        print(f'El Total de goles anotados es de {maxtogol}')
                        IsTogoles = bool(input('Presione ENTER para continuar :'))
                        
                if kkk == 'E':
                    IsProGol = True
                    while IsProGol:
                        re.os.system('cls')
                        re.totalgolpro(equiposliga)
                        progoles = re.totalgolpro(equiposliga)
                        print(f'El promedio de gol por equipo es de {progoles}')
                        IsProGol = bool(input('Presione ENTER para continuar :'))
                        
                if kkk == 'F':
                    IsRunMn = False
                           
        elif op == '5':
            isAppRun = False
        
    