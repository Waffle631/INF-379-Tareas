import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Datos\cuestionario.csv", encoding='latin1', sep=';')

# Preparar los datos para el radar chart
categorias = [
    'Música',
    'Moda',
    'Lenguaje',
    'Cine/series',
    'Redes sociales'
]

# Renombrar las columnas para facilitar el acceso
df_radar = df.rename(columns={
    df.columns[1]: 'Música',
    df.columns[2]: 'Moda',
    df.columns[3]: 'Lenguaje',
    df.columns[4]: 'Cine/series',
    df.columns[5]: 'Redes sociales'
})

# Seleccionamos a 3 usuarios como ejemplo
df_subset = df_radar[['Usuario'] + categorias].head(20)

# Crear ángulos para el gráfico de radar
num_vars = len(categorias)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # para cerrar el círculo

# Crear gráfico
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Dibujar cada usuario
for idx, row in df_subset.iterrows():
    valores = row[categorias].astype(int).tolist()
    valores += valores[:1]  # cerrar el gráfico
    ax.plot(angles, valores, label=f'Usuario {row["Usuario"]}')
    ax.fill(angles, valores, alpha=0.1)

# Ajustes del gráfico
ax.set_title('Jerarquía de Influencia Cultural (por Usuario)', size=14)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), categorias)
ax.set_ylim(1, 5)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()
