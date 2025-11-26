# Clase que representa el tablero del juego Hundir la Flota
class Tablero:
    def __init__(self, tamano):
        # El tablero será cuadrado: tamaño x tamaño
        self.dimensiones = (tamano, tamano)