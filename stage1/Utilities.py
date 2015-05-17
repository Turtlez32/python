import datetime
import time

def CreateLink(latitude, longitude, time):
	weatherAPIKey = "c9e875d725582efa9fcacefd0fc186f8/"
	url = "https://api.forecast.io/forecast/"
	
	stationLink = url + weatherAPIKey + latitude + "," + longitude + "," + str(time)
	
	return stationLink

def FindVariableType(var):
	if (isinstance(var, int)):
		return "INT"
	
	if (isinstance(var, basestring)):
		return "STR"
	
def CheckForTrainStation(station):

	#f = open('stops.txt', 'r')
	stationLocation = []
	
	with open('google_transit/stops.txt', 'r') as f:
		for line in f:
			words = line.split(',')

			if station in words[1]:
				stationLocation.append(words[2])
				stationLocation.append(words[3])
				
	return stationLocation
	
def TimeToDate(argument, day_specifier="", day_of_week="", ):

	dayargs = {"Today":9,"Tomorrow":8,"Now":7,"Monday":1,"Tuesday":2,"Wednesday":3,
	           "Thursday":4,"Friday":5,"Saturday":6,"Sunday":0,"Next Week":10}
	
	if day_of_week in dayargs:
		day = dayargs[day_of_week]
		daycount = day_specifier[0]
		weatherdate = CorrectDate(day, daycount)
	else: 
		weatherdate = datetime.datetime.today()

	current = weatherdate
	urlmin = int(argument[-4:-2])
	ampm = argument[-2]
	
	if (ampm == "p"):
		pm = True
		
	urlhour = int(argument[0])
		
	if (pm == True and urlhour < 10):
		urlhour += 12	

	urlhour = int(urlhour)
	urlmin = int(urlmin)
	
	urldate = current.replace(hour=urlhour, minute=urlmin)
	
	urldate = time.mktime(urldate.timetuple())
	
	return int(urldate)

def CheckCommandLineArgs(argv):
	
	argvCount = len(argv)
	argvList = []
	
	if (argvCount < 2):
		print "Please ensure you enter at least 2 command line items"
		print argv[0] + "<station> {<date>} <time>"
	
	if (argvCount == 2):
		argvList.append(argv[1])
	
	if (argvCount == 3):
		argvList.append(argv[1])
		argvList.append(argv[2])
	
	if (argvCount == 4):
		argvList.append(argv[1])
		argvList.append(argv[2])
		argvList.append(argv[3])
	
	if (argvCount == 7):
		argvList.append(argv[1])
		argvList.append(argv[2])
		argvList.append(argv[3])
		argvList.append(argv[4])
		argvList.append(argv[5])
		argvList.append(argv[6])
		
	return argvList
	
def CorrectDate(day, daycount):

	if (day == 0):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 1):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 2):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 3):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 4):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 5):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 6):
		# Find out today, and find its number
		today = datetime.datetime.today()
		todayday = int(today.strftime('%w'))
		
		# Work out how far to advance from today
		advance = day - todayday
		
		# Progress time based on the advance delta time
		delta = datetime.timedelta(days=advance)
		advdate = today + delta
		
		# Now progress the input days as per the user input
		inputadvance = datetime.timedelta(days=int(daycount))
		
		# date = the current date to check for weather
		date = advdate + inputadvance
		
		return date
		
	if (day == 7):
		today = datetime.datetime.now()
		return today
		
	if (day == 8):
		delta = datetime.timedelta(days=1)
		today = datetime.datetime.today()
		inputadvance = datetime.timedelta(days=int(daycount))
		tomorrow = today + delta
		
		date = tomorrow + inputadvance
		return date
	
	if (day == 9):
		today = datetime.datetime.now()
		inputadvance = datetime.timedelta(days=int(daycount))
		today = today + inputadvance
		return today
		
	if (day == 10):
		delta = datetime.timedelta(days=7)
		today = datetime.datetime.today()
		inputadvance = datetime.timedelta(days=int(daycount))
		
		date = today + delta + inputadvance
		
		return date
		
def ConvertToDegrees(temp):
	temp = temp - 32
	temp = temp * 5/9
	
	return temp
	
def JSONExtraction(JSON, Field, Section=""):

	if (Section == ""):
		data = JSON[Field]
	else:
		section = JSON[Section]
		data = section[Field]
	
	return data