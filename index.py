from conexion import Conexion
from beautifultable import BeautifulTable
import os
import time

from BaseDato import BaseDato



os.system('cls')
print ("Inciando la conexion ...")
Conexion.getConnection()
os.system('cls')


menu = BeautifulTable()
menu.columns.header = ['=== Sistema de prestamos de libro ==='] 
menu.rows.append(['1. Crear campos '])
menu.rows.append(['2. Eliminar campos'])

def crearT():
    os.system('cls')
    bd = BaseDato()
    print('____CREAR TABLAS_____')
    print()
    print(bd.crearTablas())
    print()
    time.sleep(3)

def eliminarT():
    os.system('cls')
    bd = BaseDato()
    print('____ELIMINAR TABLAS_____')
    print()
    print(bd.eliminarTablas())
    print()
    time.sleep(3)



while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        crearT()
    elif opcion == '2':
        eliminarT()
