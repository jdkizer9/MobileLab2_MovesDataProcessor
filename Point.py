##Point Class

from datetime import datetime
import math
from dateutil import parser

class Point(object):
	def __init__(self, dictionary):
		self.latitude = dictionary['lat']
		self.longitude = dictionary['lon']

	#returns meters
	def distanceFromPoint(self, point):

		lat1 = self.latitude
		lat2 = point.latitude

		long1 = self.longitude
		long2 = point.longitude

		if((lat1 == lat2) and (long1 == long2)):
			return 0.0 

		degrees_to_radians = math.pi/180.0

		# phi = 90 - latitude
		phi1 = (90.0 - lat1)*degrees_to_radians
		phi2 = (90.0 - lat2)*degrees_to_radians

		# theta = longitude
		theta1 = long1*degrees_to_radians
		theta2 = long2*degrees_to_radians

		# Compute spherical distance from spherical coordinates.

		# For two locations in spherical coordinates
		# (1, theta, phi) and (1, theta, phi)
		# cosine( arc length ) =
		#    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
		# distance = rho * arc length

		cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
			math.cos(phi1)*math.cos(phi2))

		arc = math.acos( cos )

		# Remember to multiply arc by the radius of the earth
		# in your favorite set of units to get length.
		# MODIFIED TO return distance in miles
		#return arc*3960.0
		return arc*3960.0*1609.34

class TrackPoint(Point):
	def __init__(self, dictionary):
		super(TrackPoint, self).__init__(dictionary)
		dateTimeString = dictionary['time']
		#print(dateTimeString)
		self.timeStamp = parser.parse(dateTimeString)

	