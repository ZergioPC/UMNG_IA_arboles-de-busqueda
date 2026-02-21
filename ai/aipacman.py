from collections import deque

class AIPacman:
    def __init__(self, tablero, tamano=5):
        self.tablero = tablero
        self.tamano = tamano

    def buscar_ruta(self, inicio, meta): #ESTO ES MI BUSQUEDA DE ARBOL
        # Implementación de cola
        cola = deque([(inicio, [], 0, None, "inicio")]) # (nodo, camino, costo, padre, accion)
        visitados = set() #Aqui implemento el array que mencionabamos
        paso = 0
        
        print(f"\n{'='*80}")
        print(f"{'TABLA DE EXPANSIÓN (IA)':^80}")
        print(f"{'='*80}")
        print(f"{'Paso':<5} | {'Nodo':<8} | {'Padre':<8} | {'Acción':<10} | {'Costo':<5} | {'Frontera'}")
        print("-" * 80)

        while cola:
            # Mostrar la frontera antes de extraer
            frontera_visual = [n[0] for n in cola]
            
            nodo_actual, camino, costo, padre, accion = cola.popleft()

            if nodo_actual in visitados:
                continue

            # Imprimir fila de la tabla
            print(f"{paso:<5} | {str(nodo_actual):<8} | {str(padre):<8} | {accion:<10} | {costo:<5} | {frontera_visual}")

            if nodo_actual == meta:
                print(f"\n¡META ENCONTRADA! Pasos totales: {paso}")
                return camino + [nodo_actual]

            visitados.add(nodo_actual) #Añadir a la lista de restricciones
            paso += 1

            for vecino, n_accion in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados: #Solo añade lo que no se ha visitado
                    cola.append((vecino, camino + [nodo_actual], costo + 1, nodo_actual, n_accion))
        
        return []
    
    def obtener_vecinos(self, pos): #ESTO ES MI EXPANDIR
        f, c = pos
        # Movimientos permitidos: arriba, abajo, derecha, izquierda
        posibles = {
            "arriba": (f - 1, c),
            "abajo": (f + 1, c),
            "derecha": (f, c + 1),
            "izquierda": (f, c - 1)
        }
        
        validos = []
        for accion, n_pos in posibles.items():
            if self.es_valido(n_pos):
                validos.append((n_pos, accion))
        return validos
    
    def es_valido(self, pos):
        # Verifica que la posición esté dentro de los límites 1-5
        f, c = pos
        return 1 <= f <= self.tamano and 1 <= c <= self.tamano