def validar_matriz(matriz):
    """
    >>> validar_matriz([[10, 20], [30, 40]])
    True
    >>> validar_matriz([])
    False
    """
    if not matriz or not isinstance(matriz, list):
        return False
    
    num_columnas = len(matriz[0])
    if num_columnas == 0:
        return False

    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != num_columnas:
            return False
            
    return True

def obtener_submatriz(matriz, fila_inicio, fila_fin, col_inicio, col_fin):
    """
    >>> obtener_submatriz([[1, 2], [3, 4]], 0, 0, 0, 1)
    [[1, 2]]
    """
    submatriz = []
    for r in range(fila_inicio, fila_fin + 1):
        fila_sub = []
        for c in range(col_inicio, col_fin + 1):
            fila_sub.append(matriz[r][c])
        submatriz.append(fila_sub)
    return submatriz

def calcular_ocupacion(matriz):
    """
    >>> calcular_ocupacion([[10, 0], [20, 0]])
    50.0
    """
    if not validar_matriz(matriz):
        return 0.0

    total_celdas = len(matriz) * len(matriz[0])
    celdas_ocupadas = 0

    for fila in matriz:
        for peso in fila:
            if peso > 0:
                celdas_ocupadas += 1

    porcentaje = (celdas_ocupadas / total_celdas) * 100
    return round(porcentaje, 2)

def evaluar_balance_lateral(matriz):
    if not validar_matriz(matriz):
        return "Matriz inválida"

    peso_izquierdo = 0
    peso_derecho = 0
    num_cols = len(matriz[0])
    mitad = num_cols // 2

    for fila in matriz:
        for c in range(mitad):
            peso_izquierdo += fila[c]
        
        inicio_derecha = mitad if num_cols % 2 == 0 else mitad + 1
        for c in range(inicio_derecha, num_cols):
            peso_derecho += fila[c]

    diferencia = abs(peso_izquierdo - peso_derecho)
    
    if diferencia == 0:
        return f"Perfectamente balanceado (Izq: {peso_izquierdo}kg, Der: {peso_derecho}kg)"
    elif peso_izquierdo > peso_derecho:
        return f"Inclinado a la izquierda por {diferencia}kg (Izq: {peso_izquierdo}kg, Der: {peso_derecho}kg)"
    else:
        return f"Inclinado a la derecha por {diferencia}kg (Izq: {peso_izquierdo}kg, Der: {peso_derecho}kg)"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)