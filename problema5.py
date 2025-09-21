import numpy as np
import math


def ejecutar_problema5():
    print("\n=== Problema 5: Transformación de Coordenadas en un Sistema Cartesiano ===")

    # Ingreso de la cantidad de puntos
    n_puntos = int(input("Ingrese el número de puntos: "))

    # Ingreso de las coordenadas de cada punto
    puntos = []
    for i in range(n_puntos):
        x = float(input(f"Punto {i+1} - coordenada X: "))
        y = float(input(f"Punto {i+1} - coordenada Y: "))
        puntos.append([x, y])

    puntos = np.array(puntos)
    print("\nPuntos originales:")
    print(puntos)

    # Definir transformación: ejemplo de rotación de 45 grados
    angulo = float(input("Ingrese el ángulo de rotación en grados: "))
    rad = math.radians(angulo)
    matriz_rotacion = np.array([[math.cos(rad), -math.sin(rad)],
                                [math.sin(rad),  math.cos(rad)]])

    # Aplicar transformación
    puntos_transformados = puntos.dot(matriz_rotacion.T)

    print("\nPuntos después de la transformación (rotación):")
    print(np.round(puntos_transformados, 2))  # redondeado para mayor claridad


if __name__ == "__main__":
    ejecutar_problema5()
