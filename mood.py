from spotify_client import SpotifyClient

import json

def main():
    client = SpotifyClient("Default Name")
    client.get_recommendations(t_energy=0.2, t_valence=0.1)
    # print(client.search_item("artist", "Pop Smoke"))
    print(json.dumps(client.search_item("track", "White Ferrari"), indent=2))
    # print(json.dumps(client.recommendations, indent=2))

main()