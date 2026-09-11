import unittest
from aerocargo import validar_matriz, obtener_submatriz, calcular_ocupacion, evaluar_balance_lateral

class TestAeroCargo(unittest.TestCase):

    def test_validar_matriz(self):
        matriz_ok = [[100, 200], [300, 400]]
        self.assertTrue(validar_matriz(matriz_ok))
        self.assertFalse(validar_matriz([]))

    def test_obtener_submatriz(self):
        matriz = [[100, 200], [300, 400]]
        sub = obtener_submatriz(matriz, 0, 0, 0, 1)
        self.assertEqual(sub, [[100, 200]])

    def test_calcular_ocupacion(self):
        matriz = [[100, 0], [200, 0]]
        self.assertEqual(calcular_ocupacion(matriz), 50.0)

    def test_evaluar_balance_lateral(self):
        matriz = [[100, 100], [200, 200]]
        resultado = evaluar_balance_lateral(matriz)
        self.assertIn("Perfectamente balanceado", resultado)

if __name__ == "__main__":
    unittest.main()