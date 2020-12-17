from secrets import CLIENT_ID, CLIENT_SECRET

import requests
import json
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
        message = f"{CLIENT_ID}:{CLIENT_SECRET}"
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')

        r = requests.post(
            url,
            headers={
                'Authorization': f'Basic {base64Message}'
            },
            data={
                'grant_type': 'client_credentials'
            }
        )

        return r.json()['access_token']

    def get_recommendations(self, target_acousticness, target_danceability, target_energy, target_liveness):
        """ Get recommended songs from spotify """

        url = f'https://api.spotify.com/v1/recommendations'

        self.recommendations = requests.get(
            url,
            params={
                # 'fields': 'items(track(album(artists, images), name))'
                'market': 'US',
                'seed_artists': '4NHQUGzhtTLFvgF5SZesLK',
                'seed_genres': 'rap',
                'seed_tracks': '0c6xIDDpzE81m2q797ordA',
                'limit': '1',
                # 'min_acousticness': 0.1,
                # 'max_acousticness': 0.1,
                'target_acousticness': target_acousticness,
                # 'min_danceability': 0.1,
                # 'max_danceability': 0.1,
                'target_danceability': target_danceability,
                # 'min_energy': 0.1,
                # 'max_energy': 0.1,
                'target_energy': target_energy,
                # 'min_liveness': 0.1,
                # 'max_liveness': 0.1,
                'target_liveness': target_liveness
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.__get_auth_token()}',
            }
        )