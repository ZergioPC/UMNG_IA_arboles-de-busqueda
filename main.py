import tkinter as tk

from ui.ventana import Ventana
from game.logica import Tablero
from ai.busquedas import primero_en_amplitud

if __name__ == "__main__":
    tablero = Tablero(5, (0,0), (4,4))
    root = tk.Tk()
    app = Ventana(root, tablero)
    root.mainloop()
