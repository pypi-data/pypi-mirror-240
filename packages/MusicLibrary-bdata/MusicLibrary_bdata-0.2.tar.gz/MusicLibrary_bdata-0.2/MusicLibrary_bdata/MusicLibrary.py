import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import requests
import time
import pandas as pd

class Search():
    """
    Clase para realizar búsquedas de canciones, artistas y álbumes en la API de Spotify.
    """
    def __init__(self, client_id, client_secret):
        """
        Inicializa la clase con las credenciales del cliente para acceder a la API de Spotify.

        Args:
            client_id (str): Identificador del cliente.
            client_secret (str): Clave secreta del cliente.
        """
        try:
            client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
            self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        except spotipy.SpotifyException as e:
            print("Error en la API de Spotify:", e)

        self.lista_id_cancion = []
        self.lista_id_artista = []
        self.lista_nombre_cancion = []
        self.lista_nombre_artista = []
        self.lista_nombre_album = []
        self.lista_nombre_artista_cancion = []


    def search_song(self):
        """
        Realiza una búsqueda de canciones en la API de Spotify.

        Returns:
            lista_id_cancion (list): Lista de identificadores únicos de canciones. 
            df_canciones (DataFrame): Detalles de las canciones encontradas. 
        """
        try:
            nombre_cancion = input('¿Que canción desea buscar? ')
            num_coincidencias = int(input('¿Cuantas coincidencias desea buscar? '))
        except ValueError:
            print("Error de tipo al introducir número de coincidencias.")
            return None
        else:
            detalles_cancion = self.sp.search(q=nombre_cancion, limit=num_coincidencias, type='track')
            tracks = detalles_cancion['tracks']['items']
            assert tracks != [], "Error: No se encontraron resultados para la canción buscada."
            
            dict_atributos = {}
            for num, cancion in enumerate(tracks):
                self.lista_nombre_cancion.append(cancion['name'])
                self.lista_nombre_artista_cancion.append(cancion['artists'][0]['name'])
                self.lista_id_cancion.append(cancion['id'])

                nombre_cancion = cancion['name']
                nombre_artista=cancion['artists'][0]['name']
                nombre_album = cancion['album']['name']
                duracion_ms = cancion['duration_ms']
                duracion_min = duracion_ms // 60000
                duracion_s = (duracion_ms % 60000) // 1000 
                duracion_cancion = str(duracion_min)+' min '+str(duracion_s)+' seg'
                fecha_lanzamiento = cancion['album']['release_date']
                n_cancion = 'cancion '+str(num)
                dict_atributos[n_cancion] = [nombre_cancion,nombre_artista,nombre_album,duracion_cancion,fecha_lanzamiento]
            
                print('Canción', str(num + 1) + ':')
                print(f"Nombre de la canción: {nombre_cancion} - Nombre del artista: {nombre_artista} - Nombre del álbum: {nombre_album} - Duración de la canción: {duracion_cancion} - Fecha de lanzamiento: {fecha_lanzamiento}",'\n')
            
            df_canciones = pd.DataFrame(dict_atributos).T.reset_index(drop=True)
            df_canciones.columns=['Nombre_cancion', 'Nombre_artista', 'Nombre_album', 'Duracion_cancion', 'Fecha_lanzamineto']
            return self.lista_id_cancion, df_canciones

    def search_artist(self):
        """
        Realiza una búsqueda de artistas en la API de Spotify.

        Returns:
            lista_id_artista (list): Lista de identificadores únicos de artistas. 
            df_artista (DataFrame): Detalles de los artistas encontrados.
        """
        try:
            nombre_artista = input('¿Que artista desea buscar? ')
            num_coincidencias = int(input('¿Cuantas coincidencias desea buscar? '))
        except ValueError:
            print("Error de tipo al introducir número de coincidencias.")
        else:
            detalles_artista = self.sp.search(q=nombre_artista, limit=num_coincidencias, type='artist')
            artist = detalles_artista['artists']['items']
            assert artist != [], "Error: No se encontraron resultados para el artista buscado."
            dict_atributos = {}
            for num, artista_encontrado in enumerate(artist):
                self.lista_nombre_artista.append(artista_encontrado['name'])
                nombre_artista= artista_encontrado['name']
                popularidad = artista_encontrado['popularity']
                followers = artista_encontrado['followers']['total']
                generos = artista_encontrado['genres']
                self.lista_id_artista.append(artista_encontrado['id'])

                n_artista = 'artista '+str(num)
                dict_atributos[n_artista] = [nombre_artista,popularidad, followers, generos]

                print('Artista', str(num + 1) + ':')
                print(f"Nombre del artista: {nombre_artista} - Popularidad: {popularidad} - Número total de seguidores: {followers} - Generos: {generos}\n")

            df_artista = pd.DataFrame(dict_atributos).T.reset_index(drop=True)
            df_artista.columns=['Nombre_artista', 'Popularidad', 'Seguidores', 'Generos']
            return self.lista_id_artista, df_artista

    def search_album(self):
        """
        Realiza una búsqueda de álbumes en la API de Spotify.

        Returns:
            df_album (DataFrame): Detalles de los albumes encontrados.
        """
        try:
            nombre_album = input('¿Que álbum desea buscar? ')
            num_coincidencias = int(input('¿Cuantas coincidencias desea buscar? '))
        except ValueError:
            print("Error de tipo al introducir número de coincidencias.")
        else:
            detalles_album = self.sp.search(q=nombre_album, limit=num_coincidencias, type='album')
            album = detalles_album['albums']['items']
            assert album != [], "Error: No se encontraron resultados para el album buscado."
            dict_atributos = {}
            for num, album_encontrado in enumerate(album):

                nombre_album = album_encontrado['name']
                nombre_artista = album_encontrado['artists'][0]['name'] 
                fecha_lanzamiento = album_encontrado['release_date']
                num_canciones = album_encontrado['total_tracks']

                print('\nÁlbum', str(num + 1) + ':')
                print(f"Nombre del álbum: {nombre_album} - Nombre del artista: {nombre_artista} - Fecha de lanzamiento del álbum: {fecha_lanzamiento} - Número total de canciones: {num_canciones}")
            
                detalles_canciones = self.sp.album_tracks(album_encontrado['id'])
                if detalles_canciones['items']:
                    print("Lista de canciones:")
                    lista_canciones =  []
                    for num_cancion, cancion in enumerate(detalles_canciones['items']):
                        print(f"{num_cancion + 1}. {cancion['name']}")
                        lista_canciones.append(cancion['name'])
                else:
                    print("No se han encontrado detalles de la lista de canciones.")
                
                n_album = 'album '+str(num)
                dict_atributos[n_album] = [nombre_album,nombre_artista,fecha_lanzamiento,num_canciones, lista_canciones]

            df_album = pd.DataFrame(dict_atributos).T.reset_index(drop=True)
            df_album.columns=['Nombre_album','Nombre_artista', 'Fecha_lanzamiento', 'Num_canciones', 'Nombre_canciones']
            return df_album




    def song_statistics(self, lista_ids):
        """
        Realiza una búsqueda de estadísticas sobre canciones en la API de Spotify.

        Args:
            lista (list): Lista de identificadores únicos de canciones.

        Returns:
            df_estadisticas (DataFrame): Estadísticas sobre las canciones encontradas.
        """
        try:
            num = int(input('Por favor indique el número de canción del de que desea conocer más estadísticas: '))
        except ValueError:
            print("Error de tipo al introducir número de estadísticos deseados.")
        else:
            dict_estadisticas={}
            for index, id_cancion in enumerate(lista_ids[:num]):
                audio_analysis = self.sp.audio_features(tracks=[id_cancion])
                acousticness = audio_analysis[0]['acousticness']
                danceability = audio_analysis[0]['danceability']
                energy = audio_analysis[0]['energy']
                liveness = audio_analysis[0]['liveness']
                valence = audio_analysis[0]['valence'] 
                speechiness = audio_analysis[0]['speechiness']

                track_name = self.lista_nombre_cancion[index]
                artist_name = self.lista_nombre_artista_cancion[index]

                print(f"Canción: {track_name} - Artista: {artist_name}")

                print("Acousticness:", acousticness)
                print("Danceability:", danceability)
                print("Energy:", energy)
                print("Liveness:", liveness)
                print("Valence:", valence)
                print("Speechiness:", speechiness)
                print("\n")  
            
                dict_estadisticas[index] = [track_name,artist_name,acousticness,danceability,energy,liveness,valence,speechiness]

            df_estadisticas = pd.DataFrame(dict_estadisticas).T.reset_index(drop=True)
            df_estadisticas.columns=['Nombre_cancion', 'Nombre_artista', 'Acousticness', 'Danceability', 'Energy', 'Liveness', 'Valence', 'Speechiness']

            return df_estadisticas

    
    def songs_by_genre(self):
        """
        Realiza una búsqueda de canciones por género musical en la API de Spotify.

        Returns:
            df_genero (DataFrame): Detalles de los canciones encontradas por género musical.
        """
        try:
            genero = input('¿De qué género desea buscar canciones? ')
            num_coincidencias = int(input('¿Cuantas coincidencias desea buscar? '))
        except ValueError:
            print("Error de tipo al introducir número de coincidencias.")
        else:
            query = f'genre:{genero}'
            detalles_cancion = self.sp.search(q=query, limit=num_coincidencias, type='track')
            cancion_genero = detalles_cancion['tracks']['items']
            assert cancion_genero != [], "Error: No se encontraron resultados para el artista buscado."
            dict_atributos = {}
            for num, cancion in enumerate(cancion_genero):
                nombre_cancion = cancion['name']
                nombre_artista=cancion['artists'][0]['name']
                nombre_album = cancion['album']['name']
                duracion_ms = cancion['duration_ms']
                duracion_min = duracion_ms // 60000
                duracion_s = (duracion_ms % 60000) // 1000 
                duracion_cancion = f"{duracion_min} min {duracion_s} seg"
                fecha_lanzamiento = cancion['album']['release_date']

                print('Canción', str(num + 1) + ':')
                print(f"Nombre de la canción: {nombre_cancion} - Nombre del artista: {nombre_artista} - Nombre del álbum: {nombre_album} - Duración de la canción: {duracion_cancion} - Fecha de lanzamiento: {fecha_lanzamiento}", '\n')

                n_cancion = 'cancion '+str(num)
                dict_atributos[n_cancion] = [nombre_cancion,nombre_artista,nombre_album,duracion_cancion,fecha_lanzamiento]

            df_genero = pd.DataFrame(dict_atributos).T.reset_index(drop=True)
            df_genero.columns=['Nombre_cancion', 'Nombre_artista', 'Nombre_album', 'Duracion_cancion', 'Fecha_lanzamineto']

            return df_genero

class Recommend(Search):
    """
    Clase para realizar recomendaciones de canciones y artistas en la API de Spotify. 
    Hereda la clase Search para aprovechar sus funcionalidades de búsqueda.

    """
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def recommend_by_song(self):
        """
        Realiza una búsqueda y recomendación de canciones en base a otra canción.

        Returns:
            recomendacion_canciones (list): Lista de listas con detalles de las canciones recomendadas (nombre de la canción y del artista).
        """
        lista_ids, df= self.search_song() 
        time.sleep(2)
        try:
            seleccion = int(input("¿De cuál de estas canciones quiere realizar recomendaciones? "))
            num_recomendacion = int(input("¿Cuántas recomendaciones quieres que se realicen? "))
        except ValueError:
            print("Error de tipo al introducir número de recomendaciones.")
        else:
            try: 
                recommendations = self.sp.recommendations(seed_tracks=[lista_ids[seleccion-1]], limit=num_recomendacion)
                print(f"\nNombre: {self.lista_nombre_cancion[seleccion-1]} Artista: {self.lista_nombre_artista_cancion[seleccion-1]}")
            except IndexError: 
                print('Selección incorrecta, debe introducir un número entre 1 y', len(self.lista_nombre_artista_cancion))
            else: 
                self.lista_nombre_cancion = []
                self.lista_nombre_artista_cancion = []
                if recommendations['tracks']:
                    print("\nCanciones recomendadas:")
                    recomendacion_canciones = []
                    for i, track in enumerate(recommendations['tracks']):
                        print(f"{i + 1}. {track['name']} - {track['artists'][0]['name']}")
                        recomendacion_canciones.append([track['name'],track['artists'][0]['name']])
                else:
                    print("No se encontraron canciones recomendadas para esta canción.")
                return recomendacion_canciones


    def recommend_by_artist(self):
        """
        Realiza una búsqueda y recomendación de artistas en base a otro artista.

        Returns:
            recomendacion_artista (list): Lista con los nombres de los artistas recomendados.
        """
        artist_ids, df= self.search_artist()
        time.sleep(3)
        try:
            seleccion = int(input("¿De cuál de estos artistas quiere realizar recomendaciones? "))
            num_recomendacion = int(input("¿Cuántas recomendaciones quieres que se realicen? "))
        except ValueError:
            print("Error de tipo al introducir número de recomendaciones.")

        else:
            try: 
                print(f"ID del artista seleccionado:{self.lista_nombre_artista[seleccion-1]}")
                recommendations = self.sp.recommendations(seed_artists=[artist_ids[seleccion-1]], limit=num_recomendacion)
            except IndexError: 
                print('Selección incorrecta, debe introducir un número entre 1 y', len(self.lista_nombre_artista))
            else:    
                self.lista_nombre_artista = []
                if recommendations['tracks']:
                    print("\nArtistas recomendados:")
                    recomendacion_artista= []
                    for i, track in enumerate(recommendations['tracks']):
                        for artist_info in track['album']['artists']:
                            artist_name = artist_info['name']
                            print(f"{i + 1}. {artist_name}")
                            recomendacion_artista.append(artist_name)

                else:
                    print("No se encontraron artistas recomendados para este artista.")
                return recomendacion_artista

class LyricsSearch:
    """
    Clase para buscar letras de canciones utilizando la API de Musixmatch.

        Atributos:
        - base_url (str): URL base para las solicitudes a la API de Musixmatch.
        - api_key_lyrics (str): Clave API proporcionada para autenticación.
        - track_id (str): ID de la letra de la canción recuperada.
        - lyrics (str): Letras de la canción recuperada.
        - songs_info (list): Lista para almacenar información de canciones.
    """

    def __init__(self, api_key_lyrics):
        """ 
        Inicializa la clase con la clave proporcionada en la API Musixmatch.

        Args:
        api_key_lyrics (str): Clave API para acceder a Musixmatch.

        """
        self.base_url = 'https://api.musixmatch.com/ws/1.1/'
        self.api_key_lyrics = api_key_lyrics
        self.track_id = None
        self.lyrics = None
        self.songs_info = []

    def search_lyrics(self):
        """
        Realiza una búsqueda de letras de canciones en la API de Musixmatch.

        Returns:
            lyrics (): Letra de la canción.
            track_id (): Identificadores único de la canción.
        """
        artist = input('Por favor introduce el nombre del artista')
        track_name =  input('Por favor introduce el nombre de la canción' )
        url = f"{self.base_url}matcher.lyrics.get?format=json&q_artist={artist}&q_track={track_name}&apikey={self.api_key_lyrics}"
        response = requests.get(url)
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud HTTP: {e}')
        else:
            data = response.json()
            try:
                data["message"]['body']['lyrics']['lyrics_id']
            except KeyError:
                return "Letras no encontradas."
            else:
                self.track_id = data["message"]["body"]["lyrics"]["lyrics_id"]
                self.lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]
                self.lyrics = self.lyrics.replace('(1409623939991)','')
                self.lyrics = self.lyrics.replace('*** This Lyrics is NOT for Commercial use ***','')
                print(self.lyrics)
                return self.lyrics, self.track_id 
    
    def top_songs_by_country(self):
        """
        Realiza una búsqueda de las canciones más populares en un país específico utilizando la API de Musixmatch.

        Returns:
            songs_info (): Lista de diccionarios con detalles de las canciones, incluyendo el nombre de la canción, la calificación, el ID común de la canción y las letras.
        """

        try:
            num_songs = int(input('¿Cuantas canciones quieres buscar? '))
        except ValueError:
            print('Valor incorrecto, debe introducir un número')
        else:
            sel_country = input('¿Del top de qué país quieres obtener las canciones? (Introduce las siglas en minúscula) ')
            url = f"{self.base_url}chart.tracks.get?chart_name=top&page=1&page_size={num_songs}&country={sel_country}&f_has_lyrics=1&apikey={self.api_key_lyrics}"
            try:
                response = requests.get(url)
            except requests.exceptions.RequestException as e:
                print(f'Error en la solicitud HTTP: {e}')
            else:
                data = response.json()
                try:
                    songs = data["message"]["body"]["track_list"]
                except KeyError:
                    print('Letras no encontradas')
                else:
                    for song in songs:
                        song_details = {
                            "track_name": song["track"]["track_name"],
                            "rating": song["track"]["track_rating"],
                            "commontrack_id": song["track"]["commontrack_id"]
                        }

                        lyrics = self.get_lyrics_by_id(song["track"]["commontrack_id"])
                        song_details["lyrics"] = self.lyrics
                        self.songs_info.append(song_details)

                        print("Nombre de la canción:", song_details["track_name"])
                        print("Rating:", song_details["rating"])
                        print("ID de la canción:", song_details["commontrack_id"])
                        print("Letra:", lyrics)
                        print("\n")
                    return self.songs_info
                    

    def get_lyrics_by_id(self, commontrack_id):
        """
        Obtiene las letras de una canción utilizando el ID común de la canción mediante la API de Musixmatch.

        Args:
        commontrack_id (str): ID común de la canción para la cual se buscarán las letras.

        Returns:
            lyrics (str): Letra de la canción. 
        """
        url = f"{self.base_url}track.lyrics.get?commontrack_id={commontrack_id}&apikey={self.api_key_lyrics}"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud HTTP: {e}')
        else:
            data = response.json()

            try:
                songs = data["message"]["body"]["lyrics"]
            except KeyError:
                print('Letras no encontradas')
            else:
                self.lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]
                self.lyrics = self.lyrics.replace('(1409623939991)','')
                self.lyrics = self.lyrics.replace('*** This Lyrics is NOT for Commercial use ***','')
                return self.lyrics
