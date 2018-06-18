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
		count = 0
		database = db.database.find()
		for item in database:
			print(item)
			count += 1

		print("\n")
		print("count ->", count)



	def checkDuplicates(self, db, headline):
		arr  = [] 
		data = db.database.find()
		for j in data:
			arr.append(list(j.values())[1][0])
			# print(list(j.values())[1][0])

		if headline in arr:
			return True
		else:
			return False


	def write(self, arrForWrite, db):
		dictionary = {}
		
		# arr = self.checkDuplicates(db)
		for j in range(0, len(arrForWrite)):
			tup = ()
			headerString = re.sub(' +',' ',arrForWrite[j][0])
			sourceString = arrForWrite[j][1]
			tup = (self.cleanStr(str(headerString)), ) + (sourceString, )
			dictionary["Headline"] = tup
			# print(dictionary["Headline"])
			if dictionary["Headline"][0] == "":
				continue
			elif "span class" in dictionary["Headline"][0]:
				continue
			else:
				if self.checkDuplicates(db, dictionary["Headline"][0]):
					continue
				else:
					db.database.insert_one(dictionary)
					dictionary.clear()
					tup = ()

	