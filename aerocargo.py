"""
aerocargo.py
Módulo de lógica matemática y procesamiento matricial pura para AeroCargo-Matrix.
"""


def validar_matrices(cargas, capacidades):
    if not isinstance(cargas, list) or not isinstance(capacidades, list):
        return False

    n_cargas = len(cargas)
    n_caps = len(capacidades)

    if n_cargas < 2 or n_cargas != n_caps:
        return False

    m_cargas = len(cargas[0]) if n_cargas > 0 and isinstance(cargas[0], list) else 0
    m_caps = len(capacidades[0]) if n_caps > 0 and isinstance(capacidades[0], list) else 0

    if m_cargas < 2 or m_cargas != m_caps:
        return False

    for f in range(n_cargas):
        if not isinstance(cargas[f], list) or not isinstance(capacidades[f], list):
            return False
        if len(cargas[f]) != m_cargas or len(capacidades[f]) != m_caps:
            return False

        for c in range(m_cargas):
            val_carga = cargas[f][c]
            val_cap = capacidades[f][c]

            if not isinstance(val_carga, (int, float)) or val_carga < 0:
                return False
            if not isinstance(val_cap, (int, float)) or val_cap <= 0:
                return False

    return True


def calcular_ocupacion_y_sobrecarga(cargas, capacidades):
    if not validar_matrices(cargas, capacidades):
        return {"matriz_porcentajes": [], "sobrecargas": []}

    matriz_pct = []
    sobrecargas = []

    for f in range(len(cargas)):
        fila_pct = []
        for c in range(len(cargas[0])):
            pct = round((cargas[f][c] / capacidades[f][c]) * 100.0, 2)
            fila_pct.append(pct)
            if pct > 100.0:
                sobrecargas.append((f, c))
        matriz_pct.append(fila_pct)

    return {
        "matriz_porcentajes": matriz_pct,
        "sobrecargas": sobrecargas
    }


def evaluar_balance_y_simetria(cargas, tolerancia_desbalance_kg):
    if not isinstance(cargas, list) or not cargas or not isinstance(cargas[0], list):
        return {"pesos_longitudinales": [], "desbalance_kg": 0.0, "balanceado": False}

    pesos_longitudinales = [sum(fila) for fila in cargas]

    m = len(cargas[0])
    mitad = m // 2

    peso_izquierda = sum(sum(fila[:mitad]) for fila in cargas)

    if m % 2 == 0:
        peso_derecha = sum(sum(fila[mitad:]) for fila in cargas)
    else:
        peso_derecha = sum(sum(fila[mitad + 1:]) for fila in cargas)

    desbalance_kg = abs(peso_izquierda - peso_derecha)
    es_balanceado = desbalance_kg <= tolerancia_desbalance_kg

    return {
        "pesos_longitudinales": pesos_longitudinales,
        "desbalance_kg": desbalance_kg,
        "balanceado": es_balanceado
    }


def extraer_submatriz_critica(matriz_pct, k, p):
    n = len(matriz_pct)
    m = len(matriz_pct[0]) if n > 0 and isinstance(matriz_pct[0], list) else 0

    if k > n or p > m or k <= 0 or p <= 0:
        return []

    max_promedio = -1.0
    mejor_submatriz = []

    for f in range(n - k + 1):
        for c in range(m - p + 1):
            submatriz_actual = [fila[c:c + p] for fila in matriz_pct[f:f + k]]
            suma_total = sum(sum(fila) for fila in submatriz_actual)
            promedio_actual = suma_total / (k * p)

            if promedio_actual > max_promedio:
                max_promedio = promedio_actual
                mejor_submatriz = submatriz_actual

    return mejor_submatriz


if __name__ == "__main__":
    import doctest
    doctest.testmod()