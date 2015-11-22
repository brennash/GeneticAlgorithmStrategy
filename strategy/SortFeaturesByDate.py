import json

class SortFeaturesByDate:

	def __init__(self, filename):
		
		self.jsonList = []

		file = open(filename, "r")
		for line in file:
			jsonDict = json.loads(line.rstrip())
			jsonList.append(jsonDict)
		

		newlist = sorted(jsonList, key=lambda x: self.getDateAsYYYYMMDD(x['Date']), reverse=True)

	def getDateAsYYYYMMDD(self, jsonDict)
		dateStr = jsonDict['Date']
		day, month, year = (str(x) for x in dateStr.split('/'))
		if len(year) == 2:
			year = '20'+year

		dateYYYYMMDD = int(year+month+day)
		return dateYYYYMMDD
