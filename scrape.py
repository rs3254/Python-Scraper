from handleRequests import get_url
from bs4 import BeautifulSoup
import re

class ScrapeClass:
	

	def cleanStr(self, stringVal):
		st = stringVal.strip()
		stringV = st.replace('\n', "")
		return stringV

	def createTupleList(self, header, website):
		tup = ()
		tupList = [] 
		for j in header:
			tup = (j,) + (website, )
			tupList.append(tup)
			tup = ()

		return tupList


	def genericScrape(self, stringUrl, classUrl, website):
		rawHtml = get_url(stringUrl)
		html = BeautifulSoup(rawHtml, 'html.parser')
		headers = html.find_all("a", class_=classUrl)
		headerArr = []

		for j in headers:
			for z in j:
				newString = self.cleanStr(str(z))
				headerArr.append(newString)

		return self.createTupleList(headerArr, website)


		
	def rawScrape(self, stringUrl):
		rawHtml = get_url(stringUrl)
		html = BeautifulSoup(rawHtml, 'html.parser')
		print(html)









