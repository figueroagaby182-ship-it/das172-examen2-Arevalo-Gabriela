"""
test_aerocargo.py
Suite de pruebas unitarias para validar los 4 módulos de AeroCargo-Matrix.
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
        """Configuración de matrices base para las pruebas."""
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

    # 1. Pruebas Módulo 1: Validación
    def test_validar_matrices_correcto(self):
        self.assertTrue(validar_matrices(self.cargas_validas, self.caps_validas))

    def test_validar_matrices_invalidas(self):
        caps_incorrectas = [[500, 500], [500, 500]]
        self.assertFalse(validar_matrices(self.cargas_validas, caps_incorrectas))

    # 2. Pruebas Módulo 2: Ocupación y Sobrecarga
    def test_calcular_ocupacion_y_sobrecarga(self):
        resultado = calcular_ocupacion_y_sobrecarga(self.cargas_validas, self.caps_validas)
        matriz_pct = resultado["matriz_porcentajes"]
        sobrecargas = resultado["sobrecargas"]

        self.assertEqual(matriz_pct[0][0], 100.0)
        self.assertEqual(matriz_pct[0][1], 108.33)
        self.assertIn((0, 1), sobrecargas)
        self.assertIn((1, 2), sobrecargas)

    # 3. Pruebas Módulo 3: Balance y Simetría
    def test_evaluar_balance_par(self):
        resultado = evaluar_balance_y_simetria(self.cargas_validas, tolerancia_desbalance_kg=300.0)
        self.assertEqual(resultado["pesos_longitudinales"], [2250, 1450, 850])
        self.assertEqual(resultado["desbalance_kg"], 650.0)
        self.assertFalse(resultado["balanceado"])

    def test_evaluar_balance_impar(self):
        cargas_impar = [
            [100, 999, 100],
            [200, 888, 200]
        ]
        resultado = evaluar_balance_y_simetria(cargas_impar, tolerancia_desbalance_kg=50.0)
        self.assertEqual(resultado["desbalance_kg"], 0.0)
        self.assertTrue(resultado["balanceado"])

    # 4. Pruebas Módulo 4: Submatriz Crítica
    def test_extraer_submatriz_critica(self):
        """Verifica la extracción de la ventana k x p con mayor ocupación."""
        matriz_pct = [
            [100.0, 108.33, 100.0, 80.0],
            [80.0, 60.0, 110.0, 40.0],
            [20.0, 0.0, 60.0, 90.0]
        ]
        sub = extraer_submatriz_critica(matriz_pct, k=2, p=2)
        esperado = [
            [108.33, 100.0],
            [60.0, 110.0]
        ]
        self.assertEqual(sub, esperado)


if __name__ == "__main__":
    unittest.main()