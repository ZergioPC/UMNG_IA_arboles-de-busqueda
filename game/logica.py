from typing import Callable

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
        ia:Callable[[Problema, list[list[Nodo]]],list[tuple[int,int]]]
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

        # Paso 2: asignar vecinos [arriba, derecha, abajo, izquierda]
        for fila in range(self.size):
            for col in range(self.size):
                nodo = grilla[fila][col]
                if (fila > 0): nodo.vecinos.append(grilla[fila-1][col]) # arriba
                if (col < self.size-1 ): nodo.vecinos.append(grilla[fila][col+1]) # derecha
                if (fila < self.size-1): nodo.vecinos.append(grilla[fila+1][col]) # abajo
                if (col > 0): nodo.vecinos.append(grilla[fila][col-1]) # izquierda


        return grilla
    
    def obtener_ruta(self) -> list[tuple[int,int]]:
        return self.ia(self.problema, self.tablero)