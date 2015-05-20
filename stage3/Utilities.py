import datetime
import time
import re
from PIL import Image, ImageDraw, ImageFont

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
	
def CheckDate(argument):

	type = FindVariableType(argument)
	today = time.strftime("%w")

	print time.strftime("%A")
	
	if (type == "INT"):
		return argument
	
	if (type == "STR"):
		if (argument == "now" or argument == "Now"):
			now = time.strftime("%x")
			return now
		
		if (argument == "Today" or argument == "today"):
			now = time.strftime("%x")
			return now
			
		if (argument == "Tomorrow" or argument == "tomorrow"):
			now = datetime.date.today() + datetime.timedelta(days=1)
			return now
			
		if (argument == "Next Week" or argument == "next week"):
			now = datetime.date.today() + datetime.timedelta(days=7)
			return now
		
		#if (argument == "Monday" or argument == "monday"):
		#if (argument == "Tuesday" or argument == "tuesdayday"):
		#if (argument == "Wednesday" or argument == "wednesday"):
		#if (argument == "Thursday" or argument == "thursday"):
		#if (argument == "Friday" or argument == "friday"):
		#if (argument == "Saturday" or argument == "saturday"):
		#if (argument == "Sunday" or argument == "sunday"):
			
		if (argument == "days" or argument == "Days"):
			print "Provided a days"

def TimeToDate(argument, day_specifier="", day_of_week="", ):

	dayargs = {"Today":9,"Tomorrow":8,"Now":7,"Monday":1,"Tuesday":2,"Wednesday":3,
	           "Thursday":4,"Friday":5,"Saturday":6,"Sunday":0,"Next Week":10}
	
	if day_of_week in dayargs:
		day = dayargs[day_of_week]
		daycount = day_specifier
		weatherdate = CorrectDate(day, daycount)
	else: 
		weatherdate = datetime.datetime.today()

	current = weatherdate
	urlmin = argument[-4:-2]
	ampm = argument[-2]
	
	if (ampm == "P"):
		pm = True
	else:
		pm = False
		
	urlhour = int(argument[0])
		
	if (pm == True and urlhour < 10):
		urlhour += 12

	urlhour = int(urlhour)
	urlmin = int(urlmin)
	
	urldate = current.replace(hour=urlhour, minute=urlmin)
	
	urldate = time.mktime(urldate.timetuple())
	
	return int(urldate)
	
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
	
def ListTrainStops():

	stops = []
	
	with open('google_transit/stops.txt', 'r') as f:
		for line in f:
			words = line.split(',')
			
			if (words[1] != "stop_name"):
				stop = words[1]
				stop = stop[1:-1]
				stops.append(stop)
			
	return stops

def ImageDisplay(trainStop):
	filename = 'assets/trainrescale2.png'

	original = Image.open(filename).convert('RGBA')
	original.load()
	
	with open('assets/ImageStopLocation.txt', 'r') as f:
		for line in f:
			words = line.split(',')
			
			if trainStop in words[0]:
				xMin = words[1]
				yMin = words[2]
				xMax = words[3]
				yMax = words[4]

		topLeft = round(float(xMin))
		topLeft = int(topLeft) * 2
		
		bottomLeft = round(float(yMin))
		bottomLeft = int(bottomLeft) * 2
		
		topRight = round(float(xMax))
		topRight = int(topRight) * 2
		
		bottomRight = round(float(yMax))
		bottomRight = int(bottomRight) * 2
	
	draw = ImageDraw.Draw(original)
	# diagonal line from top left to bottom right


	draw.rectangle([(topLeft,bottomLeft),(topRight,bottomRight)],fill=None,outline="Green")

	# diagonal line from top right to bottom left
	#draw.line((0, original.size[1], original.size[0], 0), fill=0)
	del draw

	original.save("assets/highlighted" + ".png")
	
	outputFile = "highlighted.png"
	return outputFile