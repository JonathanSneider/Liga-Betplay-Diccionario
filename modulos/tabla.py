from tabulate import tabulate
def Tabla(equiposligaa:dict):
    info = []
    for key,value in equiposligaa.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))