import tkinter as tk

from ai.commons import Nodo
from game.logica import Tablero

class Ventana:
    def __init__(self, root, tablero:Tablero):
        self.root = root
        self.root.title("Busqueda de Arboles - Pacman IA")
        
        self.tablero = tablero
        self.tamano_tablero = tablero.size
        self.tamano_celda = 80
        self.tablero_ancho = self.tamano_celda * self.tamano_tablero
        self.tablero_alto = self.tamano_celda * self.tamano_tablero
        
        self.canvas = tk.Canvas(
            root, 
            width=self.tablero_ancho, 
            height=self.tablero_alto,
            bg="white"
        )
        self.canvas.pack(pady=10)
        
        self.btn_calcular_general = tk.Button(
            root, 
            text="Algoritmo General", 
            font=("Arial", 12),
            command=self.calcular_general
        )
        self.btn_calcular_general.pack(pady=10)

        self.btn_calcular_bfs = tk.Button(
            root, 
            text="Algoritmo BFS", 
            font=("Arial", 12),
            command=self.calcular_primero_amplitud
        )
        self.btn_calcular_bfs.pack(pady=10)

        self.btn_calcular_dfs = tk.Button(
            root, 
            text="Algoritmo DFS", 
            font=("Arial", 12),
            command=self.calcular_profundidad_primero
        )
        self.btn_calcular_dfs.pack(pady=10)
        
        self.ruta = []
        self.paso_actual = 0
        self.pacman_id = None
        
        self.dibujar_tablero()
    
    def dibujar_tablero(self):
        self.canvas.delete("all")
        for fila in range(self.tamano_tablero):
            for col in range(self.tamano_tablero):
                x1 = col * self.tamano_celda
                y1 = fila * self.tamano_celda
                x2 = x1 + self.tamano_celda
                y2 = y1 + self.tamano_celda
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="blue",
                    outline="black",
                    width=2
                )
    
    def dibujar_ruta(self):
        for pos in self.ruta:
            x = (pos[1]) * self.tamano_celda + self.tamano_celda // 2
            y = (self.tamano_tablero - 1 - pos[0]) * self.tamano_celda + self.tamano_celda // 2
            # Y es de esta forma porque en computacion grafica +Y es hacia abajo
            
            self.canvas.create_oval(
                x - 10, y - 10, x + 10, y + 10,
                fill="white",
                outline="white"
            )
    
    def dibujar_pacman(self, pos):
        if self.pacman_id:
            self.canvas.delete(self.pacman_id)
        
        x = (pos[1]) * self.tamano_celda + self.tamano_celda // 2
        y = (self.tamano_tablero - 1 - pos[0]) * self.tamano_celda + self.tamano_celda // 2
        # Y es de esta forma porque en computacion grafica +Y es hacia abajo
        
        self.pacman_id = self.canvas.create_oval(
            x - 25, y - 25, x + 25, y + 25,
            fill="yellow",
            outline="black"
        )

    # Calcular ruta segun algoritms
    
    def calcular_general(self):
        import random
        from ai.busquedas import general
        
        # Estrategia Hardcodeada :v
        def estrategia(frontera:list[Nodo])-> Nodo:
            return random.choice(frontera[-2:])

        print("Buscando ruta...")
        ruta = self.tablero.obtener_ruta(general, estrategia)
        self.ruta = ruta
        self.animar()

    def calcular_primero_amplitud(self):
        from ai.busquedas import primero_en_amplitud
        print("Buscando ruta...")
        ruta = self.tablero.obtener_ruta(primero_en_amplitud)
        self.ruta = ruta
        self.animar()

    def calcular_profundidad_primero(self):
        from ai.busquedas import profundidad_primero
        print("Buscando ruta...")
        ruta = self.tablero.obtener_ruta(profundidad_primero)
        self.ruta = ruta
        self.animar()

    # Animaciones

    def animar(self):        
        if self.ruta:
            print(f"Ruta encontrada: {self.ruta}")
            self.paso_actual = 0
            self.dibujar_tablero()
            self.dibujar_ruta()
            self.animar_pacman()
        else:
            print("No se encontró ruta antes de los 100 pasos")
    
    def animar_pacman(self):
        if self.paso_actual < len(self.ruta):
            pos = self.ruta[self.paso_actual]
            self.dibujar_pacman(pos)
            self.paso_actual += 1
            self.root.after(500, self.animar_pacman)
