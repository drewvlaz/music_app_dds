"""from find_artists import FindArtists_wiki
from artist_genre import ArtistGenre
import time

cities = ["Pottstown"]
states = ["Pennsylvania"]

#for state in states:
for i in range(len(cities)):
    try:
        start = time.time()
        artists = set()
        class1 = FindArtists_wiki(cities[i], states[i])
        artists = class1.findArtistsByLocation()

        class2 = ArtistGenre(artists)
        genre_info = (class2.getAllArtistsGenre())
        for a in genre_info:
            #write line to the file with name of the city
            print (a)

        end = time.time()
        # prints when city is done to console
        print(cities[i] + ", " + states[i] + ":   Genre Search Time: " + str(end - start) + " for " + str(len(artists)) + " results")
    except:
        print (cities[i] + ", " + states[i] + " does not have a page")
        pass"""


import os
import requests
from bs4 import BeautifulSoup
from find_artists import FindArtists_wiki
from artist_genre import ArtistGenre
import time
#state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]





response = requests.get(
    url=("https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068"),
)
soup = BeautifulSoup(response.content, 'html.parser')
soup = soup.find(class_ = "topic-content col-sm pr-lg-60").parent.find_next_sibling()

x = 326620
while (x<=326669):
    temp_soup = soup.find(id = ("ref" + str(x)))
    target_state = temp_soup.find(class_="h1").text.strip()
    cities = temp_soup.find(class_="topic-list").find_all("a")
    for a in range(len(cities)):
        cities[a] = cities[a].text.strip()
        path = os.getcwd() + "\Artist and Genre\\" + target_state
        try:
            start = time.time()
            artists = set()
            class1 = FindArtists_wiki(cities[a], target_state)
            artists = class1.findArtistsByLocation()

            class2 = ArtistGenre(artists)
            genre_info = (class2.getAllArtistsGenre())
            """for artist_x in genre_info:
                # write line to the file with name of the city"""


            end = time.time()
            # prints when city is done to console
            print(cities[a] + ", " + target_state + ":   Genre Search Time: " + str(end - start) + " for " + str(len(artists)) + " results")
        except:
            print(cities[a] + ", " + target_state + " does not have a page")
            pass

    x += 1

