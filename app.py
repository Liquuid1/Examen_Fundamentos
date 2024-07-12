import utilidades as ff
import os

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
dict_trabajadores = []
op = 0

while op!=5:
    os.system('cls')
    ff.menu()
    op = ff.validar_int(1,5)

    if op==1:
        os.system('cls')
        ff.asignar_sueldos(trabajadores,dict_trabajadores)
        os.system('pause')
    elif op==2:
        os.system('cls')
        ff.clasificar_sueldos(dict_trabajadores)
        os.system('pause')
    elif op==3:
        os.system('cls')
        ff.estadísticas(dict_trabajadores)
        os.system('pause')
    elif op==4:
        os.system('cls')
        ff.reporte(dict_trabajadores)
        os.system('pause')

os.system('cls')
print("Finalizando programa...")
print("Desarrollado por David Zúñiga")
print("RUT 20.099.797-2")