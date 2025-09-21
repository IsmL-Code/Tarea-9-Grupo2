# Proyecto: Aplicaciones Numéricas con Arreglos y Simulaciones

Este proyecto contiene una serie de problemas resueltos utilizando **Python** y **NumPy**, enfocándose en la manipulación de arreglos multidimensionales, simulaciones físicas, procesamiento de imágenes y análisis de datos.

---

## Contenido del Proyecto

El proyecto incluye los siguientes problemas:

### Problema 1: Análisis de Fuerzas en una Estructura
- **Descripción:** Se modela una estructura 3x3 con fuerzas aplicadas en cada nodo usando una matriz bidimensional. Se calculan las reacciones en los nodos sumando las fuerzas por fila y columna.
- **Enfoque:** Uso de matrices (`numpy.array`) y operaciones de suma por eje (`np.sum`) para calcular fuerzas totales y parciales.
- **Impacto en eficiencia:** Al utilizar operaciones vectorizadas de NumPy, se evita recorrer la matriz manualmente con bucles anidados, mejorando la eficiencia de cálculo en estructuras grandes.

---

### Problema 2: Simulación de Fluido en una Cuadrícula 3D
- **Descripción:** Representación tridimensional de un fluido con propiedades como presión, temperatura y velocidad. Se realiza un cálculo simple de promedio de presión por capa.
- **Enfoque:** Uso de matrices tridimensionales (`numpy.array`) para almacenar las propiedades del fluido y acceso mediante índices multidimensionales.
- **Impacto en eficiencia:** Las operaciones sobre arreglos 3D permiten realizar cálculos sobre subconjuntos de datos sin necesidad de estructuras de control complejas, optimizando la simulación.

---

### Problema 3: Análisis de Imágenes Médicas en 3D
- **Descripción:** Suavizado de un volumen tridimensional de imágenes médicas mediante un filtro de promedio para reducir ruido.
- **Enfoque:** Uso de un arreglo 3D para representar el volumen de imágenes y un algoritmo de promedio de vecinos inmediatos.
- **Impacto en eficiencia:** La vectorización parcial y el uso de copias de matrices permite actualizar el volumen suavizado sin modificar los datos originales, manteniendo la integridad de los datos y mejorando el rendimiento de las operaciones de filtrado.

---

### Problema 4: Manejo de Datos en una Tabla de Sensores
- **Descripción:** Gestión de datos de sensores de temperatura en una tabla 5x5. Se calcula promedio y desviación estándar por fila y columna.
- **Enfoque:** Uso de matrices bidimensionales y funciones estadísticas de NumPy (`np.mean`, `np.std`) para análisis rápido.
- **Impacto en eficiencia:** El uso de funciones estadísticas optimizadas evita el procesamiento manual, permitiendo un análisis eficiente de grandes cantidades de datos sensoriales.

---

### Problema 5: Transformación de Coordenadas en un Sistema Cartesiano
- **Descripción:** Transformación lineal (rotación) de un conjunto de puntos en un sistema cartesiano utilizando matrices de transformación.
- **Enfoque:** Representación de los puntos como una matriz 2D y uso de multiplicación de matrices (`dot`) para aplicar transformaciones.
- **Impacto en eficiencia:** La multiplicación matricial permite aplicar la transformación a todos los puntos de forma simultánea, evitando bucles innecesarios y mejorando la eficiencia computacional.

---

## Tecnologías Utilizadas
- **Python 3.x**
- **NumPy:** Para manejo de arreglos multidimensionales y operaciones vectorizadas.
- **Math:** Para cálculos matemáticos como conversión de ángulos y funciones trigonométricas.

---

## Conclusión
El enfoque central de este proyecto es el uso de **arreglos multidimensionales y operaciones vectorizadas** para optimizar cálculos y simulaciones. Este enfoque:
- Reduce el número de bucles explícitos y la complejidad del código.
- Permite realizar operaciones en grandes volúmenes de datos de manera eficiente.
- Facilita la extensión de los problemas a dimensiones mayores sin impacto significativo en el rendimiento.

---

## Instrucciones de Ejecución
1. Asegúrate de tener instalado la librería **NumPy**.
2. Ejecuta cada problema de manera independiente mediante:
```bash
