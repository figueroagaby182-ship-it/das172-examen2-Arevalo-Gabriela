"""
Pruebas unitarias para el módulo aerocargo utilizando Pytest.
Cubre casos típicos y casos de borde para cada función.
"""

import pytest
from aerocargo import validar_matriz, obtener_submatriz, calcular_ocupacion, balance_lateral


def test_validar_matriz_valida():
    matriz = [[10, 20], [30, 40]]
    assert validar_matriz(matriz) is True


def test_validar_matriz_invalida_dimensiones():
    matriz = [[10, 20], [30]]  # Filas desiguales
    assert validar_matriz(matriz) is False


def test_validar_matriz_valores_negativos():
    matriz = [[10, -5], [30, 40]]  # Peso negativo invalido
    assert validar_matriz(matriz) is False


def test_obtener_submatriz():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    esperado = [[5, 6], [8, 9]]
    assert obtener_submatriz(matriz, 1, 2, 1, 2) == esperado


def test_calcular_ocupacion():
    matriz = [
        [10, 0],
        [0, 20]
    ]
    # 2 celdas de 4 ocupadas = 50%
    assert calcular_ocupacion(matriz) == 50.0


def test_balance_lateral():
    matriz_balanceada = [
        [100, 100],
        [200, 200]
    ]
    izq, der, balanceado = balance_lateral(matriz_balanceada)
    assert izq == 300.0
    assert der == 300.0
    assert balanceado is True