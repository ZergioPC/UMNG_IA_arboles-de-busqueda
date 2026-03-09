from ai.commons import Nodo, Problema

def _aux_get_nodo(pos: tuple[int, int],  tablero:list[list[Nodo]]) -> Nodo:
    """
    Retorna el nodo en la posición dada.
    
    Args:
        pos (tuple( int, int)) : Posicion del Nodo

    Returns:
        Nodo : Nodo esperado
    """
    fila, col = pos

    if (fila >= len(tablero) or col >= len(tablero[fila])):
        raise IndexError("Nodo no encontrado")

    return tablero[fila][col]

def _aux_reconstruir_ruta(ruta_nodos:dict[int,Nodo|None], meta):
    """
    Retorna una lista con las coordenadas en orden para la UI

    Args:
        ruta_nodos (dict) : diccionario con la ruta de Nodos
        meta (Nodo): Nodo meta
    """
    ruta = []
    nodo = meta
    while nodo is not None:
        ruta.append(nodo.pos)
        nodo = ruta_nodos[nodo.id]
    return list(reversed(ruta))

def _expandir(visitados:list[int], nodo:Nodo) -> list[Nodo]:
    """
    Expaned la frontera de un nodo y valida que no estén visitados

    Args:
        visitados (list[int]) : Lista de Ids de los nodos visitados
        nodo (Nodo) : Nodo a expandir
    
    Returns:
        list[Nodo] : Vecinos del nodo
    """

    hijos:list[Nodo] = []
    for vecino in nodo.vecinos:
        if vecino and vecino.id not in visitados:
            hijos.append(vecino)
    
    return hijos

def primero_en_amplitud(problema:Problema, tablero:list[list[Nodo]]) -> list[tuple[int,int]]:
    """
    Algoritmo de busqueda que utiliza la estructura de datos FIFO (First In
    First Out) para seleccionar la frontera a expandir.

    Args:
        problema (Problema) : El problema de busqueda.
        tablero (list) : tablero de nodos.

    Returns:
        list[tuple[int,int]] : Ruta a seguir para llegar a la meta.
    """
    inicio = _aux_get_nodo(problema.inicio, tablero)
    meta = _aux_get_nodo(problema.meta, tablero)
    
    if (inicio.pos == meta.pos):
        return [inicio.pos]
    
    visitados = [inicio.id]
    ruta:dict[int,Nodo | None] = {inicio.id: None}
    
    isMetaEncontrada = False

    frontera = [inicio]
    while frontera and not isMetaEncontrada:
        nodo_actual = frontera.pop(0)
        
        for hijo in _expandir(visitados, nodo_actual):
            visitados.append(hijo.id)
            ruta[hijo.id] = nodo_actual

            if hijo.pos == meta.pos:
                
                isMetaEncontrada = True
            
            frontera.append(hijo)
    return _aux_reconstruir_ruta(ruta, meta)