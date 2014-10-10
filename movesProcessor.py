
import json
from DailySummary import DailySummary

def readJSON():
	f = open('Data/processed.json', 'r')
	jsonString = f.readline()
	#print jsonString
	f.close()
	jsonDict = json.loads(jsonString)
	return jsonDict



def main():

	dailyArray = readJSON()

	dailySummaryArray = [DailySummary(d) for d in dailyArray]
	i=1
	for dailySummary in dailySummaryArray:
	 	print dailySummary.geodiameter()
	 	print i
	 	i=i+1

if __name__ == "__main__":
    main()