"""
main.py
Módulo de ejecución y demostración para el reto evaluativo AeroCargo-Matrix.
"""

from aerocargo import (
    validar_matrices,
    calcular_ocupacion_y_sobrecarga,
    evaluar_balance_y_simetria,
    extraer_submatriz_critica,
)


def ejecutar_demostracion():
    # -------------------------------------------------------------------------
    # DATOS DE ENTRADA DE PRUEBA (Discretización N = 3 filas, M = 4 columnas)
    # -------------------------------------------------------------------------
    # Matriz de Cargas Reales [kg] (Presenta sobrecargas intencionales)
    cargas_reales = [
        [500, 650, 700, 400],
        [400, 300, 550, 200],
        [100, 0, 300, 450],
    ]

    # Matriz de Capacidades Máximas [kg]
    capacidades_maximas = [
        [500, 600, 700, 500],
        [500, 500, 500, 500],
        [500, 500, 500, 500],
    ]

    # Umbral de tolerancia de desbalance lateral en kilogramos
    tolerancia_desbalance_kg = 300.0

    print("=" * 60)
    print("   RETO EVALUATIVO: AUDITORÍA AEROCARGO-MATRIX v2.0")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # 1. MÓDULO DE VALIDACIÓN Y COHERENCIA DIMENSIONAL
    # -------------------------------------------------------------------------
    es_valida = validar_matrices(cargas_reales, capacidades_maximas)
    print(f"\n1. Validación y Coherencia Dimensional: {es_valida}")

    if not es_valida:
        print("   [ERROR] Las matrices ingresadas no cumplen los criterios N x M.")
        return

    # -------------------------------------------------------------------------
    # 2. MÓDULO DE CÁLCULO DE OCUPACIÓN Y DETECCIÓN DE SOBRECARGA
    # -------------------------------------------------------------------------
    res_ocupacion = calcular_ocupacion_y_sobrecarga(
        cargas_reales, capacidades_maximas
    )
    print("\n2. Matriz de Porcentajes de Ocupación (%):")
    for fila in res_ocupacion["matriz_porcentajes"]:
        print(f"   {fila}")

    coordenadas_sobrecarga = res_ocupacion["sobrecargas"]
    print(
        f"   Coordenadas de Celdas Sobrecargadas (>100%): {coordenadas_sobrecarga}"
    )

    # -------------------------------------------------------------------------
    # 3. MÓDULO DE EVALUACIÓN DE BALANCE Y SIMETRÍA
    # -------------------------------------------------------------------------
    res_balance = evaluar_balance_y_simetria(
        cargas_reales, tolerancia_desbalance_kg
    )
    print("\n3. Evaluación de Balance y Simetría:")
    print(
        f"   - Vector de Pesos Longitudinales (Filas): {res_balance['pesos_longitudinales']} kg"
    )
    print(
        f"   - Desbalance Lateral Calculado: {res_balance['desbalance_kg']} kg"
    )
    print(f"   - Tolerancia Máxima Permitida: {tolerancia_desbalance_kg} kg")
    estado_str = (
        "APROBADO" if res_balance["balanceado"] else "RECHAZADO (Desbalance Excesivo)"
    )
    print(f"   - Estado de Balance: {estado_str}")

    # -------------------------------------------------------------------------
    # 4. MÓDULO DE EXTRACCIÓN DE SUBMATRIZ DE SOBRECARGA CRÍTICA (k=2, p=2)
    # -------------------------------------------------------------------------
    k, p = 2, 2
    sub_critica = extraer_submatriz_critica(
        res_ocupacion["matriz_porcentajes"], k, p
    )
    print(f"\n4. Submatriz Crítica Ventana ({k}x{p}) de Mayor Ocupación:")
    for fila in sub_critica:
        print(f"   {fila}")

    print("=" * 60)


if __name__ == "__main__":
    ejecutar_demostracion()