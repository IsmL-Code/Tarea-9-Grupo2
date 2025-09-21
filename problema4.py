import numpy as np


def ejecutar_problema4():
    print("\n=== Problema 4: Manejo de Datos en una Tabla de Sensores ===")

    # Fijas dimensiones 5x5 según el problema
    filas = 5   # momentos en el tiempo
    columnas = 5  # sensores

    datos_sensores = []

    # Ingreso de datos por el usuario
    for i in range(filas):
        fila = []
        print(f"\nMomento {i+1}:")
        for j in range(columnas):
            valor = float(input(f"  Lectura Sensor {j+1}: "))
            fila.append(valor)
        datos_sensores.append(fila)

    # Convertimos la lista de listas en un array de numpy
    datos_sensores = np.array(datos_sensores)

    # Mostrar la tabla completa
    print("\nTabla de lecturas de sensores (filas = momentos, columnas = sensores):")
    print(datos_sensores)

    # Cálculos
    promedio_fila = np.mean(datos_sensores, axis=1)
    desviacion_fila = np.std(datos_sensores, axis=1)

    promedio_columna = np.mean(datos_sensores, axis=0)
    desviacion_columna = np.std(datos_sensores, axis=0)

    # Mostrar resultados
    print("\n--- Estadísticas por momento (fila) ---")
    for i in range(filas):
        print(
            f"Momento {i+1}: Promedio = {promedio_fila[i]:.2f}, Desviación estándar = {desviacion_fila[i]:.2f}")

    print("\n--- Estadísticas por sensor (columna) ---")
    for j in range(columnas):
        print(
            f"Sensor {j+1}: Promedio = {promedio_columna[j]:.2f}, Desviación estándar = {desviacion_columna[j]:.2f}")


if __name__ == "__main__":
    ejecutar_problema4()
