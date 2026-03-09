# UMNG IA. Taller de Arboles de búsqueda

Repostorio del taller 1 de la clase de Inteligencia Artificial de la UMNG.

```mermaid
---
title: Imaginatio DB
config: {
  "theme": "base"
}
---
flowchart LR
    A[Libreria de funciones de busqueda de IA]
    B[
        Logica del Juego
        - **Restricciones**: Solo moverse arriba y derecha
        - Dar las opciones en un array, y las funciones IA las converten en nodos
    ]
    C[Array de Ruta con las posiciones finales]
    D1[
        **Logica del pacman**
        Ciclo de animacion y movimiento, que se actualiza cada 5 seg
    ]
    D2[
        **Logica del tablero**
        Mostrar la ruta
    ]
    E[
        **Interfaz gráfica**
        * Controlar la ventana
        * Dibujar elemntos
        * Dibujar la UI y sus botones.
        **Opcion 1:** Reproducir animacion
        **Opcion 2:** Calcular nueva ruta
    ]

    A ---> B
    B ---> C
    C ---> D1
    C ---> D2
    D1 ---> E
    D2 ---> E
```

---

A partir de este punto, la logica de la _IA_ será definida por el problema visto desde esta perspectiva:

> Busqueda de una ruta a través de un plano `(x,y)` donde se conoce el punto de inicio y el punto final

Ante esto se plantea el uso de las siguientes clases:

* Problema `[coordenada_inicial, coordenada_final]`
* Nodo `[posicion, costo, vecinos]`
* Vecinos `[vecino_up, vecino_right, vecino_down, vecino_left]`