 # AeroCargo-Matrix 

Sistema en Python para la validación de matrices de carga, cálculo de tasas de ocupación y análisis de balance lateral para aeronaves de carga.

---

##  Explicación del Problema

En la industria aeronáutica, el control de *balance de masa* y la *capacidad de piso* son fundamentales para la seguridad operacional y la eficiencia del vuelo:

* *Balance de Masa y Centro de Gravedad (CG):* Una distribución asimétrica del peso altera el centro de gravedad de la aeronave. Un desequilibrio lateral obliga a aplicar correcciones continuas de compensación (trim) en vuelo, lo que incrementa el arrastre aerodinámico y el consumo de combustible. En casos extremos, superar los límites de balance lateral compromete la maniobrabilidad en despegue y aterrizaje.
* *Capacidad de Piso (Floor Loading Limits):* Cada compartimento de carga posee límites estructurales de resistencia por unidad de superficie (kg/m² o lbs/ft²). La validación matricial garantiza que el peso distribuido no supere la resistencia máxima del piso del fuselaje, evitando daños en la estructura.

---

##  Diagrama de Arquitectura Modular

```text
       +-------------------------------------------------------+
       |                       main.py                         |
       |  (Script principal: Datos de prueba y visualización)  |
       +---------------------------+---------------------------+
                                   |
            1. Envía matriz        |        2. Devuelve booleano/
               de carga            v           métricas calculadas
       +-------------------------------------------------------+
       |                     aerocargo.py                      |
       |  (Módulo de validación, submatrices y cálculos)       |
       |                                                       |
       |  - validar_matriz()  -> Comprueba dimensiones/valores |
       |  - obtener_submatriz() -> Extrae región de carga       |
       |  - calcular_ocupacion() -> % de celdas utilizadas     |
       |  - balance_lateral()   -> Compara peso Izq vs Der     |
       +---------------------------+---------------------------+
                                   ^
            3. Importa y valida    |
               funciones           |
       +---------------------------+---------------------------+
       |                  test_aerocargo.py                    |
       |  (Suite Pytest: Casos típicos y casos de borde)       |
       +-------------------------------------------------------+