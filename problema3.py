import numpy as np


def ejecutar_problema3():
    print("\n=== Problema 3: Suavizado de Imágenes Médicas 3D ===")
    capas = int(input("Número de capas (profundidad): "))
    filas = int(input("Número de filas por imagen: "))
    columnas = int(input("Número de columnas por imagen: "))

    volumen = []
    for k in range(capas):
        print(f"\nCapa {k+1}:")
        capa = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Píxel [{k+1},{i+1},{j+1}]: "))
                fila.append(valor)
            capa.append(fila)
        volumen.append(capa)

    volumen = np.array(volumen)
    print("\nVolumen original:")
    print(volumen)

    # Suavizado simple: promedio de vecinos inmediatos
    volumen_suavizado = np.copy(volumen)
    for k in range(capas):
        for i in range(filas):
            for j in range(columnas):
                vecinos = []
                for dk in [0]:
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < filas and 0 <= nj < columnas:
                                vecinos.append(volumen[k, ni, nj])
                volumen_suavizado[k, i, j] = np.mean(vecinos)

    print("\nVolumen suavizado:")
    print(volumen_suavizado)


if __name__ == "__main__":
    ejecutar_problema3()
