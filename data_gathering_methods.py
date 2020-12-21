"""
# method gets artist and genre for the states and cities using city file in each state folder

import time
from find_artists import FindArtists_wiki
from artist_genre import ArtistGenre
import os



#state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
state_names = []

path = os.getcwd() + "\\Artist and Genre\\"
print (path)

for state in state_names:
    cities = []
    filename = (path + state + r"\cities.txt")
    with open(filename, 'r') as fd:
        for line in fd:
            cities.append(line.rstrip("\n"))

    main_path = path + state
    for a in cities:
        start = time.time()
        artists = set()
        try:
            class1 = FindArtists_wiki(a, state)
            artists = class1.findArtistsByLocation()
        except:
            print(a + ", " + state + " does not have a page")
            continue

        try_again = True
        while try_again == True:
            try:
                class2 = ArtistGenre(artists)
                artist_genre_info = (class2.getAllArtistsGenre())
                try_again = False
            except:
                try_again = True
                print (a + ":   ArtistGenre Class Error. Trying again in 2 seconds")
                time.sleep(2)

        file1 = open((main_path + "\\" + a + ".txt"), "w")
        for ii in artist_genre_info:
            try:
                file1.write(ii + "\n")
            except UnicodeEncodeError:
                pass
        file1.close()

        end = time.time()

        # prints when city is done to console
        print(a + ", " + state + ":   Genre Search Time: " + str(end - start) + " for " + str(
            len(artists)) + " results")

    print ("COMPLETED: " + state)
"""