from playlist import Playlist

import json

def main():
    recs = Playlist("Default Name")
    recs.get_recommendations(t_acousticness=0.1, t_danceability=0.1, t_energy=0.7, t_liveness=0.1, t_valence=0.5)
    print(json.dumps(recs.recommendations.json(), indent=2))

main()