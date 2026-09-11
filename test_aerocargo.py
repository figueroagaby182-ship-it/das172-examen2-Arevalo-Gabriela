"""
test_aerocargo.py
Suite de pruebas unitarias para validar las funciones del proyecto AeroCargo-Matrix.
"""

import unittest
from aerocargo import (
    validar_matrices,
    calcular_ocupacion_y_sobrecarga,
    evaluar_balance_y_simetria,
    extraer_submatriz_critica,
)


class TestAeroCargoMatrix(unittest.TestCase):

    def setUp(self):
        """Configuración de matrices base para los casos de prueba."""
        # Matriz válida 3x4
        self.cargas_validas = [
            [500, 650, 700, 400],
            [400, 300, 550, 200],
            [100, 0, 300, 450],
        ]
        self.caps_validas = [
            [500, 600, 700, 500],
            [500, 500, 500, 500],
            [500, 500, 500, 500],
        ]

    # -------------------------------------------------------------------------
    # PRUEBAS MÓDULO 1: Validación y Coherencia Dimensional
    # -------------------------------------------------------------------------
    def test_validar_matrices_correcto(self):
        """Verifica que matrices válidas retorno True."""
        self.assertTrue(validar_matrices(self.cargas_validas, self.caps_validas))

    def test_validar_matrices_dimensiones_incompatibles(self):
        """Verifica falla cuando las dimensiones N x M no coinciden."""
        caps_incorrectas = [[500, 500], [500, 500]]
        self.assertFalse(validar_matrices(self.cargas_validas, caps_incorrectas))

    def test_validar_matrices_valores_invalidos(self):
        """Verifica rechazo de cargas negativas o capacidades <= 0."""
        cargas_negativas = [[-100, 200], [200, 200]]
        caps_ceros = [[0, 500], [500, 500]]
        self.assertFalse(validar_matrices(cargas_negativas, self.caps_validas))
        self.assertFalse(validar_matrices(self.cargas_validas, caps_ceros))

    # -------------------------------------------------------------------------
    # PRUEBAS MÓDULO 2: Ocupación y Sobrecarga
    # -------------------------------------------------------------------------
    def test_calcular_ocupacion_y_sobrecarga(self):
        """Verifica el cálculo de porcentajes y la identificación de celdas > 100%."""
        resultado = calcular_ocupacion_y_sobrecarga(self.cargas_validas, self.caps_validas)
        matriz_pct = resultado["matriz_porcentajes"]
        sobrecargas = resultado["sobrecargas"]

        # 650/600 * 100 = 108.33% en (0, 1) y 550/500 * 100 = 110.0% en (1, 2)
        self.assertEqual(matriz_pct[0][0], 100.0)
        self.assertEqual(matriz_pct[0][1], 108.33)
        self.assertIn((0, 1), sobrecargas)
        self.assertIn((1, 2), sobrecargas)

    # -------------------------------------------------------------------------
    # PRUEBAS MÓDULO 3: Balance y Simetría
    # -------------------------------------------------------------------------
    def test_evaluar_balance_par(self):
        """Verifica balance en matriz con número par de columnas (M=4)."""
        resultado = evaluar_balance_y_simetria(self.cargas_validas, tolerancia_desbalance_kg=300.0)
        
        # Pesos longitudinales por fila: [2250, 1450, 850]
        self.assertEqual(resultado["pesos_longitudinales"], [2250, 1450, 850])
        # Babor (cols 0,1): 500+650 + 400+300 + 100+0 = 1950 kg
        # Estribor (cols 2,3): 700+400 + 550+200 + 300+450 = 2600 kg
        # Desbalance: |1950 - 2600| = 650 kg > 300.0 kg => RECHAZADO (False)
        self.assertEqual(resultado["desbalance_kg"], 650.0)
        self.assertFalse(resultado["balanceado"])

    def test_evaluar_balance_impar(self):
        """Verifica la omisión de la columna central si M es impar (M=3)."""
        cargas_impar = [
            [100, 999, 100],
            [200, 888, 200]
        ]
        resultado = evaluar_balance_y_simetria(cargas_impar, tolerancia_desbalance_kg=50.0)
        # Columna 1 (índice 1, valor 999 y 888) se omite.
        # Babor: 100 + 200 = 300. Estribor: 100 + 200 = 300. Desbalance = 0.
        self.assertEqual(resultado["desbalance_kg"], 0.0)
        self.assertTrue(resultado["balanceado"])

    # -------------------------------------------------------------------------
    # PRUEBAS MÓDULO 4: Extracción de Submatriz Crítica
    # -------------------------------------------------------------------------
    def test_extraer_submatriz_critica(self):
        """Verifica la extracción de la ventana k x p con mayor ocupación."""
        matriz_pct = [
            [100.0, 108.33, 100.0, 80.0],
            [80.0, 60.0, 110.0, 40.0],
            [20.0, 0.0, 60.0, 90.0]
        ]
        sub = extraer_submatriz_critica(matriz_pct, k=2, p=2)
        # La ventana 2x2 en superior izquierda (filas 0-1, cols 0-1) promedia mayor carga
        esperado = [
            [100.0, 108.33],
            [80.0, 60.0]
        ]
        self.assertEqual(sub, esperado)


if __name__ == "__main__":
    unittest.main()