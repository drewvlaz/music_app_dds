from playlist import Playlist

import json

def main():
    recs = Playlist("Default Name")
    recs.get_recommendations(0.1,0.1,0.1,0.1)
    print(json.dumps(recs.recommendations.json(), indent=2))

main()