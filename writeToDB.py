from pymongo import MongoClient
import re 
import datetime




class wToMongo:

	def cleanStr(self, stringVal):
		st = stringVal.strip()
		stringValue = st.replace('\n', "")
		return stringValue

	def write(arrForWrite, db):
		client = MongoClient()
		client = MongoClient('localhost', 27017)
		client.drop_database("database")
		db = client.database

		for j in range(0, len(arrForWrite)):
			headerString = re.sub(' +',' ',arrForWrite[j])
			dictionary["Headline"] = cleanStr(headerString)
			db.database.insert_one(dictionary)
			dictionary.clear()

	