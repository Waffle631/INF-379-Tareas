import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Cargar el CSV si no lo has hecho ya
df = pd.read_csv("Datos\cuestionario.csv", sep=';', encoding='latin1')

# Renombrar columnas para facilidad
df = df.rename(columns={
    df.columns[6]: 'Ropa/Accesorios',
    df.columns[7]: 'Videojuegos anime',
    df.columns[8]: 'Eventos anime',
    df.columns[9]: 'Música japonesa'
})

# Contar las frecuencias por categoría
categorias = ['Ropa/Accesorios', 'Videojuegos anime', 'Eventos anime', 'Música japonesa']
frecuencias = ['Nunca', 'Ocasionalmente', 'Frecuentemente']

conteo = {cat: df[cat].value_counts().reindex(frecuencias, fill_value=0) for cat in categorias}

# Construir datos para el waffle chart
from pywaffle import Waffle

# Datos totales a graficar
data = {}
for cat in categorias:
    for freq in frecuencias:
        label = f'{cat} - {freq}'
        data[label] = conteo[cat][freq]

# Definir colores por frecuencia
colores = {
    'Nunca': '#ff9999',
    'Ocasionalmente': '#ffcc99',
    'Frecuentemente': '#99ff99'
}

# Mapear colores a cada categoría-frecuencia
colors = [colores[freq] for label in data for freq in [label.split(' - ')[1]]]

# Crear el gráfico tipo waffle
fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=data,
    colors=colors,
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)},
    title={'label': 'Influencia del Anime en el Consumo Cultural', 'loc': 'center'}
)

plt.show()
