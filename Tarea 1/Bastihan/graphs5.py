import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datos/anime-filtered.csv")
df = df[df['Aired'].notna() & df['Aired'].str.contains('to')]
df['start_date_str'] = df['Aired'].str.extract(r'^(.*) to')
df['start_date'] = pd.to_datetime(df['start_date_str'], errors='coerce')
df = df.dropna(subset=['start_date'])
df['year'] = df['start_date'].dt.year

df['year_group'] = (df['year'] // 5) * 5  # e.g., 2001 → 2000, 2006 → 2005

df['Genres'] = df['Genres'].fillna('').str.split(', ')
df_exploded = df.explode('Genres')

top_10_genres = df_exploded['Genres'].value_counts().head(10).index.tolist()

df_top = df_exploded[df_exploded['Genres'].isin(top_10_genres)]

genre_counts = df_top.groupby(['year_group', 'Genres']).size().unstack(fill_value=0)
genre_counts = genre_counts.sort_index()

genre_counts.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab10')
plt.title('Top 10 Anime Genres by 5-Year Intervals')
plt.xlabel('5-Year Interval')
plt.ylabel('Number of Animes')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
