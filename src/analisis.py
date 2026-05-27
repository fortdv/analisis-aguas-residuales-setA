import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from funciones_calculo import eficiencia_dbo, cumplimiento_norma

# Cargar dataset
df = pd.read_excel("data/dataset_set_A_aguas_residuales.xlsx")

# Limpieza
df = df.dropna()
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])

# Cálculo de eficiencia
df['eficiencia_DBO'] = df.apply(
    lambda x: eficiencia_dbo(x['DBO_entrada_mg_L'], x['DBO_salida_mg_L']),
    axis=1
)

# Cálculo de cumplimiento
df['cumple_norma_calc'] = df['DBO_salida_mg_L'].apply(cumplimiento_norma)

# Resumen por planta
resumen = df.groupby('planta').agg({
    'caudal_entrada_m3_d': 'mean',
    'DBO_entrada_mg_L': 'mean',
    'DBO_salida_mg_L': 'mean',
    'eficiencia_DBO': 'mean',
    'cumple_norma_calc': 'mean'
}).reset_index()

print("\nResumen por planta:")
print(resumen)

# Gráfico DBO salida
plt.figure(figsize=(12,5))
sns.lineplot(data=df, x='fecha_registro', y='DBO_salida_mg_L', hue='planta')
plt.title("DBO de salida por planta")
plt.xlabel("Fecha")
plt.ylabel("DBO salida (mg/L)")
plt.grid(True)
plt.tight_layout()
plt.savefig("dashboard/grafico_dbo_salida.png")
plt.show()

# Exportar archivos para áreas internas
df_operaciones = df[['fecha_registro','planta','caudal_entrada_m3_d',
                     'DBO_entrada_mg_L','DBO_salida_mg_L',
                     'energia_aeracion_kWh','lodos_generados_kg_d']]

df_ambiental = df[['fecha_registro','planta','DBO_salida_mg_L','cumplimiento_norma']]

df_operaciones.to_csv("docs/reporte_operaciones.csv", index=False)
df_ambiental.to_csv("docs/reporte_ambiental.csv", index=False)

print("\nArchivos exportados correctamente.")
