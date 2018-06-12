from handleRequests import get_url
from bs4 import BeautifulSoup
import re

class ScrapeClass:
	

	def cleanStr(self, stringVal):
		st = stringVal.strip()
		stringV = st.replace('\n', "")
		return stringV


	def genericScrape(self, stringUrl, classUrl):
		rawHtml = get_url(stringUrl)
		html = BeautifulSoup(rawHtml, 'html.parser')
		headers = html.find_all("a", class_=classUrl)
		headerArr = []

		for j in headers:
			for z in j:
				newString = self.cleanStr(str(z))
				headerArr.append(newString)

		return headerArr


		

	def scrapeCNBC(self):
		cnbcHtml = get_url('http://cnbc.com')
		html = BeautifulSoup(cnbcHtml, 'html.parser')
		headers = html.find_all("a", class_=" ")
		headerArr = []

		for j in headers:
			for z in j:
				newString = self.cleanStr(str(z))
				headerArr.append(newString)


		return headerArr









