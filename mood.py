from secrets import SPOTIFY_TOKEN
import requests

class Playlist:
    """ Contains and controls playlist elements """

    def __init__(self, name):
        self.name = name

    def get_recommendations(self):
        """ Get playlist data from spotify """
        query = f'https://api.spotify.com/v1/recommendations'
        # query = f'https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_danceability=.1&max_danceability=.9&target_danceability=.4&min_energy=0.4&min_popularity=50'
        # NOTE: Auth token expires every hour
        # TODO: Set up auth workflow to get around this
        self.data = requests.get(
            query,
            params={
                # 'fields': 'items(track(album(artists, images), name))'
                'market': 'US',
                'seed_artists': '4NHQUGzhtTLFvgF5SZesLK',
                'seed_genres': 'rap',
                'seed_tracks': '0c6xIDDpzE81m2q797ordA',
                'limit': '1'
                # 'min_acousticness': 0.1
                # 'max_acousticness': 0.1
                # 'target_acousticness': 0.1
                # 'min_dancebility': 0.1
                # 'max_dancebility': 0.1
                # 'target_dancebility': 0.1
                # 'min_energy': 0.1
                # 'max_energy': 0.1
                # 'target_energy': 0.1
                # 'min_liveness': 0.1
                # 'max_liveness': 0.1
                # 'target_liveness': 0.1
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {SPOTIFY_TOKEN}',
            }
        )

pl = Playlist("Test")
pl.get_recommendations()
print(pl.data.json())