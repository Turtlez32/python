class StationArguments(object):

	def SetArguments(self, Args, count):
		if (count == 1):
			print "Program usage: "
			print "Stage1.py <stationName> <time>"
			print "Stage1.py <stationName> <date> <time>"
			print "<date> = {<int> days from <day>}"
			print "<days> = {Today, Tomorrow, Now, Monday-Sunday, Mon-Sun, \"Next Week\"}"
			sys.exit()
		elif (count == 3):
			self.SetStation(Args[1])
			self.SetTime(Args[-1])
		elif (count == 7):
			self.SetStation(Args[1])
			self.SetTime(Args[-1])
			self.SetDateInt(Args[1])
			self.SetDateString(Args[2])
			self.SetDateDay(Args[3])
			self.SetDayOfWeek(Args[4])
			self.SetDate()
	
	def SetDate(self):
		self.Date = self.GetDateInt() + " " + self.GetDateString() + " " + self.GetDateDay()
	
	def GetDate(self):
		return self.Date
	
	def SetStation(self, station):
		self.StationName = station
	
	def GetStation(self):
		return self.StationName
	
	def SetDateInt(self, int):
		self.DateInt = int
	
	def GetDateInt(self):
		return self.DateInt
	
	def SetDateString(self, datestring):
		self.DateString = datestring
	
	def GetDateString(self):
		return self.DateString
	
	def SetDateDay(self, dateday):
		self.DateDay = dateday
	
	def GetDateDay(self):
		return self.DateDay
	
	def SetDayOfWeek(self, weekday):
		self.DayOfWeek = weekday
	
	def GetDayOfWeek(self, ):
		return self.DayOfWeek
	
	def SetTime(self, time):
		self.Time = time
	
	def GetTime(self):
		return self.Time