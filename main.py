import numpy as np
import pandas as pd
import os
import sys
import datetime
import time

lista_fecha = []
lista_descripcion = []
lista_piezas = []
lista_precios = []
precios_totales = []
menu = 1

while menu >= 1 and menu < 3:
    print("\n···BIENVENIDO A JOYERIA CISNEROS···")
    print("\n1. Registrar una venta\n2. Consultar ventas de un día específico\n3. Salir")
    menu = int(input("\n¿Qué opción desea elegir?\nOpción: "))

    try:
        if menu == 1:
            print("***REGISTRO DE VENTA***")
            cantidad = int(input("Cantidad de artículos que deseas registrar en la venta: "))
            for articulo in range (cantidad):
                fecha_actual = datetime.date.today()
                lista_fecha.append(fecha_actual)
                descripcion = input("Escriba la descripción del artículo: ")
                lista_descripcion.append(descripcion)
                cant_piezas = int(input("Número de piezas vendidas de este artículo: "))
                lista_piezas.append(cant_piezas)
                precio_venta = float(input("Precio de venta del artículo: $"))
                lista_precios.append(precio_venta)
                precios_totales.append((cant_piezas)*(precio_venta))
                total = sum(precios_totales)
            
            frameVentas = pd.DataFrame(list(zip(lista_fecha, lista_descripcion, lista_piezas, lista_precios)))
            frameVentas.columns = ["Fecha","Descripción","# de Piezas","Precio $"]
            print(frameVentas)
            
            print(f"\nEl total a pagar es: ${total}")

            frameVentas.to_csv ("historial.csv",mode = "a", index=False, header=True)
            print("--EXPORTADO--")
        if menu == 2:
            if not os.path.exists("historial.csv"):
                    print("EL ARCHIVO NO EXISTE, FAVOR DE REGISTRAR UNA VENTA")
            else:
                inventario = pd.read_csv("historial.csv", index_col=0)
                pedirfecha = input("¿Cuál es la fecha que quieres consultar? Formato: Año-Mes-Día: ")
                filtro = inventario.loc[pedirfecha: pedirfecha]
                print(filtro)
    except Exception:   
        print(f"Ocurrió un error {sys.exc_info()[0]}")
