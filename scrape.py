from handleRequests import get_url
from bs4 import BeautifulSoup
import re

class ScrapeClass:
	

	# def cleanStr(self, stringVal):
	# 	st = stringVal.strip()
	# 	stringValue = st.replace('\n', "")
	# 	return stringValue


	def scrapeCNBC():
		cnbcHtml = get_url('http://cnbc.com')
		html = BeautifulSoup(cnbcHtml, 'html.parser')
		headers = html.find_all("a", class_=" ")
		headerArr = []

		for j in headers:
			for z in j:
				# newString = self.cleanStr(z)

				st = str(z).strip()
				stringValue = st.replace('\n', "")
				headerArr.append(stringValue)


		return headerArr







