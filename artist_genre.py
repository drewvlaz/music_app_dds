"""
DJ Kovarik
12/16/2020
Class will get the genres of all artists from the cities/states given using FindArtists class
"""

import requests
from bs4 import BeautifulSoup
import time

class ArtistGenre:
    def __init__(self, artists):
        self.artists = artists

    def getAllArtistsGenre(self):
        start = time.time()
        for i in self.artists:
            artLink = i

            for x in range(len(artLink)):
                if artLink[x:x+1] == " ":
                    artLink = artLink[0:x] + "_" + artLink[x+1:len(artLink)]

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
                    #print(i + ":   ERROR- no sidebar to get genres from")
                    continue


            for x in soup_all_tr:
                try:
                    if x.find(scope="row").text.strip() == "Genres":
                        data = x.find_all("a")

                        if len(data) == 0:
                            data = x.find_all("td")

                        if len(data) != 0:
                            check_for_genre = True
                        else:
                            #print(i + ":   somehow there is a genre category in the sidebar but no genres are showing up??? (Rare)")
                            pass
                        break
                except:
                    pass

            complete_data = []
            if check_for_genre == False:
                #print(i + ":   ERROR- sidebar is there, but there is no genre info")
                continue
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
                            temp = temp[temp.find(",")+2:len(temp)]
                        complete_data.append (temp)
                        #print (i + ":   genres info was not formatted to hyperlinks in wikipedia")



            print (i + "   " + str(complete_data))



        end = time.time()
        print("Wiki Search Time: " + str(end - start) + " for " + str(len(self.artists)) + " results")