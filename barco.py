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

        # Metodo que comprueba si el barco está hundido
    def esta_hundido(self):
        return self.golpes_recibidos == self.longitud

# Bloque de pruebas de la clase Barco
if __name__ == "__main__":
    # Crear un submarino (longitud 1)
    submarino = Barco("Submarino", 1)
    submarino.recibir_impacto()
    print("Submarino hundido:", submarino.esta_hundido())

    # Crear un buque (longitud 3)
    buque = Barco("Buque", 3)
    buque.recibir_impacto()
    buque.recibir_impacto()
    print("Buque hundido (2 impactos):", buque.esta_hundido())

    buque.recibir_impacto()
    print("Buque hunido (3 impactos):", buque.esta_hundido())

#Comentario final