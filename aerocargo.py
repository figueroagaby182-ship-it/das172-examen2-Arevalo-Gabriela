"""
Módulo AeroCargo: Funciones para validación, extracción de submatrices,
cálculo de ocupación y balance lateral de carga en aeronaves.
"""

def validar_matriz(matriz):
    """
    Verifica que la matriz sea rectangular (todas las filas del mismo tamaño)
    y que todos sus elementos sean números no negativos (>= 0).
    """
    if not matriz or not isinstance(matriz, list):
        return False
    
    if not isinstance(matriz[0], list) or len(matriz[0]) == 0:
        return False
        
    columnas = len(matriz[0])
    
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != columnas:
            return False
        for elemento in fila:
            if not isinstance(elemento, (int, float)) or elemento < 0:
                return False
                
    return True


def obtener_submatriz(matriz, fila_inicio, fila_fin, col_inicio, col_fin):
    """
    Extrae y devuelve una submatriz delimitada por las filas y columnas indicadas.
    """
    if not validar_matriz(matriz):
        return []
        
    num_filas = len(matriz)
    num_cols = len(matriz[0])
    
    if (fila_inicio < 0 or fila_fin >= num_filas or fila_inicio > fila_fin or
        col_inicio < 0 or col_fin >= num_cols or col_inicio > col_fin):
        return []
        
    submatriz = []
    for f in range(fila_inicio, fila_fin + 1):
        submatriz.append(matriz[f][col_inicio:col_fin + 1])
        
    return submatriz


def calcular_ocupacion(matriz):
    """
    Calcula el porcentaje de celdas ocupadas (peso > 0) respecto al total de celdas.
    """
    if not validar_matriz(matriz):
        return 0.0
        
    total_celdas = len(matriz) * len(matriz[0])
    if total_celdas == 0:
        return 0.0
        
    celdas_ocupadas = sum(1 for fila in matriz for elemento in fila if elemento > 0)
    
    return round((celdas_ocupadas / total_celdas) * 100, 2)


def balance_lateral(matriz):
    """
    Calcula el peso total de la mitad izquierda vs mitad derecha.
    Devuelve una tupla (peso_izq, peso_der, esta_balanceado).
    """
    if not validar_matriz(matriz):
        return (0.0, 0.0, False)
        
    num_cols = len(matriz[0])
    mitad = num_cols // 2
    
    peso_izq = 0.0
    peso_der = 0.0
    
    for fila in matriz:
        peso_izq += sum(fila[:mitad])
        # Si el número de columnas es impar, la columna central se omite o se reparte equitativamente
        if num_cols % 2 == 0:
            peso_der += sum(fila[mitad:])
        else:
            peso_der += sum(fila[mitad + 1:])
            
    esta_balanceado = abs(peso_izq - peso_der) < 1e-5
    
    return (round(peso_izq, 2), round(peso_der, 2), esta_balanceado)