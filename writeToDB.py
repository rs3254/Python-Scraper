from pymongo import MongoClient
import re 
import datetime




class wToMongo:

	def cleanStr(self, stringVal):
		st = stringVal.strip()
		newSt = st.replace('\n', "")
		return newSt




	def setConnection(self):
		client = MongoClient()
		client = MongoClient('localhost', 27017)
		client.drop_database("database")
		db = client.database
		return db



	def read(self, db):
		database = db.database.find()
		for item in database:
			print(item)
			# print(list(item.values())[1])





	def write(self, arrForWrite, db):
		dictionary = {}

		for j in range(0, len(arrForWrite)):
			headerString = re.sub(' +',' ',arrForWrite[j])
			dictionary["Headline"] = self.cleanStr(str(headerString))
			db.database.insert_one(dictionary)
			dictionary.clear()

	