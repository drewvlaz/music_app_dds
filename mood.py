from spotify_client import SpotifyClient

import json

def main():
    client = SpotifyClient("Default Name")
    recommendations = client.get_recommendations(t_energy=0.3, t_speechiness=0.7, t_valence=0.1)
    id = client.search_item("Pop Smoke", "artist")
    # print(json.dumps(client.get_artist(id), indent=2))
    print(json.dumps(recommendations, indent=2))

main()