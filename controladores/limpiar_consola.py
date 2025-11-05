import os
def limpiar():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    os.system('cls' if os.name == 'nt' else 'clear')