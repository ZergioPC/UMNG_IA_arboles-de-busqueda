from ai.commons import Nodo, Vecinos, Problema

def primero_en_amplitud(problema:Problema, tablero:list[Nodo]):
    inicio = problema.inicio
    meta = problema.meta