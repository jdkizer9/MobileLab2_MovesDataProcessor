##Activity Class

from Point import TrackPoint
from dateutil import parser

def isPointInDay(point, day):
	return (point.timeStamp.date() == day)

class Activity:
	def __init__(self, dictionary):
		self.trackPointsArray = [TrackPoint(d) for d in dictionary['trackPoints']]
		self.startTime = parser.parse(dictionary['startTime'])
		self.endTime = parser.parse(dictionary['endTime'])

	def getPointsForDay(self, day):
		return [x for x in self.trackPointsArray if isPointInDay(x, day)]