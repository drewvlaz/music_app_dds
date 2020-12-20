"""
DJ Kovarik
12/14/2020
Class will find artists from given city given the @param city. state
"""

import requests
from bs4 import BeautifulSoup

class FindArtists_wiki:
	def __init__(self, city:str, state:str):
		self.city = city
		self.state = state

	def __getAllNamesInPage(self, url_link:str):
		local_artists = set()

		response = requests.get(
			url = url_link,
		)
		soup = BeautifulSoup(response.content, 'html.parser')

		# recursion to search sub categories in page
		try:
			subCats_rawData = soup.find(id = "mw-subcategories").find_all("a")

			for x in subCats_rawData:
				result = x.attrs['href']
				#print("RECURSION USED:   " + result)
				temp_result = self.__getAllNamesInPage("https://en.wikipedia.org" + result)
				if temp_result != None:
					local_artists = local_artists | temp_result
				else:
					print ("There is a page in wiki with no artists in it for some reason")
		except AttributeError:
			pass

		# gets names in page
		try:
			artists_rawData = soup.find(id = "mw-pages").find(class_ = "mw-content-ltr").find_all("li")
			for x in artists_rawData:
				result = x.text.strip()

				# remove wiki sub-info on person
				"""if result.find("(") != -1:
					result = result[0:result.find("(") - 1]"""

				local_artists.add(result)

			return local_artists
		except AttributeError:
			#print("ERROR: invalid link----" + url_link)
			pass

	# public, @returns artists as a set
	def findArtistsByLocation(self):
		link1 = "https://en.wikipedia.org/wiki/Category:Musicians_from_" + self.city
		link2 = "https://en.wikipedia.org/wiki/Category:Musicians_from_" + self.city + ",_" + self.state

		artists = set()

		temp = self.__getAllNamesInPage(link2)
		if temp != None:
			artists = temp
		else:
			temp = self.__getAllNamesInPage(link1)
			if temp != None:
				artists = temp
			else:
				raise LinkException("InvalidParameters")

		"""artists = list(artists)
		artists.sort()

		for x in artists:
			print(x)
		print("There are " + str(len(artists)) + " search results")"""
		return artists


class LinkException(Exception):
	pass

