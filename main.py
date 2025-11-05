import numpy as np
import pandas as pd
from controladores.leerDoc import leer_documento
from controladores.limpiar_consola import limpiar
from dotenv import load_dotenv
import os

load_dotenv()

ruta_archivo = os.getenv("path")
BD = leer_documento(ruta_archivo)

while True:
    limpiar()
    print("Seleccione una opción:")
    print("1. Mostrar las primeras filas del DataFrame")
    print("2. Calcular estadísticas descriptivas")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    match opcion:
        case '1':
            print(BD.head())
            input("Presione Enter para continuar...")
        case '2':
            print(BD.info())
            input("Presione Enter para continuar...")
        case '3':
            print("Saliendo del programa.")
            break
        case _: ("Opción no válida. Por favor, intente de nuevo.")