##LocationManager

from Point import Point

kRadius = 400 #meters
kPrimaryLocationID = -1
kSecondaryLocationID = -2

class LocationManagerClass(object):
	def __init__(self, *args, **kwargs):
		self.logicalPoints = []
		self.primaryLogicalLocation = kPrimaryLocationID
		self.secondaryLogicalLocation = kSecondaryLocationID
		self.primaryLocationEquivalencyClass = {'point' : Point({'lat': 40.72539, 'lon' : -74.07099}), 'equivalencyID' : self.primaryLogicalLocation, 'idNumbers' : []}
		self.secondaryLocationEquivalencyClass = {'point' : Point({'lat': 40.74096, 'lon' : -74.00212}), 'equivalencyID' : self.secondaryLogicalLocation, 'idNumbers' : []}
		self.otherLocations = []

	def locationForIDAndPoint(self, locationID, point):
		if point.distanceFromPoint(self.primaryLocationEquivalencyClass['point']) < kRadius:
			self.primaryLocationEquivalencyClass['idNumbers'].append(locationID)
			return self.primaryLocationEquivalencyClass['equivalencyID']
		elif point.distanceFromPoint(self.secondaryLocationEquivalencyClass['point']) < kRadius:
			self.secondaryLocationEquivalencyClass['idNumbers'].append(locationID)
			return self.secondaryLocationEquivalencyClass['equivalencyID']
		else:
			self.otherLocations.append(locationID)
			return locationID


LocationManager = LocationManagerClass()