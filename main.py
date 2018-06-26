
from scrape import ScrapeClass
from pymongo import MongoClient
import re 
from writeToDB import wToMongo
import markovify
import language_check
import pprint


pp = pprint.PrettyPrinter(indent=4)
mongo = wToMongo()
db = mongo.setConnection()

tool = language_check.LanguageTool('en-US')



scraper = ScrapeClass()
headerCNBC = scraper.genericScrape('http://cnbc.com', " ", "CNBC")
headerBloomberg1 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__related-story-link', "BLOOMBERG")
headerBloomberg2 = scraper.genericScrape('https://bloomberg.com', 'story-package-module__story__headline-link', "BLOOMBERG")
headerBloomberg3 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__headline-link', "BLOOMBERG")
headersFT = scraper.genericScrape("http://ft.com", "js-teaser-heading-link", "FT")


mergedList = headerCNBC + headerBloomberg1 + headerBloomberg2 + headerBloomberg3 + headersFT

m = headerBloomberg1 + headerBloomberg2 + headerBloomberg3


# mongo.write(mergedList, db)
# mongo.read(db)

compStr = mongo.createCompleteHeaderStr(db)

model = markovify.NewlineText(compStr)


def genOutput(value):
	i = 0
	while i < value:
		outPutStr = model.make_sentence(tries=100)

		if len(outPutStr) < 40:
			i += 1
			matches = tool.check(outPutStr)
			if len(matches) > 0:
				m = list(matches[0])[6]
				if m == "Possible spelling mistake found":
					i -= 1
					continue
				elif m == "Comparison requires 'than', not 'then' nor 'as'.":
					print(outPutStr, len(outPutStr))

				else:
					i -= 1
					continue 
			else:
				print(outPutStr, len(outPutStr))

		else:
			continue 





genOutput(20)




