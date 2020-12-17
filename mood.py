from spotify_client import SpotifyClient

import json

def main():
    client = SpotifyClient("Default Name")
    client.get_recommendations(t_energy=0.2, t_valence=0.1)
    print(json.dumps(client.recommendations.json(), indent=2))

main()