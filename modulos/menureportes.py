import os
def menuReportes():
    opciones = {
        'A': 'Equipo Goleador',
        'B': 'Equipo con mayor puntaje',
        'C': 'Equipo que mas partidos gano',
        'D': 'Total de goles anotados por todos los equipos',
        'E': 'Promedio de goles anotados en el torneo',
        'F': 'Salir'
        }
    titulo = """
    +++++++++++++++++++++++++++++++++++++++++++
    +       MENU DE REPORTES LIGA BEPLAY      +
    +++++++++++++++++++++++++++++++++++++++++++
    """
    
    print(titulo)
    for item, value in opciones.items():
        print(f'{item}: {value}')
    try:
        op = input('Seleccione una opcion: ').upper()
    except:
        print('Error intentalo otra vez')
        os.system('pause')
        menuReportes()
    else:
        return op
    
    