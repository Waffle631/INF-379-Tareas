import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("Datos\cuestionario.csv", encoding='latin1', sep=';')

# Renombrar columnas relevantes para facilidad
df = df.rename(columns={
    df.columns[10]: 'Relación emocional',
    df.columns[11]: 'Década impacto'
})

# Agrupar y contar ocurrencias
conteo = df.groupby(['Relación emocional', 'Década impacto']).size().reset_index(name='value')

# Exportar a CSV
conteo.to_csv("conteo_emocion_decada.csv", index=False, encoding='utf-8-sig')

print("Archivo exportado como 'conteo_emocion_decada.csv'")