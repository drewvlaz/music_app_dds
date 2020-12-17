from playlist import Playlist

import json

def main():
    recs = Playlist("Default Name")
    recs.get_recommendations()
    print(json.dumps(recs.recommendations.json(), indent=2))

main()