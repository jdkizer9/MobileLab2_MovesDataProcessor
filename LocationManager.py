##LocationManager

from Point import Point

kRadius = .25
kPrimaryLocationID = -1
kSecondaryLocationID = -2

class LocationManagerClass(object):
	__instance = None
	def __init__(self, *args, **kwargs):
		print "LocationManager singleton instance"
		#self.klass = klass
		self.instance = None
		self.logicalPoints = []
		self.primaryLocationEquivalencyClass = {'point' : Point({'lat': 40.72539, 'lon' : -74.07099}), 'equivalencyID' : kPrimaryLocationID, 'idNumbers' : []}
		self.secondaryLocationEquivalencyClass = {'point' : Point({'lat': 40.74096, 'lon' : -74.00212}), 'equivalencyID' : kSecondaryLocationID, 'idNumbers' : []}
		self.otherLocations = []

	def __call__(self, *args, **kwargs):

		print "In Call Method"
		# if self.instance is None:
		# 	self.instance = self.__init__(*args, **kwargs)

		#print self.instance
		return self.instance

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

#class LocationManager:
	# def __init__(self):
	# 	print "LocationManager singleton instance"
	# 	self.klass = klass
	# 	self.instance = None
	# 	self.logicalPoints = []

	# 	self.primaryLocationEquivalencyClass = {'point' : Point(40.72539, -74.07099), 'equivalencyID' : kPrimaryLocationID, 'idNumbers' : []}
	# 	self.secondaryLocationEquivalencyClass = {'point' : Point(40.72539, -74.07099), 'equivalencyID' : kSecondaryLocationID, 'idNumbers' : []}
	# 	self.otherLocations = []
	# 	Point(40.74096, -74.00212)

	# def __call__(self):

	# 	if self.instance is None:
	# 		self.instance = self.klass()

	# 	return self.instance

	# def locationForIDAndPoint(self, locationID, point):
	# 	if point.distanceFromPoint(self.primaryLocation) < kRadius:
	# 		self.primaryLocationEquivalencyClass['idNumbers'].append(locationID)
	# 		return self.primaryLocationEquivalencyClass['equivalencyID']
	# 	elif point.distanceFromPoint(self.secondaryLocation) < kRadius:
	# 		self.secondaryLocationEquivalencyClass['idNumbers'].append(locationID)
	# 		return self.secondaryLocationEquivalencyClass['equivalencyID']
	# 	else:
	# 		self.otherLocations.append(locationID)
	# 		return locationID