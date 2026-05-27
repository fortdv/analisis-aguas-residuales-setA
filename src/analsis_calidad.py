import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
df = pd.read_excel("data/dataset_set_A_aguas_residuales.xlsx")

# --- 1. Tabla de calidad de datos ---

calidad = {
    "Variable": [
        "fecha_registro",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "caudal_entrada_m3_d",
        "energia_aeracion_kWh",
        "cumplimiento_norma"
    ],
    "Problema detectado": [
        "Fechas no ordenadas",
        "Valores extremos",
        "Variabilidad abrupta",
        "Variabilidad excesiva",
        "Valores dispares",
        "Inconsistencias"
    ],
    "Riesgo asociado": [
        "Afecta tendencias",
        "Sesga eficiencia",
        "Oculta fallas",
        "Errores de medición",
        "Dificulta análisis energético",
        "Reportes incorrectos"
    ]
}

df_calidad = pd.DataFrame(calidad)
print("\nTabla de análisis de calidad de datos:")
print(df_calidad)

# --- 2. Gráfico de valores extremos DBO entrada ---

plt.figure(figsize=(10,5))
sns.boxplot(x=df["DBO_entrada_mg_L"])
plt.title("Detección de valores extremos en DBO de entrada")
plt.xlabel("DBO entrada (mg/L)")
plt.grid(True)
plt.tight_layout()
plt.savefig("dashboard/analisis_calidad_dbo.png")
plt.show()

print("\nGráfico de calidad generado correctamente.")
