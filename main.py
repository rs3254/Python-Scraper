
from handleRequests import get_url
from scrape import ScrapeClass
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re 
from writeToDB import wToMongo





def cleanStr(stringVal):
	st = stringVal.strip()
	stringValue = st.replace('\n', "")
	return stringValue


def read():
	database = db.database.find()
	for item in database:
		print(item)
		# print(list(item.values())[1])



# def aggSum():

	


client = MongoClient()
client = MongoClient('localhost', 27017)

# Too Drop use below code -> clears out old values 
client.drop_database("database")
db = client.database





# raw_html = handleRequests.get_url('https://bloomberg.com')
raw_html = get_url('https://bloomberg.com')
html = BeautifulSoup(raw_html, 'html.parser')
# print(html)

headers = html.find_all("a", class_='single-story-module__related-story-link')
headers2 = html.find_all("a", class_="story-package-module__story__headline-link")
headers3  = html.find_all("a", class_="single-story-module__headline-link")
headerArr = []; 


dictionary = {}










for j in headers:
	for z in j:
		headerArr.append(z.rstrip())


for j in headers2:
	for z in j:
		headerArr.append(z.rstrip())

for j in headers3:
	for z in j:
		headerArr.append(z.rstrip())






headerCNBC = ScrapeClass.scrapeCNBC()


def write(arrForWrite):

	for j in range(0, len(arrForWrite)):
		headerString = re.sub(' +',' ',arrForWrite[j])
		dictionary["Headline"] = cleanStr(headerString)
		db.database.insert_one(dictionary)
		dictionary.clear()




write(headerArr)
write(headerCNBC)

read()









