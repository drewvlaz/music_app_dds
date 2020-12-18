from secrets import CLIENT_ID, CLIENT_SECRET

from random import randint
import requests
import base64

class SpotifyClient:
    """ Contains and controls Spotify elements """

    def __init__(self, name):
        self.name = name
        self.get_access_token()
        self.get_genres()

    def search_item(self, query, type):
        """ Search for item in Spotify
            Type must be:
            album, artist, playlist, track, show or episode.
        """

        url = 'https://api.spotify.com/v1/search'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'q': query,
                'type': type
            }
        )

        try:
            return r.json()[f'{type}s']['items'][0]['id']
        except:
            # raise SpotifyException("Bad Search Parameter")
            return None

    def get_artist(self, id):
        """ Gets an artist using their Spotify ID """

        url = f'https://api.spotify.com/v1/artists/{id}'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
        )

        return r.json()


    def get_access_token(self):
        """ Get authorization token from client credentials """

        url = 'https://accounts.spotify.com/api/token'

        # Encode to base 64
        # Refer to https://dev.to/mxdws/using-python-with-the-spotify-api-1d02
        message = f'{CLIENT_ID}:{CLIENT_SECRET}'
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')

        r = requests.post(
            url,
            headers={'Authorization': f'Basic {base64Message}'},
            data={'grant_type': 'client_credentials'}
        )

        self.access_token = r.json()['access_token']

    def get_genres(self):
        """ Get list of available genres """

        url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            }
        )

        self.genres = r.json()['genres']

    def get_recommendations(self, t_acousticness=None, t_danceability=None, t_energy=None, t_liveness=None, t_valence=None):
        """ Get recommended songs from Spotify """

        seed_genres = ', '.join([self.genres[randint(0,len(self.genres)-1)] for _ in range(2)])

        url = f'https://api.spotify.com/v1/recommendations'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'market': 'US',
                'seed_artists': '4NHQUGzhtTLFvgF5SZesLK',
                'seed_genres': seed_genres,
                'seed_tracks': '0c6xIDDpzE81m2q797ordA',
                'limit': 50,
                # 'min_acousticness': 0.1,
                # 'max_acousticness': 0.1,
                'target_acousticness': t_acousticness,
                # 'min_danceability': 0.1,
                # 'max_danceability': 0.1,
                'target_danceability': t_danceability,
                # 'min_energy': 0.1,
                # 'max_energy': 0.1,
                'target_energy': t_energy,
                # 'min_liveness': 0.1,
                # 'max_liveness': 0.1,
                'target_liveness': t_liveness,
                # 'min_valence': 0.1,
                # 'max_valence': 0.1,
                'target_valence': t_valence
            }
        )

        self.recommendations = [r.json()['tracks'][x]['preview_url'] for x in range(len(r.json()['tracks']))]

class SpotifyException(Exception):
	pass