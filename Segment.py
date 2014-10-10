##Segment Class

from Activity import Activity
from Place import Place
from datetime import datetime
from dateutil import parser

class Segment(object):
	def __init__(self, dictionary):
		#print 'In Segment Constructor'
		self.segmentType = dictionary['type']
		#print self.segmentType
		#print dictionary['startTime']
		#self.startTime = datetime.strptime(dictionary['startTime'], '%Y%m%dT%H%M%S%Z')
		self.startTime = parser.parse(dictionary['startTime'])
		#self.endTime = datetime.strptime(dictionary['endTime'], '%Y%m%dT%H%M%S%Z')
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

class PlaceSegment(Segment):
	"""docstring for PlaceSegment"""
	def __init__(self, dictionary):
		#print 'In Place Segment Constructor'
		super(PlaceSegment, self).__init__(dictionary)
		#print 'In Place Segment Constructor'
		#print dictionary['place']
		#print self.segmentType
		self.place = Place(dictionary['place'])

class MoveSegment(Segment):
	"""docstring for MoveSegment"""
	def __init__(self, dictionary):
		super(MoveSegment, self).__init__(dictionary)