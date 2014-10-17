##Segment Class

from Activity import Activity
from Place import Place
from datetime import datetime, time
from dateutil import parser

class Segment(object):
	def __init__(self, dictionary):
		self.segmentType = dictionary['type']
		self.startTime = parser.parse(dictionary['startTime'])
		self.endTime = parser.parse(dictionary['endTime'])

		if 'activities' in dictionary:
			self.activitiesArray = [Activity(d) for d in dictionary['activities']]
		else:
			self.activitiesArray = []

	def getPointsForDay(self, day):
		#TODO - how to do nested list comprehensions??
		listOfpointLists = [activity.getPointsForDay(day) for activity in self.activitiesArray]
		pointList = []
		for listOfPoints in listOfpointLists:
			pointList = pointList + listOfPoints
		return pointList

	def minutesForDay(self, day):
		startTime = self.startTime
		endTime = self.endTime

		#the start time for this segment occurred before today
		#set startTime to be the beginning of today
		if startTime.date() < day:
			startTime = datetime.combine(day, time(tzinfo=self.startTime.tzinfo))

		if endTime.date() > day:
			endTime = datetime.combine(day, time(hour=23, minute=59, second=59, tzinfo=self.endTime.tzinfo))

		timeDelta = endTime - startTime
		return timeDelta.total_seconds()/60.0

class PlaceSegment(Segment):
	"""docstring for PlaceSegment"""
	def __init__(self, dictionary):
		super(PlaceSegment, self).__init__(dictionary)
		self.place = Place(dictionary['place'])

	def placeHasLogicalLocation(self, logicalLocation):
		return self.place.logicalLocation == logicalLocation

class MoveSegment(Segment):
	"""docstring for MoveSegment"""
	def __init__(self, dictionary):
		super(MoveSegment, self).__init__(dictionary)