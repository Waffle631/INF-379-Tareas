# INF-379-Tareas

Tarea desarrollada por:
- Adolfo Espinosa
- Bastihan
- Tomas

La fuente de datos principal es Anime Dataset 2023 (https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset),
en donde tenemos tres archivos: anime-dataset-2023.csv, users-details-2023.csv y users-score-2023.csv

Por temas de tamaño, solo se pueden subir los archivos anime-dataset-2023.csv y users-details-2023.csv al repositorio,
ya que users-score-2023.csv pesa más de 1GB

Descrición de los datasets:
------------------------------------------ "anime-dataset-2023.csv" ----------------------------------------------
anime_id: Identificador único de cada anime.
Name: Nombre del anime en su idioma original.
English name: Nombre en inglés del anime.
Other name: Nombre nativo o título del anime (puede estar en japonés, chino o coreano).
Score: Puntuación o calificación asignada al anime.
Genres: Géneros del anime, separados por comas.
Synopsis: Breve descripción o resumen de la trama del anime.
Type: Tipo de anime (por ejemplo, serie de TV, película, OVA, etc.).
Episodes: Número de episodios del anime.
Aired: Fechas en que se emitió el anime.
Premiered: Temporada y año en que se estrenó el anime.
Status: Estado del anime (por ejemplo, finalizado, en emisión, etc.).
Producers: Compañías productoras o productores del anime.
Licensors: Distribuidores del anime (por ejemplo, plataformas de streaming).
Studios: Estudios de animación que trabajaron en el anime.
Source: Material de origen del anime (por ejemplo, manga, novela ligera, original).
Duration: Duración de cada episodio.
Rating: Clasificación por edad del anime.
Rank: Posición del anime en el ranking según popularidad u otros criterios.
Popularity: Ranking de popularidad del anime.
Favorites: Número de veces que los usuarios marcaron el anime como favorito.
Scored By: Número de usuarios que calificaron el anime.
Members: Número de miembros que añadieron el anime a su lista.
Image URL: URL de la imagen o póster del anime.

--------------------------------------------- "users-details-2023.csv" ------------------------------------------------
Mal_ID: Identificador único de cada usuario.
Username: Nombre de usuario del usuario.
Gender: Género del usuario.
Birthday: Fecha de nacimiento del usuario (en formato ISO).
Location: Ubicación o país del usuario.
Joined: Fecha en la que el usuario se unió a la plataforma (en formato ISO).
Days Watched: Número total de días que el usuario ha pasado viendo anime.
Mean Score: Puntuación media que el usuario ha dado a los animes que ha visto.
Watching: Número de animes que el usuario está viendo actualmente.
Completed: Número de animes completados por el usuario.
On Hold: Número de animes en pausa por el usuario.
Dropped: Número de animes que el usuario ha abandonado.
Plan to Watch: Número de animes que el usuario planea ver en el futuro.
Total Entries: Número total de entradas en la lista del usuario.
Rewatched: Número de animes que el usuario ha vuelto a ver.
Episodes Watched: Número total de episodios vistos por el usuario.

---------------------------------------------- "users-score-2023.csv" -------------------------------------------------
user_id: Identificador único de cada usuario.
Username: Nombre de usuario del usuario.
anime_id: Identificador único de cada anime.
Anime Title: Título del anime.
rating: Calificación otorgada por el usuario al anime.