from aerocargo import validar_matriz, obtener_submatriz, calcular_ocupacion, evaluar_balance_lateral

def main():
    # Matriz de carga de prueba
    matriz_carga = [
        [100, 200, 150],
        [300, 400, 350],
        [250, 150, 100]
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
    balance = evaluar_balance_lateral(matriz_carga)
    print(f"4. Análisis de balance lateral: {balance}")

if __name__ == "__main__":
    main()
