import os

def CrearMenu():
    dicopcion = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
    }
    titulo = """
    +++++++++++++++++++++++++++++++
    +       MENU LIGA BEPLAY      +
    +++++++++++++++++++++++++++++++
    """
    
    print(titulo)
    
    try:
        opciones = '1. Agregar Equipo\n2. Registrar Fecha\n3. Ver Tabla de Clasificaciones\n4. Reportes\n5. Salir'
        print(opciones)
        op = str(input('selecciones una opciones: '))
        if (op not in dicopcion):
            return CrearMenu()
            
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        return CrearMenu()
        
    else:
        return op
    
    