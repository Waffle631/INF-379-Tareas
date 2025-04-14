import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Cargar datos
df = pd.read_csv('Datos/anime-filtered.csv')

# Limpiar Aired
df['start_date'] = df['Aired'].str.split(' to ').str[0]
df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')

# Sacar año y quarto de año
df['year'] = df['start_date'].dt.year
df['quarter'] = df['start_date'].dt.quarter

# Expandimos Genres por cada entrada, ya que cada entrada es de tipo "[a, b, c...]"
df['Genres'] = df['Genres'].apply(lambda x: x if isinstance(x, list) else str(x).split(', '))
df_exploded = df.explode('Genres')
df_exploded = df_exploded[df_exploded['Genres'].notna()]

# Agrupar y contar
genre_quarter_counts = (
    df_exploded.groupby(['Genres', 'year', 'quarter'])
    .size()
    .reset_index(name='count')
)

# Top N genres
N = 10
top_Genres = genre_quarter_counts.groupby('Genres')['count'].sum().sort_values(ascending=False).head(N).index
genre_quarter_counts = genre_quarter_counts[genre_quarter_counts['Genres'].isin(top_Genres)]

# Asegurarse que los indices no tengan duplicados
genre_quarter_counts = genre_quarter_counts.groupby(['Genres', 'year', 'quarter'], as_index=False)['count'].sum()

# Define quarters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
frame_list = []
unique_years = sorted(genre_quarter_counts['year'].dropna().unique())

# Construir frames para la animacion
for year in unique_years:
    year_data = genre_quarter_counts[genre_quarter_counts['year'] == year]
    frame_traces = []

    for genre in top_Genres:
        genre_data = year_data[year_data['Genres'] == genre]
        counts = genre_data.set_index('quarter').reindex([1, 2, 3, 4], fill_value=0)['count'].tolist()
        counts += counts[:1]  # loop closure

        frame_traces.append(go.Scatterpolar(
            r=counts,
            theta=quarters + [quarters[0]],
            mode='lines+markers',
            name=genre
        ))

    frame_list.append(go.Frame(data=frame_traces, name=str(year)))

# Initial data (first year)
init_year = unique_years[0]
init_data = []
init_year_data = genre_quarter_counts[genre_quarter_counts['year'] == init_year]
for genre in top_Genres:
    genre_data = init_year_data[init_year_data['Genres'] == genre]
    counts = genre_data.set_index('quarter').reindex([1, 2, 3, 4], fill_value=0)['count'].tolist()
    counts += counts[:1]
    init_data.append(go.Scatterpolar(
        r=counts,
        theta=quarters + [quarters[0]],
        mode='lines+markers',
        name=genre
    ))

# Create the figure with the initial data
fig = go.Figure(
    data=init_data,
    layout=go.Layout(
        title="Top Anime Genres by Quarter (Animated)",
        polar=dict(radialaxis=dict(visible=True)),
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {"label": "Play", "method": "animate", "args": [None, {"frame": {"duration": 700}, "fromcurrent": True}]},
                {"label": "Pause", "method": "animate", "args": [[None], {"mode": "immediate", "frame": {"duration": 0}}]}
            ]
        }],
        sliders=[{
            "steps": [{
                "method": "animate",
                "args": [[str(year)], {"mode": "immediate", "frame": {"duration": 700}}],
                "label": str(year)
            } for year in unique_years],
            "currentvalue": {"prefix": "Year: "}
        }]
    ),
    frames=frame_list
)

fig.show()
