from secrets import CLIENT_ID, CLIENT_SECRET

from random import randint
import requests
import base64

class Playlist:
    """ Contains and controls playlist elements """

    def __init__(self, name):
        self.name = name

    def __get_auth_token(self):
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

        return r.json()['access_token']

    def get_genres(self):
        """ Get list of available genres"""

        url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.__get_auth_token()}',
        }

        r = requests.get(url, headers=headers)

        return r.json()['genres']

    def get_recommendations(self, t_acousticness=None, t_danceability=None, t_energy=None, t_liveness=None, t_valence=None):
        """ Get recommended songs from spotify """

        genres = self.get_genres()
        seed_genres = ', '.join([genres[randint(0,len(genres)-1)] for _ in range(2)])

        url = f'https://api.spotify.com/v1/recommendations'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.__get_auth_token()}',
        }

        params = {
            'market': 'US',
            'seed_artists': '4NHQUGzhtTLFvgF5SZesLK',
            'seed_genres': seed_genres,
            'seed_tracks': '0c6xIDDpzE81m2q797ordA',
            'limit': 2
            # 'min_acousticness': 0.1,
            # 'max_acousticness': 0.1,
            # 'min_danceability': 0.1,
            # 'max_danceability': 0.1,
            # 'min_energy': 0.1,
            # 'max_energy': 0.1,
            # 'min_liveness': 0.1,
            # 'max_liveness': 0.1,
            # 'min_valence': 0.1,
            # 'max_valence': 0.1,
        }

        # Only add param if value passed in
        if t_acousticness != None:
            params['target_acousticness'] = t_acousticness
        if t_danceability != None:
            params['target_danceability'] = t_danceability
        if t_energy != None:
            params['target_energy'] = t_energy
        if t_liveness != None:
            params['target_liveness'] = t_liveness
        if t_valence != None:
            params['target_valence'] = t_valence

        self.recommendations = requests.get(url, headers=headers, params=params)
