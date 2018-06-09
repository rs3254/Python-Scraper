
from handleRequests import get_url
from bs4 import BeautifulSoup
import re 
import datetime
from pymongo import MongoClient



client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pymongo_test



# raw_html = handleRequests.get_url('https://bloomberg.com')
raw_html = get_url('https://bloomberg.com')
html = BeautifulSoup(raw_html, 'html.parser')
# print(html)

headers = html.find_all("a", class_='single-story-module__related-story-link')
headers2 = html.find_all("a", class_="story-package-module__story__headline-link")
headers3  = html.find_all("a", class_="single-story-module__headline-link")
headerArr = []; 


# posts = db.posts
# post_data = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))



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


for j in range(0, len(headerArr)):
	timeStamp = datetime.datetime.utcnow()
	headerString = re.sub(' +',' ',headerArr[j])
	dictionary[timeStamp] = headerString




# print(dictionary.values())

for j in dictionary:
	print(dictionary[j])

