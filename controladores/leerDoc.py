import pandas as pd
import numpy as np

def leer_documento(archivo):
    """
    Lee un documento CSV y devuelve un DataFrame de pandas.
    
    Parámetros:
    archivo (str): archivo base como BD.
    
    Retorna:
    pd.DataFrame: DataFrame con los datos del archivo CSV.
    """
    df = pd.read_csv(archivo)
    return df