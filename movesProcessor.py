
import json
from DailySummary import DailySummary
import csv as csv
import numpy as np
from datetime import time


def readJSON():
	f = open('Data/processed.json', 'r')
	jsonString = f.readline()
	#print jsonString
	f.close()
	jsonDict = json.loads(jsonString)
	return jsonDict

def rowArrayForDailySummary(dailySummary, isAnomoly, explanationString):
	dayString = dailySummary.date.isoformat()
	tahString = str(dailySummary.minAtPrimaryLocation)
	tawString = str(dailySummary.minAtSecondaryLocation)
	otString = 24*60 - (dailySummary.minAtPrimaryLocation + dailySummary.minAtSecondaryLocation)
	if dailySummary.timeLeftPrimary:
		tlhString = dailySummary.timeLeftPrimary.time().replace(second=0).isoformat()
	else:
		tlhString = ''

	if dailySummary.timeReturnedPrimary:
		trhString = dailySummary.timeReturnedPrimary.time().replace(second=0).isoformat()
	else:
		trhString = ''

	geoString = str(int(dailySummary.geodiameter))
	weekdayString = str(dailySummary.isWeekday)
	anomalyString = str(isAnomoly)

	rowArray = [dayString, tahString, tawString, otString, tlhString, trhString, geoString, weekdayString, anomalyString, explanationString]
	return rowArray

def minutesFromMidnightForTime(t):
	return int(t.hour * 60 + t.minute)

def isInRange(value, mean, std):

	if value > mean+2*std or value < mean-2*std:

		return False
	else:

		return True

def computeCSVForArrayOfDays(summaryArray, filename):
	
	#compute statistics for summaryArray
	timeAtHomeArray = [ds.minAtPrimaryLocation for ds in summaryArray]
	timeAtWorkArray = [ds.minAtSecondaryLocation for ds in summaryArray]
	otherTimeArray = [24*60 - (ds.minAtPrimaryLocation + ds.minAtSecondaryLocation) for ds in summaryArray]
	leftHomeArray = [(0 if ds.timeLeftPrimary is None else minutesFromMidnightForTime(ds.timeLeftPrimary.time())) for ds in summaryArray]
	arrivedHomeArray = [(0 if ds.timeReturnedPrimary is None else minutesFromMidnightForTime(ds.timeReturnedPrimary.time())) for ds in summaryArray]
	geodiameterArray = [ds.geodiameter for ds in summaryArray]

	featureArray = [timeAtHomeArray, timeAtWorkArray, otherTimeArray, leftHomeArray, arrivedHomeArray, geodiameterArray]
	meanArray = []
	varArray = []
	stdArray = []
	for feature in featureArray:
		meanArray.append(np.mean(feature)) 
		varArray.append(np.var(feature)) 
		stdArray.append(np.std(feature)) 

	#detect anomolies
	anomolyArray = []
	explanationArray = []
	for i in range(len(summaryArray)):
		ds = summaryArray[i]
		#print ds.date
		isAnomoly = False
		explanation = ''
		if not isInRange(timeAtHomeArray[i], meanArray[0], stdArray[0]):
			isAnomoly = True
			explanation = explanation + 'time@Home, '
			#print explanation

		if not isInRange(timeAtWorkArray[i], meanArray[1], stdArray[1]):
			isAnomoly = True
			explanation = explanation + 'time@CT, '
			#print explanation

		if not isInRange(otherTimeArray[i], meanArray[2], stdArray[2]):
			isAnomoly = True
			explanation = explanation + 'Other Time, '
			#print explanation

		if not isInRange(leftHomeArray[i], meanArray[3], stdArray[3]):
			isAnomoly = True
			explanation = explanation + 'Time Left Home, '
			#print explanation

		if not isInRange(arrivedHomeArray[i], meanArray[4], stdArray[4]):
			isAnomoly = True
			explanation = explanation + 'Time Arrived Home, '
			#print explanation

		if not isInRange(geodiameterArray[i], meanArray[5], stdArray[5]):
			isAnomoly = True
			explanation = explanation + 'Geodiameter, '
			#print explanation

		if not isAnomoly:
			explanation = 'n/a'
			#print explanation

		anomolyArray.append(isAnomoly)
		explanationArray.append(explanation)


	rowArray = []
	#append header
	headerArray = ['Day', 'Time At Home', 'Time At Cornell Tech', 'Other Time', 'Time Left Home', 'Time Back Home', 'Geodiameter', 'Weekday?', 'Anomaly?', 'Explanation']
	rowArray.append(headerArray)

	#append days
	for i in range(len(summaryArray)):
		rowArray.append(rowArrayForDailySummary(summaryArray[i], anomolyArray[i], explanationArray[i]))

	rowArray.append([])
	#append statistic summaries
	rowArray.append(['Mean'] + meanArray)
	rowArray.append(['Variance'] + varArray)
	rowArray.append(['Std Dev'] + stdArray)

	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(rowArray)



def main():

	dailyArray = readJSON()

	dailySummaryArray = [DailySummary(d) for d in dailyArray]
	weekdaySummaryArray = [d for d in dailySummaryArray if d.isWeekday]
	weekendSummaryArray = [d for d in dailySummaryArray if not d.isWeekday]

	computeCSVForArrayOfDays(dailySummaryArray, 'dailySummary.csv')
	computeCSVForArrayOfDays(weekdaySummaryArray, 'weekdaySummary.csv')
	computeCSVForArrayOfDays(weekendSummaryArray, 'weekendSummary.csv')

if __name__ == "__main__":
    main()