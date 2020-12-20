"""
DJ Kovarik
12/16/2020
Class will get the genres of all artists from the cities/states given using FindArtists class
"""

import requests
from bs4 import BeautifulSoup
import time
from spotify_client import SpotifyClient
from spotify_client import SpotifyException


class ArtistGenre:
    def __init__(self, artists):
        self.artists = artists

    def getAllArtistsGenre(self):
        all_info = []
        for i in self.artists:
            complete_data = []
            altMethodUsed = False
            obscureArtist = False

            artLink = i
            for x in range(len(artLink)):
                if artLink[x:x + 1] == " ":
                    artLink = artLink[0:x] + "_" + artLink[x + 1:len(artLink)]

            response = requests.get(
                url=("https://en.wikipedia.org/wiki/" + artLink),
            )
            soup = BeautifulSoup(response.content, 'html.parser')
            data = None
            soup_all_tr = None
            check_for_genre = False
            try:
                soup_all_tr = soup.find(class_="infobox vcard plainlist").find_all("tr")
            except:
                try:
                    soup_all_tr = soup.find(class_="infobox biography vcard").find_all("tr")
                except:
                    try:
                        altMethodUsed = True
                        complete_data = self.getArtistGenreFromSpotify(i)
                        if len(complete_data) == 0:
                            obscureArtist = True
                            #print (i + ":   ERROR- genre not on wiki or spotify")
                    except SpotifyException:
                        #print (i + ":   not on spotify")
                        continue
                    #print(i + ":   ERROR- no sidebar to get genres from")

            if altMethodUsed == False:
                for x in soup_all_tr:
                    try:
                        if x.find(scope="row").text.strip() == "Genres":
                            data = x.find_all("a")

                            if len(data) == 0:
                                data = x.find_all("td")

                            if len(data) != 0:
                                check_for_genre = True
                            else:
                                print(i + ":   somehow there is a genre category in the sidebar but no genres are showing up??? (Rare)")
                                pass
                            break
                    except:
                        pass

            if check_for_genre == False:
                if altMethodUsed == False:
                    altMethodUsed = True
                    try:
                        complete_data = self.getArtistGenreFromSpotify(i)
                        if len(complete_data) == 0:
                            obscureArtist = True
                            #print(i + ":   ERROR- genre not on wiki or spotify")
                    except SpotifyException:
                        #print (i + ":   not on spotify")
                        continue
                    #print(i + ":   ERROR- sidebar is there, but there is no genre info")
            else:
                for x in range(len(data)):
                    # issue shows pop as pop music, change from title to the actual text somehow
                    try:
                        complete_data.append(data[x].attrs['title'])
                    except:
                        pass

                    if len(complete_data) == 0:
                        temp = data[x].text.strip()
                        while "," in temp:
                            complete_data.append(temp[0:temp.find(",")])
                            temp = temp[temp.find(",") + 2:len(temp)]
                        complete_data.append(temp)
                        # print (i + ":   genres info was not formatted to hyperlinks in wikipedia")

            """if altMethodUsed == True:
                print(i + ":   Via Spotify- " + str(complete_data))
            else:
                print(i + ":   Via Wiki- " + str(complete_data))"""
            all_info.append(i + ":" + str(complete_data))
        return all_info

    def getArtistGenreFromSpotify(self, artist):
        try_again = True
        if artist.find("(") != -1:
            artist = artist[0:artist.find("(") - 1]
        genres = []

        #added since spotify has errors for too many requests, but im not sure how what error that would be
        while try_again == True:
            try:
                try_again = False
                # get rid of wiki formatting if it is there
                spotClass = SpotifyClient("DJ?Does this do anything")
                # can through "bad search parameters" SpotifyException and needs to be caught when this called
                artist_id = spotClass.search_item(artist, "artist")
                artist_json_data = spotClass.get_artist(artist_id)
                for x in artist_json_data['genres']:
                    genres.append(x)
                return genres
            except SpotifyException:
                raise SpotifyException
            except:
                try_again = True
                print (artist + ":   getArtistGenreFromSpotify Error. Trying again in 3 seconds")
                time.sleep(3)



