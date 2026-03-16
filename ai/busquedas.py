from typing import Callable

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

def _aux_reconstruir_simple(
    ruta_nodos:list[Nodo]
) -> list[tuple[int,int]]:
    """
    Retorna una lista con las coordenadas en orden para la UI

    Args:
        ruta_nodos (list) : listado de Nodos 

    Returns:
        (list) : Tuplas de coordenadas de la ruta a seguir
    """
    return [n.pos for n in ruta_nodos]


def _aux_reconstruir_ruta(
    ruta_nodos:dict[int,Nodo|None],
    meta:Nodo,
) -> list[tuple[int,int]]:
    """
    Retorna una lista con las coordenadas en orden para la UI

    Args:
        ruta_nodos (dict) : diccionario con la ruta de Nodos
        meta (Nodo): Nodo meta

    Returns:
        (list) : Tuplas de coordenadas de la ruta a seguir
    """
    ruta = []
    nodo_actual = meta
    aux_counter = 0

    # Mientras el ID del nodo esté en el diccionario
    while nodo_actual is not None and aux_counter < 200:
        aux_counter += 1
        ruta.append(nodo_actual.pos)
        
        # Buscamos al padre. Si no tiene padre (es el inicio), devolverá None
        # Si el nodo no existe en el diccionario, es que no hay ruta completa
        if nodo_actual.id in ruta_nodos:
            nodo_actual = ruta_nodos[nodo_actual.id]
        else:
            # Si el nodo actual no está en el diccionario y no es el inicio,
            # significa que la ruta está rota.
            break

    return list(reversed(ruta))


def general(
    problema:Problema, 
    tablero:list[list[Nodo]],
    estrategia:Callable[[list[Nodo]],Nodo],
) -> list[tuple[int,int]]:
    """
    Algoritmo de busqueda general, que sigue una estrategia
    para seleccionar la frontera a expandir.

    Args:
        problema (Problema) : El problema de busqueda.
        tablero (list) : tablero de nodos.
        estrategia (Callable) : Funcion de evaluacion

    Returns:
        list[tuple[int,int]] : Ruta a seguir para llegar a la meta.
    """
    aux_counter = 0

    inicio = _aux_get_nodo(problema.inicio, tablero)
    meta = _aux_get_nodo(problema.meta, tablero)
    
    if (inicio.pos == meta.pos):
        return [inicio.pos]
    
    ruta:list[Nodo] = []
    frontera = [inicio]
    isMetaEncontrada = False
    
    while frontera and not isMetaEncontrada and aux_counter < 100:
        aux_counter += 1
        
        nodo_actual = estrategia(frontera)
        frontera.remove(nodo_actual)
        ruta.append(nodo_actual)

        if nodo_actual.pos == meta.pos:
            isMetaEncontrada = True
        
        #expansion
        for vecino in nodo_actual.vecinos:
            frontera.append(vecino)

    return _aux_reconstruir_simple(ruta)

def primero_en_amplitud(
    problema:Problema, 
    tablero:list[list[Nodo]],
    _:Callable[[list[Nodo]],Nodo] 
) -> list[tuple[int,int]]:
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
        
        if nodo_actual.pos == meta.pos:                
            isMetaEncontrada = True
            break

        #expansion
        for vecino in nodo_actual.vecinos:
            if vecino.id not in visitados:
                visitados.append(vecino.id)
                ruta[vecino.id] = nodo_actual           
                frontera.append(vecino)

    return _aux_reconstruir_ruta(ruta, meta)

def profundidad_primero(
    problema:Problema, 
    tablero:list[list[Nodo]],
    f:Callable[[list[Nodo]],Nodo],
) -> list[tuple[int,int]]:
    """
    Algoritmo centrado en obtener un nodo de la frontera
    segun la funcion de evaluacion

    Args:
        problema (Problema) : El problema de busqueda.
        f (Callable) : Funcion de evaluacion
        tablero (list) : tablero de nodos.

    Returns:
        list[tuple[int,int]] : Ruta a seguir para llegar a la meta.

    """
    inicio = _aux_get_nodo(problema.inicio, tablero)
    meta = _aux_get_nodo(problema.meta, tablero)

    if (inicio.pos == meta.pos):
        return [inicio.pos]
    
    alcanzados = []
    ruta:dict[int,Nodo | None] = {inicio.id: None}

    isMetaEncontrada = False

    frontera = [inicio]
    while frontera and not isMetaEncontrada:
        nodo_actual = f(frontera)
        
        if (nodo_actual.pos == meta.pos):
            isMetaEncontrada = True

        #expandir
        # Expandir
        for vecino in nodo_actual.vecinos:
            if vecino and vecino.id not in alcanzados:
                alcanzados.add(vecino.id)
                ruta[vecino.id] = nodo_actual
                frontera.append(vecino)
    
    return _aux_reconstruir_ruta(ruta, meta)
