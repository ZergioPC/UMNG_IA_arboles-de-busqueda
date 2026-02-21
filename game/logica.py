from ai.aipacman import AIPacman

class Tablero:
    def __init__(self, tamano=5):
        self.tamano = tamano
        self.inicio = (5, 1)
        self.meta = (1, 5)
        self.ai = AIPacman(tablero=None, tamano=tamano)
    
    def obtener_ruta(self):
        return self.ai.buscar_ruta(self.inicio, self.meta)
