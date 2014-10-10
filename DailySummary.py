##DailySummary

from datetime import date, datetime
from Segment import PlaceSegment, MoveSegment
from Point import Point

class DailySummary():
	"""docstring for ClassName"""
	def __init__(self, dictionary):
		
		#print dictionary
		self.segmentsArray = []
		if dictionary['segments']:
			for segment in dictionary['segments']:
				if segment['type'] == 'move':
					self.segmentsArray.append(MoveSegment(segment))
				elif segment['type'] == 'place':
					self.segmentsArray.append(PlaceSegment(segment))

		#print dictionary['date']
		self.date = datetime.strptime(dictionary['date'], '%Y%m%d').date()

	def getPointsForToday(self):
		listOfpointLists = [segment.getPointsForDay(self.date) for segment in self.segmentsArray]
		pointList = []
		for listOfPoints in listOfpointLists:
			pointList = pointList + listOfPoints
		return pointList

	def geodiameter(self):
		listOfPoints = self.getPointsForToday()
		maxDistance = 0.0
		print len(listOfPoints)
		for i in range(len(listOfPoints)):
			for j in range(i+1, len(listOfPoints)):
				point1 = listOfPoints[i]
				point2 = listOfPoints[j]
				distance = point1.distanceFromPoint(point2)
				if(distance > maxDistance):
					maxDistance = distance
		print maxDistance
		return maxDistance
		