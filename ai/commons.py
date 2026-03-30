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

class Nodo:
    """
    Clase que representa los nodos del arbol de búsqueda

    Attributes:
        id (int): identificador
        pos (tuple( int, int )): coordenada en el tablero.
        costo (float): costo de uso.
        vecinos (list(Nodo)): listado de los vecinos del nodo.
    """

    def __init__(
        self,
        id: int,
        pos: tuple[int, int],
        costo: float,
        vecinos:list["Nodo"] | None = None
    ):
        """Inicializa la clase Nodo.

        Args:
            id (int): identificador
            pos (tuple( int, int )): coordenada en el tablero.
            costo (float): costo de uso.
            vecinos (list(Nodo)): listado de los vecinos del nodo.
        """
        self.id = id
        self.pos = pos
        self.costo = costo
        self.vecinos = vecinos if vecinos is not None else []

    def __str__(self) -> str:
        return f"Nodo {self.id}. Pos{self.pos}. Vecinos:{[veci.id for veci in self.vecinos]}"