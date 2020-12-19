from spotify_client import SpotifyClient

import json

def main():
    client = SpotifyClient("Default Name")
    recommendations = client.get_recommendations(t_energy=0.5, t_valence=0.8, t_tempo=120)
    id = client.search_item("The Piano Guys", "artist")
    # print(json.dumps(client.get_artist(id), indent=2))
    print(json.dumps(recommendations, indent=2))
    print(len(client.genres))

main()