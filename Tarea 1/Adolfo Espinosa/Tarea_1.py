import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import geopandas as gpd
from itertools import combinations
import networkx as nx
import seaborn as sns

# Cargar el archivo CSV
df_users = pd.read_csv("Datos/users-details-2023.csv")
df_scores = pd.read_csv("Datos/users-score-2023.csv")
df_anime = pd.read_csv("Datos/anime-dataset-2023.csv")
# Obtener todos los géneros en un solo string
generos_unicos = set()
df_anime["Genres"].dropna().str.split(", ").apply(generos_unicos.update)

# Contar la frecuencia de cada género en todo el dataset
genero_frecuencia = {}
for genero in generos_unicos:
    if genero != "UNKNOWN":
        genero_frecuencia[genero] = df_anime["Genres"].str.contains(genero, na=False).sum()

# Generar la nube de palabras
wordcloud = WordCloud(
    width=800, height=400, background_color="black", colormap="coolwarm"
).generate_from_frequencies(genero_frecuencia)

# Mostrar el gráfico
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Quitar los ejes
plt.title("Nube de Palabras de Géneros de Anime", fontsize=14)
plt.show()

# Cargar el dataset
df_anime = pd.read_csv('Datos/anime-dataset-2023.csv')

df_anime = df_anime.dropna(subset=['Genres', 'Score'])

# Convertir la columna de puntuaciones a numérica (manejo de errores)
df_anime['Score'] = pd.to_numeric(df_anime['Score'], errors='coerce')

# Separar los géneros en listas y eliminar duplicados dentro de cada anime
df_anime['Genres'] = df_anime['Genres'].str.split(',').apply(lambda x: list(set(x) if isinstance(x, list) else []))

# Expandir los géneros
df_genres = df_anime.explode('Genres')

# Eliminar valores nulos y espacios extra en los nombres de los géneros
df_genres = df_genres.dropna(subset=['Genres'])
df_genres['Genres'] = df_genres['Genres'].str.strip()

# **Eliminar el género "UNKNOWN"**
df_genres = df_genres[df_genres['Genres'].str.upper() != "UNKNOWN"]

# Filtrar géneros con al menos 10 animes para evitar distorsión
genre_counts = df_genres['Genres'].value_counts()
valid_genres = genre_counts[genre_counts >= 10].index
df_genres = df_genres[df_genres['Genres'].isin(valid_genres)]

# Verificar si hay valores duplicados en el índice y resetearlo
df_genres = df_genres.reset_index(drop=True)

# Graficar el Violin Plot
plt.figure(figsize=(12, 6))
sns.violinplot(x=df_genres['Genres'], y=df_genres['Score'], palette='coolwarm')
plt.xticks(rotation=90)
plt.title("Distribución de Puntuaciones por Género de Anime")
plt.xlabel("Género")
plt.ylabel("Puntuación")
plt.show()