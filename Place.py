##Place Object

from Point import Point
from LocationManager import LocationManager

class Place:

 	def __init__(self, dictionary):
 		#print dictionary
 		self.idNumber = dictionary['id']
 		#self.name = dictionary['name']
 		self.typeName = dictionary['type']
 		self.location = Point(dictionary['location'])
 		self.logicalLocation = LocationManager.locationForIDAndPoint(self.idNumber, self.location)
 		

