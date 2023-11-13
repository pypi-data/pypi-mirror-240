#%%
# Importar librerias
from MusicLibrary import *

# Claves para API
client_id = 'd29cd1a0fefa49c3ac200d7a66c7d308'
client_secret = 'b25abefbd93b4254aa9d302a38afb8d1'
api_key_lyrics = '39b3f63c63948221ef8d876f142493e4'

# Instanciar las clases
buscador = Search(client_id,client_secret)
recomendador = Recommend(client_id,client_secret)
letras = LyricsSearch(api_key_lyrics)

#%%
# Uso de la clase Search

lista_id,df_canciones = buscador.search_song()
df_estadisticas = buscador.song_statistics(lista_id)
a, df_artistas = buscador.search_artist()
df_albumes = buscador.search_album()
df_canciones_genero = buscador.songs_by_genre()
#%%
# Uso de la clase Recommend
resultado_cancion = recomendador.recommend_by_song()
resultado_artista = recomendador.recommend_by_artist()

#%%
# Uso de la clase LyricsSearch
letras_canciones,ids = letras.search_lyrics()
#%%
informacion = letras.top_songs_by_country()
# %%
