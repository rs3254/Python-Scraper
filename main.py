
from handleRequests import get_url
from scrape import ScrapeClass
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re 
from writeToDB import wToMongo







mongo = wToMongo()
db = mongo.setConnection()







scraper = ScrapeClass()
headerCNBC = scraper.genericScrape('http://cnbc.com', " ")
headerBloomberg1 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__related-story-link')
headerBloomberg2 = scraper.genericScrape('https://bloomberg.com', '"story-package-module__story__headline-link')
headerBloomberg3 = scraper.genericScrape('https://bloomberg.com', 'single-story-module__headline-link')

mergedList = headerCNBC + headerBloomberg1 + headerBloomberg2 + headerBloomberg3


mongo.write(mergedList, db)




mongo.read(db)







