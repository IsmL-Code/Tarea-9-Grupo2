import numpy as np

def ejecutar_problema1():
    print("\n=== Problema 1: Balance de Fuerzas ===")
    filas = int(input("Ingrese el número de filas de la matriz de fuerzas: "))
    columnas = int(input("Ingrese el número de columnas de la matriz de fuerzas: "))

    fuerzas = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Fuerza en posición [{i+1},{j+1}]: "))
            fila.append(valor)
        fuerzas.append(fila)

    fuerzas = np.array(fuerzas)

    print("\nMatriz de fuerzas ingresada:")
    print(fuerzas)

    suma_filas = np.sum(fuerzas, axis=1)
    suma_columnas = np.sum(fuerzas, axis=0)

    print("\nSuma de fuerzas por fila:", suma_filas)
    print("Suma de fuerzas por columna:", suma_columnas)
    print("Fuerza total:", np.sum(fuerzas))

if __name__ == "__main__":
    ejecutar_problema1()
