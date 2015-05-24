class CheckForTrainStation(object):
	
	def __init__(self):
		self.filename = 'google_transit/stops.txt'
		self.StationLocation = []
		self.StationDict = {}
		self.LongitudeDict = {}
		self.LatitudeDict = {}
		self.StationList = self.GetTrainData(self.filename)
		
	def GetTrainData(self, filename):
		self.index = 0001
	
		with open(filename, 'r') as f:
			for line in f:
				words = line.split(',')
				self.StationKey = words[1]
				self.StationValue = self.index
				self.StationDict = {self.StationKey:self.StationValue}
		
				self.LongitudeKey = self.index
				self.LongitudeValue = words[2]
				self.LongitudeDict = {self.LongitudeKey:self.LongitudeValue}
		
				self.LatitudeKey = self.index
				self.LatitudeVaue = words[3]
				self.LatitudeDict = {self.LatitudeKey:self.LongitudeValue}	
		
				self.index += 1
	
	def FindStation(self, station):
		if station in self.StationDict:
			Key = self.StationDict[station]
		
		if Key in self.LongitudeDict:
			self.Longitude = self.LongitudeDict[Value]
			print "Key: " + Key + " Not found in Dictionary LatitudeDict"
			
		if Key in self.LatitudeDict:
			self.Latitude = self.LatitudeDict[Value]
			print "Key: " + Key + " Not found in Dictionary LatitudeDict"
	
		self.StationLocation.append(Longitude)
		self.StationLocation.append(Latitude)
	
	def GetStation(self, station):
		self.LocationList = []
		self.LocationList = self.FindStation(station)
		
		return self.LocationList