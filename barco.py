# Clase que representa un barco del juego Hundir la Flota
class Barco:
    def __init__(self, nombre, longitud):
        # Nombre del barco (ej: "Submarino", "Buque")
        self.nombre = nombre

        # Longitud del barco (cuántas casillas ocupa)
        self.longitud = longitud

        # Golpes recibidos por el barco (empieza en 0)
        self.golpes_recibidos = 0

        # Metodo que registra un impacto en el barco
    def recibir_impacto(self):
        self.golpes_recibidos += 1