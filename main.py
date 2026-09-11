"""
Script principal de ejecución para AeroCargo-Matrix.
Demuestra la validación de matrices de carga, extracción de submatrices,
cálculo de tasa de ocupación y análisis de balance lateral.
"""

from aerocargo import validar_matriz, obtener_submatriz, calcular_ocupacion, balance_lateral


def ejecutar_demostracion():
    # Matriz de carga de prueba (4 filas x 4 columnas)
    matriz_carga = [
        [150.0, 200.0, 200.0, 150.0],
        [100.0,   0.0,   0.0, 100.0],
        [300.0, 250.0, 250.0, 300.0],
        [  0.0, 180.0, 180.0,   0.0]
    ]

    print("=== MATRIZ DE CARGA AEROCARGO ===")
    for fila in matriz_carga:
        print(fila)
    print("-" * 35)

    # 1. Validar Matriz
    es_valida = validar_matriz(matriz_carga)
    print(f"1. ¿Matriz válida?: {es_valida}")

    # 2. Extraer Submatriz (Zona Central)
    submatriz = obtener_submatriz(matriz_carga, 0, 1, 1, 2)
    print(f"2. Submatriz (Filas 0-1, Cols 1-2): {submatriz}")

    # 3. Calcular Tasa de Ocupación
    porcentaje_ocupado = calcular_ocupacion(matriz_carga)
    print(f"3. Tasa de ocupación: {porcentaje_ocupado}%")

    # 4. Análisis de Balance Lateral
    peso_izq, peso_der, balanceado = balance_lateral(matriz_carga)
    print(f"4. Peso Izquierda: {peso_izq} kg | Peso Derecha: {peso_der} kg")
    print(f"   ¿Balance lateral correcto?: {balanceado}")


if _name_ == "_main_":
    ejecutar_demostracion()