from find_artists import FindArtists_wiki
from artist_genre import ArtistGenre

cities = ["Harrisburg"]
states = ["Pennsylvania"]

artists = set()
for i in range(len(cities)):
    try:
        class1 = FindArtists_wiki(cities[i], states[i])
        artists = class1.findArtistsByLocation()
    except:
        print ("Bad Parameters Caught")

    class2 = ArtistGenre(artists)
    class2.getAllArtistsGenre()


print("There are " + str(len(artists)) + " search results")



















"""

import os
import requests
from bs4 import BeautifulSoup
#state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]


path = os.getcwd()+"\Artist and Genre\\"
try:
    os.makedirs(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

#print ("The current working directory is %s" % path)

response = requests.get(
    url=("https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068"),
)
soup = BeautifulSoup(response.content, 'html.parser')
soup = soup.find(class_ = "topic-content col-sm pr-lg-60")
print (soup)
x = 326620
while (x<=326669):
    x += 1
"""
