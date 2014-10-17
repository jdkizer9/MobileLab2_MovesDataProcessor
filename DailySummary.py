##DailySummary

from datetime import date, datetime
from Segment import PlaceSegment, MoveSegment
from Point import Point
from LocationManager import LocationManager

class DailySummary(object):
	"""docstring for ClassName"""
	def __init__(self, dictionary):
		self.segmentsArray = []
		if 'segments' in dictionary and dictionary['segments']:
			for segment in dictionary['segments']:
				if segment['type'] == 'move':
					self.segmentsArray.append(MoveSegment(segment))
				elif segment['type'] == 'place':
					self.segmentsArray.append(PlaceSegment(segment))

		self.date = datetime.strptime(dictionary['date'], '%Y%m%d').date()

		
	 	self.minAtPrimaryLocation = int(self.minutesAtPrimaryLocation())
	 	self.minAtSecondaryLocation = int(self.minutesAtSecondaryLocation())
	 	self.timeLeftPrimary = self.firstTimeLeftPrimaryLocation()
	 	self.timeReturnedPrimary = self.lastTimeArivedPrimaryLocation()
	 	self.geodiameter = self.computeGeodiameter()
	 	self.isWeekday = self.date.weekday() < 5
	 	#self.isAnomoly = False
	 	#self.explanation = ''

	def getPointsForToday(self):
		listOfpointLists = [segment.getPointsForDay(self.date) for segment in self.segmentsArray]
		pointList = []
		for listOfPoints in listOfpointLists:
			pointList = pointList + listOfPoints
		return pointList


	def placeSegments(self):
		return filter(lambda x: x.segmentType == 'place', self.segmentsArray)

	def placeSegmentsWithLogicalLocation(self, logicalLocation):
		return filter(lambda x: x.placeHasLogicalLocation(logicalLocation), self.placeSegments())

	def minutesAtLogicalLocation(self, logicalLocation):
		minutesArray = [placeSegment.minutesForDay(self.date) for placeSegment in self.placeSegmentsWithLogicalLocation(logicalLocation)]
		return sum(minutesArray)

	def minutesAtPrimaryLocation(self):
		return self.minutesAtLogicalLocation(LocationManager.primaryLogicalLocation)

	def firstTimeLeftPrimaryLocation(self):
		primaryPlaceSegments = self.placeSegmentsWithLogicalLocation(LocationManager.primaryLogicalLocation)
		if len(primaryPlaceSegments) > 0:
			return primaryPlaceSegments[0].endTime
		else:
			return None

	def lastTimeArivedPrimaryLocation(self):
		primaryPlaceSegments = self.placeSegmentsWithLogicalLocation(LocationManager.primaryLogicalLocation)
		if len(primaryPlaceSegments) > 0:
			return primaryPlaceSegments[-1].startTime
		else:
			return None

	def minutesAtSecondaryLocation(self):
		return self.minutesAtLogicalLocation(LocationManager.secondaryLogicalLocation)

	def computeGeodiameter(self):
		listOfPoints = self.getPointsForToday()
		maxDistance = 0.0
		for i in range(len(listOfPoints)):
			for j in range(i+1, len(listOfPoints)):
				point1 = listOfPoints[i]
				point2 = listOfPoints[j]
				distance = point1.distanceFromPoint(point2)
				if(distance > maxDistance):
					maxDistance = distance
		return maxDistance
		