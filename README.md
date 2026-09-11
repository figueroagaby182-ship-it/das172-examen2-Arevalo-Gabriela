# AeroCargo-Matrix 

**Reto Evaluativo:** Auditoría y Balance Matricial de Distribución de Carga en Bahía de Aeronave (*AeroCargo-Matrix*).

---

##  III. Contexto de Ingeniería Aeronáutica

En el transporte aéreo de carga y la aviación comercial, la correcta distribución del peso en la bodega (*cargo hold*) de una aeronave es fundamental por dos razones operativas y de seguridad:

1. **Capacidad y Resistencia del Piso:** Cada sección del piso de carga soporta un peso máximo permitido en kilogramos ($\text{kg}$). Si una zona se sobrecarga ($>100\%$), se compromete la integridad estructural del piso y las vigas del fuselaje.
2. **Balance y Simetría:** Para garantizar un vuelo seguro y maniobrable, el peso debe estar equilibrado entre el lado izquierdo (**Babor**) y el lado derecho (**Estribor**), omitiendo la columna central si el número de columnas $M$ es impar por ubicarse sobre el eje de simetría longitudinal de la aeronave.

El piso de carga se discretiza como una cuadrícula bidimensional de dimensiones $N \times M$ ($N$ filas a lo largo de proa a popa y $M$ columnas de izquierda a derecha).

---

##  IV. Estructura de Datos y Reglas de Cálculo

El sistema procesa dos matrices de entrada $N \times M$ e implementa las siguientes reglas de operación:

* **Porcentaje de Ocupación Celda a Celda:**
  $$\text{PorcentajeOcupacion}(i, j) = \left( \frac{\text{PesoReal}(i, j)}{\text{CapacidadMaxima}(i, j)} \right) \times 100.0$$
  *(Condición de sobrecarga: Celda activa si $\text{PorcentajeOcupacion} > 100.0\%$)*

* **Peso Total Fila (Longitudinal):**
  $$\text{PesoTotalFila}(i) = \sum_{j=0}^{M-1} \text{PesoReal}(i, j)$$

* **Desbalance Lateral (Transversal):**
  $$\text{DesbalanceLateral} = \vert{}\text{SumaPesosMitadIzquierda} - \text{SumaPesosMitadDerecha}\vert{}$$
  *(Si $M$ es impar, la columna central $M // 2$ se omite por alineación sobre el eje de simetría).*

---

##  Análisis de Complejidad Computacional

El comportamiento de los módulos ante matrices $N \times M$ cumple con los siguientes parámetros formales:

* **Complejidad Temporal — $O(N \times M)$:**
  Las funciones de validación, porcentaje celda a celda y sumatoria de pesos transversales/longitudinales requieren un recorrido lineal de las $N \times M$ celdas de la cuadrícula. La extracción de ventana crítica de tamaño $k \times p$ opera bajo $O((N-k+1) \times (M-p+1) \times k \times p)$.

* **Complejidad Espacial — $O(N \times M)$:**
  Se utilizan funciones puras sin variables globales ni mutación de datos de entrada. La matriz de porcentajes retenida en memoria utiliza espacio auxiliar proporcional al tamaño $N \times M$.

---

##  Arquitectura Modular del Sistema

```mermaid
flowchart TD
    MAIN[main.py<br><i>Ejecución y Presentación</i>] -->|Cargas y Capacidades| AERO[aerocargo.py<br><i>Módulo Principal de Lógica</i>]
    AERO -->|Resultados y Métricas| MAIN
    TEST[test_aerocargo.py<br><i>Suite de Pruebas Unitarias</i>] -->|Validación de Módulos| AERO

    subgraph MODULOS ["V. Módulos Requeridos (aerocargo.py)"]
        M1[1. validar_matrices: Coherencia dimensional N x M]
        M2[2. calcular_ocupacion_y_sobrecarga: Matriz % y lista >100%]
        M3[3. evaluar_balance_y_simetria: Vectores longitudinales y desbalance kg]
        M4[4. extraer_submatriz_critica: Ventana k x p de mayor ocupación]
    end

    AERO --- MODULOS