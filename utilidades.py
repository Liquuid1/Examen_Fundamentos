from random import randrange
from numpy import sum
import csv


def menu():
    menu = """            SELECCIONA
********************************
[1] Asignar sueldos aleatorios
[2] Clasificar sueldos
[3] Ver estadísticas.
[4] Reporte de sueldos
[5] Salir del programa
--> """
    print(menu,end="")

def validar_int(menor,mayor):
    while True:
        try:
            op = int(input())
            if op<menor or op>mayor:
                raise ValueError
            else:
                return op
        except:
            print("Selecciona una opción valida --> ",end="")
    
def asignar_sueldos(lista_nombres,lista_resultado):
    for nombre in lista_nombres:
        nom = nombre
        sueldo = randrange(300000,2500000)

        dic = {"nombre":nom,"sueldo":sueldo}
        lista_resultado.append(dic)
    print("Sueldos asignados!")
    
def clasificar_sueldos(lista):
    if len(lista)==0:
        print("Necesita asignar los sueldos antes. Intentelo de nuevo")
    else:
        bajos = []
        medios = []
        altos = []
        sueldos = [trabajador["sueldo"] for trabajador in lista]

        for trabajador in lista:
            if trabajador["sueldo"]<800000:
                bajos.append(trabajador)
            elif trabajador["sueldo"]<2000000:
                medios.append(trabajador)
            else:
                altos.append(trabajador)

        print(f"Sueldos menores a $800.000 TOTAL {len(bajos)}")
        print("Nombre empleado          Sueldo")
        print()
        for a in bajos:
            print(a["nombre"],"$"+str(a["sueldo"]),sep=" "*(24-len(a["nombre"])))
        print()

        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL {len(medios)}")
        print("Nombre empleado          Sueldo")
        print()
        for a in medios:
            print(a["nombre"],"$"+str(a["sueldo"]),sep=" "*(24-len(a["nombre"])))
        print()

        print(f"Sueldos superiores a $2.000.000 TOTAL {len(altos)}")
        print("Nombre empleado          Sueldo")
        print()
        for a in altos:
            print(a["nombre"],"$"+str(a["sueldo"]),sep=" "*(24-len(a["nombre"])))
        print()

        print(f"TOTAL SUELDOS ${sum(sueldos)}")

def sueldo_menor(lista):
    bajo = lista[0]
    for a in lista:
        if bajo["sueldo"]>a["sueldo"]:
            bajo = a
    
    return bajo

def sueldo_mayor(lista):
    alto = lista[0]
    for a in lista:
        if alto["sueldo"]<a["sueldo"]:
            alto = a
    
    return alto

def promedio_sueldos(lista):
    sueldos = [trabajador["sueldo"] for trabajador in lista]
    return int((sum(sueldos))/(len(sueldos)))


def estadísticas(lista):
    if len(lista)==0:
        print("Necesita asignar los sueldos antes. Intentelo de nuevo")
    else:
        menor = sueldo_menor(lista)
        mayor = sueldo_mayor(lista)
        promedio = promedio_sueldos(lista)
        print(f"Sueldo más bajo: {menor["nombre"]} ${menor["sueldo"]}")
        print(f"Sueldo más alto: {mayor["nombre"]} ${mayor["sueldo"]}")
        print(f"El promedio de los sueldos es ${promedio}")
        print(f"La media geometrica es ${promedio}")
        print()

def reporte(lista):
    if len(lista)==0:
        print("Necesita asignar los sueldos antes. Intentelo de nuevo")
    else:
        exportar = []
        campos = ["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"]

        for a in lista:
            nom = a["nombre"]
            sueldo_bruto = a["sueldo"]
            afp = int(sueldo_bruto * 0.12)
            salud = int(sueldo_bruto * 0.07)
            sueldo_liquido = sueldo_bruto - afp - salud

            dic = {campos[0]:nom,campos[1]:sueldo_bruto,campos[2]:salud,campos[3]:afp,campos[4]:sueldo_liquido}
            exportar.append(dic)
        
        with open("Reporte Sueldos.csv",'w',newline="") as archivo:
            esc = csv.DictWriter(archivo,fieldnames=campos)
            esc.writeheader()
            esc.writerows(exportar)

        print("Nombre empleado     Sueldo base         Descuento Salud     Descuento AFP       Sueldo Liquido")
        for trabajador in exportar:
            print(trabajador[campos[0]]," "*(18-len(trabajador[campos[0]])),"$"+str(trabajador[campos[1]])," "*(17-len(str(trabajador[campos[1]]))),"$"+str(trabajador[campos[2]])," "*(17-len(str(trabajador[campos[2]]))),"$"+str(trabajador[campos[3]])," "*(17-len(str(trabajador[campos[3]]))),"$"+str(trabajador[campos[4]]))
        