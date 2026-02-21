import tkinter as tk

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Busqueda de Arboles - Pacman IA")
        
        self.tamano_celda = 80
        self.tamano_tablero = 5
        self.tablero_ancho = self.tamano_celda * self.tamano_tablero
        self.tablero_alto = self.tamano_celda * self.tamano_tablero
        
        self.canvas = tk.Canvas(
            root, 
            width=self.tablero_ancho, 
            height=self.tablero_alto,
            bg="white"
        )
        self.canvas.pack(pady=10)
        
        self.btn_calcular = tk.Button(
            root, 
            text="Calcular Ruta", 
            font=("Arial", 12),
            command=self.calcular_y_animar
        )
        self.btn_calcular.pack(pady=10)
        
        self.ruta = []
        self.paso_actual = 0
        self.pacman_id = None
        
        self.dibujar_tablero()
    
    def dibujar_tablero(self):
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
    
    def dibujar_ruta(self, ruta):
        for pos in ruta:
            x = (pos[1] - 1) * self.tamano_celda + self.tamano_celda // 2
            y = (pos[0] - 1) * self.tamano_celda + self.tamano_celda // 2
            
            self.canvas.create_oval(
                x - 10, y - 10, x + 10, y + 10,
                fill="white",
                outline="white"
            )
    
    def dibujar_pacman(self, pos):
        if self.pacman_id:
            self.canvas.delete(self.pacman_id)
        
        x = (pos[1] - 1) * self.tamano_celda + self.tamano_celda // 2
        y = (pos[0] - 1) * self.tamano_celda + self.tamano_celda // 2
        
        self.pacman_id = self.canvas.create_oval(
            x - 25, y - 25, x + 25, y + 25,
            fill="yellow",
            outline="black"
        )
    
    def calcular_y_animar(self):
        from game.logica import Tablero
        
        tablero = Tablero(tamano=5)
        print("Buscando ruta...")
        ruta = tablero.obtener_ruta()
        
        if ruta:
            print(f"Ruta encontrada: {ruta}")
            self.ruta = ruta
            self.paso_actual = 0
            self.dibujar_ruta(ruta)
            self.animar_pacman()
        else:
            print("No se encontró ruta")
    
    def animar_pacman(self):
        if self.paso_actual < len(self.ruta):
            pos = self.ruta[self.paso_actual]
            self.dibujar_pacman(pos)
            self.paso_actual += 1
            self.root.after(500, self.animar_pacman)
