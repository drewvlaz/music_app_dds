from spotify_client import SpotifyClient

import json

def main():
    client = SpotifyClient("Default Name")
    client.get_recommendations(t_danceability=0.3, t_energy=0.9, t_valence=0.7)
    id = client.search_item("Pop Smoke", "artist")
    # print(json.dumps(client.get_artist(id), indent=2))
    print(json.dumps(client.recommendations, indent=2))

main()