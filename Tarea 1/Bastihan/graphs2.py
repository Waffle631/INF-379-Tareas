import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Datos/anime-filtered.csv")

df = df[df['Aired'].notna() & df['Aired'].str.contains('to')]

df['start_date_str'] = df['Aired'].str.extract(r'^(.*) to')

df['start_date'] = pd.to_datetime(df['start_date_str'], errors='coerce')

df = df.dropna(subset=['start_date'])

df['year'] = df['start_date'].dt.year
df['quarter'] = df['start_date'].dt.quarter
df['genre_list'] = df['Genres'].str.split(',\s*')

df.to_csv("cleaned_anime.csv", index=False)

################################################

df_exploded = df.explode('genre_list')

df_exploded = df_exploded[df_exploded['genre_list'].notna()]

genre_quarter_counts = (
    df_exploded.groupby(['genre_list', 'quarter'])
    .size()
    .reset_index(name='count')
)

N = 10

top_genres = (
    genre_quarter_counts.groupby('genre_list')['count']
    .sum()
    .sort_values(ascending=False)
    .head(N)
    .index
)


quarters = [1, 2, 3, 4]
angles = np.linspace(0, 2 * np.pi, len(quarters), endpoint=False).tolist()
angles += angles[:1] 

genre_angle_data = {}

for genre in top_genres:
    
    row = genre_quarter_counts[genre_quarter_counts['genre_list'] == genre]
    row = row.set_index('quarter').reindex(quarters, fill_value=0)

    values = row['count'].values.tolist()
    values += values[:1]
    
    genre_angle_data[genre] = values

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for genre, values in genre_angle_data.items():
    ax.plot(angles, values, label=genre, linewidth=2)
    ax.fill(angles, values, alpha=0.2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])

ax.set_title(f"Top {N} Anime Genres by Quarter", va='bottom')
ax.grid(True)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()