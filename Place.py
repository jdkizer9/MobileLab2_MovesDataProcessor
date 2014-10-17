##Place Object

from Point import Point
from LocationManager import LocationManager

class Place:

 	def __init__(self, dictionary):
 		self.idNumber = dictionary['id']
 		self.typeName = dictionary['type']
 		self.location = Point(dictionary['location'])
 		self.logicalLocation = LocationManager.locationForIDAndPoint(self.idNumber, self.location)
 		