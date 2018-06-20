
from scrape import ScrapeClass
from pymongo import MongoClient
import re 
from writeToDB import wToMongo
import markovify



mongo = wToMongo()
db = mongo.setConnection()





scraper = ScrapeClass()
headerCNBC = scraper.genericScrape('http://cnbc.com', " ", "CNBC")
headerBloomberg1 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__related-story-link', "BLOOMBERG")
headerBloomberg2 = scraper.genericScrape('https://bloomberg.com', 'story-package-module__story__headline-link', "BLOOMBERG")
headerBloomberg3 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__headline-link', "BLOOMBERG")
headersFT = scraper.genericScrape("http://ft.com", "js-teaser-heading-link", "FT")


mergedList = headerCNBC + headerBloomberg1 + headerBloomberg2 + headerBloomberg3 + headersFT

m = headerBloomberg1 + headerBloomberg2 + headerBloomberg3

# scraper.rawScrape("https://bloomberg.com")




mongo.write(mergedList, db)
# mongo.read(db)

compStr = mongo.createCompleteHeaderStr(db)

model = markovify.NewlineText(compStr)


for i in range(5):
	print(model.make_sentence())

