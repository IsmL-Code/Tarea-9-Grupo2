import numpy as np

def ejecutar_problema2():
    print("\n=== Problema 2: Simulación de Fluido 3D ===")
    capas, filas, columnas = 3, 3, 3  # Tamaño fijo

    fluido = []  # Lista de capas
    for k in range(capas):
        capa = []
        print(f"\nCapa {k+1}:")
        for i in range(filas):
            fila = []
            for j in range(columnas):
                presion = float(input(f"Presión en [{k+1},{i+1},{j+1}]: "))
                temp = float(input(f"Temperatura en [{k+1},{i+1},{j+1}]: "))
                vel = float(input(f"Velocidad en [{k+1},{i+1},{j+1}]: "))
                fila.append([presion, temp, vel])
            capa.append(fila)
        fluido.append(capa)

    fluido = np.array(fluido)
    print("\nFluido 3D ingresado:")
    print(fluido)

    # Ejemplo simple de cálculo: promedio de presiones por capa
    for k in range(capas):
        presiones = fluido[k,:,:,0]  # extraemos solo presiones de la capa k
        print(f"\nPromedio de presión en capa {k+1}: {np.mean(presiones)}")

if __name__ == "__main__":
    ejecutar_problema2()
