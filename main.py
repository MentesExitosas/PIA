import os
from os import system, name
import sys
import datetime
import time
import sqlite3
from sqlite3 import Error

def borrar():
  if name == "nt":
    system("cls")
  else:
    system("clear")

lista_fecha = []
lista_descripcion = []
lista_piezas = []
lista_precios = []
precios_totales = []
menu = 1


try:

    with sqlite3.connect('Ventas.db') as conn:
        conexion = conn.cursor()
        conexion.execute('CREATE TABLE IF NOT EXISTS Venta (ID INTEGER PRIMARY KEY AUTOINCREMENT,Descripcion_art TEXT NOT NULL,Cantidad_elementos INTEGER, Precio_producto FLOAT, Total INTEGER, fecha DATE);')
        print('Se creo la Base de datos')
        while menu != 3:
            print("\n···BIENVENIDO A JOYERIA CISNEROS···")
            print("\n1. Registrar una venta\n2. Consultar ventas de un día específico\n3. Salir")
            menu = int(input("\n¿Qué opción desea elegir?\nOpción: "))
            if menu in range(1,4) and menu > 0:

                if menu == 1:
                    print("···REGISTRO DE VENTA···")
                    cantidad = int(input("Cantidad de artículos que deseas registrar en la venta: "))
                    if cantidad > 0:
                        for articulo in range (cantidad):
                            fecha_actual = datetime.date.today()
                            
                            descripcion = input("Escriba la descripción del artículo: ")
                            if len(descripcion) == 0 or descripcion.isspace():
                                print("\nIngresaste un carácter no válido\nSe repetirá el menú\n")
                                input("Presione enter para continuar...")
                                borrar()
                            else:
                                cant_piezas = int(input(f"Número de piezas vendidas del artículo {descripcion}: "))
                                if cant_piezas > 0:
                                    precio_venta = float(input("Precio de venta del artículo: $"))
                                    if precio_venta > 0:
                                        precios_totales.append((cant_piezas)*(precio_venta))
                                        total = sum(precios_totales)
                                        print(f"\nEl total a pagar es: ${total}")

                                        print(f"Fecha de venta: {fecha_actual}")
                                        print(f"Descripción: {descripcion}")
                                        print(f"La cantidad de piezas es: {cant_piezas}")
                                        print(f"El precio de venta del artículo es: {precio_venta}")
                                        
                                        conexion.execute('SELECT MAX(ID)+1 FROM Venta')
                                        I = conexion.fetchone()
                                        if I[0] == None:
                                            I = 1
                                        else:
                                            I = int(I[0])
                                        insert = (f'INSERT INTO Venta VALUES({I}), {descripcion}, {cant_piezas},{precio_venta}, {total}, {fecha_actual}')
                                        conexion.execute(insert)
                                        input("Presione enter para continuar...")
                                        borrar()
                                    else:
                                        print("\nIngrese un precio de venta que sea válido\nSe repetirá el menú\n")  
                                        input("Presione enter para continuar...")
                                        borrar()

                                else:
                                    print("\nIngrese un número que sea válido\nSe repetirá el menú\n")
                                    input("Presione enter para continuar...")
                                    borrar()
                    else:
                        print("\nIngrese un número que sea válido\nSe repetirá el menú\n")
                        input("Presione enter para continuar...")
                        borrar()
                if menu == 2:
                    if not os.path.exists("historial.csv"):
                        print("EL ARCHIVO NO EXISTE, FAVOR DE REGISTRAR UNA VENTA")
                    else:
                        inventario = pd.read_csv("historial.csv", index_col=0)
                        pedirfecha = input("¿Cuál es la fecha que quieres consultar? Formato: Año-Mes-Día: ")
                        filtro = inventario.loc[pedirfecha: pedirfecha]
                        print(filtro)
            else:
                print("\nIngrese un dígito válido\nSe repetirá el menú\n")
                input("Presione enter para continuar...")
                borrar()
except Error as e:
    print (e)
except:
    print(f"Ocurrió un error {sys.exc_info()[0]}")

    
    
