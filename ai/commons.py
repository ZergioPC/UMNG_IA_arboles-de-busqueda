class Problema:
    """
    Clase que define el problema  de busqueda, en este caso, el 
    punto inicial y la meta.

    Attributes:
        inicio (tuple( int, int )): coordenada de inicio.
        meta (tuple( int, int )): coordenada de la Meta.
    """

    def __init__(self, inicio:tuple[int,int], meta:tuple[int,int]):
        """
        Inicializar la clase Problema.

        Args:
            inicio (tuple( int, int )): coordenada de inicio.
            meta (tuple( int, int )): coordenada de la Meta.
        """
        self.inicio = inicio
        self.meta = meta

class Vecinos:
    """
    Clase que controla los vecinos de la clase Nodo

    Attributes:
        vecino_up (Nodo | None): vecino de arriba.
        vecino_right (Nodo | None): vecino de derecha.
        vecino_down (Nodo | None): vecino de abajo.
        vecino_left (Nodo | None): vecino de izquierda.
    """

    def __init__(
        self,
        vecino_up: "Nodo" | None,
        vecino_right: "Nodo" | None, 
        vecino_down: "Nodo" | None,
        vecino_left: "Nodo" | None
    ):
        """
        Inicializa la clase Vecinos

        Args:
            vecino_up (Nodo | None): vecino de arriba.
            vecino_right (Nodo | None): vecino de derecha.
            vecino_down (Nodo | None): vecino de abajo.
            vecino_left (Nodo | None): vecino de izquierda.
        """
        self.vecino_up = vecino_up
        self.vecino_right = vecino_right
        self.vecino_down = vecino_down
        self.vecino_left = vecino_left

class Nodo:
    """
    Clase que representa los nodos del arbol de búsqueda

    Attributes:
        id (int): identificador
        pos (tuple( int, int )): coordenada en el tablero.
        costo (float): costo de uso.
        vecinos (Vecinos): listado de los vecinos del nodo
    """

    def __init__(
        self,
        id: int,
        pos: tuple[int, int],
        costo: float,
        vecino_up: "Nodo" | None = None,
        vecino_right: "Nodo" | None = None,
        vecino_down: "Nodo" | None = None,
        vecino_left: "Nodo" | None = None,
    ):
        """Inicializa la clase Nodo.

        Args:
            id (int): identificador
            pos (tuple( int, int )): coordenada en el tablero.
            costo (float): costo de uso.
            vecino_up (Nodo | None): vecino de arriba.
            vecino_right (Nodo | None): vecino de derecha.
            vecino_down (Nodo | None): vecino de abajo.
            vecino_left (Nodo | None): vecino de izquierda.
        """
        self.id = id
        self.pos = pos
        self.costo = costo
        self.vecinos = Vecinos(
            vecino_up,
            vecino_right,
            vecino_down,
            vecino_left
        )