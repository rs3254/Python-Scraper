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
		# client.drop_database("database")
		db = client.database
		return db



	def read(self, db):
		database = db.database.find()
		for item in database:
			print(item)



	def checkDuplicates(self, db, headline):
		arr  = [] 
		data = db.database.find()
		for j in data:
			arr.append(list(j.values())[1])


		if headline in arr:
			return True
		else:
			return False


	def write(self, arrForWrite, db):
		dictionary = {}
		# arr = self.checkDuplicates(db)
		for j in range(0, len(arrForWrite)):
			headerString = re.sub(' +',' ',arrForWrite[j])
			dictionary["Headline"] = self.cleanStr(str(headerString))
			if dictionary["Headline"] == "":
				continue
			elif "span class" in dictionary["Headline"]:
				continue
			else:
				if self.checkDuplicates(db, dictionary["Headline"]):
					continue
				else:
					db.database.insert_one(dictionary)
					dictionary.clear()

	