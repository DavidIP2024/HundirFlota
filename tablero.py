# Clase que representa el tablero del juego Hundir la Flota
class Tablero:
    def __init__(self, tamano):
        # El tablero será cuadrado: tamaño x tamaño
        self.dimensiones = (tamano, tamano)
        # Inicialización de la matriz del tablero
        # Todas las casillas empiezan como "agua" → representado con 0
        filas, columnas = self.dimensiones
        self.casillas = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Metodo que imprime el tablero por consola
    def mostrar_tablero(self):
        for fila in self.casillas:
            print(fila)
