"""
from ai.aipacman import AIPacman

class Tablero:
    def __init__(self, tamano=5):
        self.tamano = tamano
        self.inicio = (5, 1)
        self.meta = (1, 5)
        self.ai = AIPacman(tablero=None, tamano=tamano)
    
    def obtener_ruta(self):
        return self.ai.buscar_ruta(self.inicio, self.meta)
"""

from ai.commons import Nodo, Problema

class Tablero:
    """
    Es quien controla la logica del juego
    """

    def __init__(
        self, 
        size:int, 
        inicio:tuple[int,int],
        meta:tuple[int,int],
        ia:function
    ):
        self.ia = ia
        self.size = size
        self.problema = Problema(inicio, meta)
        self.tablero = self._crear_tablero()

    def _crear_tablero(self) -> list[list[Nodo]]:
        """
        Crea la grilla de nodos con sus vecinos asignados.

        Returns:
            list[list[Nodo]]: grilla size x size de nodos conectados.
        """
        # Paso 1: crear todos los nodos sin vecinos aún
        grilla = [
            [
                Nodo(
                    id=(fila * self.size) + col, 
                    pos=(fila, col), 
                    costo=1
                )
                for col 
                in range(self.size)
            ]
            for fila in range(self.size)
        ]

        # Paso 2: asignar vecinos a cada nodo
        for fila in range(self.size):
            for col in range(self.size):
                nodo = grilla[fila][col]
                nodo.vecinos.vecino_up    = grilla[fila-1][col] if fila > 0           else None
                nodo.vecinos.vecino_down  = grilla[fila+1][col] if fila < self.size-1 else None
                nodo.vecinos.vecino_left  = grilla[fila][col-1] if col > 0            else None
                nodo.vecinos.vecino_right = grilla[fila][col+1] if col < self.size-1  else None

        return grilla

    def _get_nodo(self, pos: tuple[int, int]) -> Nodo | None:
        """
        Retorna el nodo en la posición dada.
        
        Args:
            pos (tuple( int, int)) : Posicion del Nodo

        Returns:
            Nodo : Nodo esperado
        """
        fila, col = pos

        if (fila >= len(self.tablero) or col >= len(self.tablero[fila])):
            raise IndexError("Error: Nodo no encontrado")

        return self.tablero[fila][col]
    
    def obtener_ruta(self):
        self.ia(self.problema, self.tablero)