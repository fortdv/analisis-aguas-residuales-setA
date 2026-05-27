# Proyecto Analítico – AquaLimpia S.A.
Análisis del desempeño de las plantas de tratamiento de aguas residuales utilizando un flujo de trabajo reproducible basado en Python, visualización y control de versiones con Git.

---

##  1. Objetivo del Proyecto
El objetivo principal es analizar el comportamiento operacional de las plantas de tratamiento de AquaLimpia S.A. mediante:

- Limpieza y validación del dataset.
- Cálculo de indicadores clave como eficiencia del tratamiento.
- Análisis exploratorio de datos (EDA).
- Visualización mediante dashboard.
- Exportación de reportes para áreas internas.
- Documentación y trazabilidad mediante Git.

---

##  2. Estructura del Proyecto

- /src
- analisis.py
- funciones_calculo.py
- /notebooks
- analisis.ipynb
- /data
- dataset_set_A_aguas_residuales.xlsx
- /dashboard
- dashboard.pbix
- grafico_dbo_salida.png
- /docs
- informe.md
- README.md


Cada carpeta cumple un rol específico:

- **src/** → Scripts Python modulares.
- **notebooks/** → Análisis interactivo.
- **data/** → Dataset original.
- **dashboard/** → Visualizaciones y dashboard.
- **docs/** → Documentación técnica.
- **README.md** → Descripción general del proyecto.

---

##  3. Proceso Analítico

### **1. Ingesta de datos**
Se carga el archivo `dataset_set_A_aguas_residuales.xlsx`, que contiene más de 200 registros con variables como caudal, DBO, SST, pH, energía y cumplimiento normativo.

### **2. Limpieza y validación**
- Conversión de fechas.
- Eliminación de duplicados.
- Revisión de valores extremos (ej.: DBO > 400 mg/L).
- Estandarización de columnas.

### **3. Transformación**
- Cálculo de eficiencia del tratamiento:
  

\[
  \text{eficiencia} = \frac{DBO_{entrada} - DBO_{salida}}{DBO_{entrada}}
  \]


- Clasificación de cumplimiento normativo.
- Agregaciones por planta.

### **4. Análisis Exploratorio (EDA)**
- Tendencias temporales de DBO.
- Comparación entre plantas.
- Correlaciones entre variables.
- Identificación de días con incumplimiento.

### **5. Visualización**
Se genera un dashboard con:
- KPI de eficiencia.
- KPI de cumplimiento.
- Gráficos comparativos por planta.
- Alertas automáticas.


### **6. Exportación de reportes**
Se generan automáticamente:
- `reporte_operaciones.csv`
- `reporte_ambiental.csv`

### **7. Control de versiones con Git**
El repositorio incluye:
- Scripts modulares.
- Notebook.
- Dashboard.
- Documentación.
- Dataset.



---

##  4. Scripts Utilizados

### **funciones_calculo.py**
```python
import numpy as np

def eficiencia_dbo(DBO_in, DBO_out):
    return (DBO_in - DBO_out) / DBO_in

def cumplimiento_norma(DBO_out, limite=50):
    return 1 if DBO_out <= limite else 0

---
### Felipe Obreque Tarea Iacc 2026 Ciencias de datos
