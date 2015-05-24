# Importing System, Language Functions
import sys, urllib2, json, datetime
# Importing User Created Functions
import Utilities
import StationArguments
import JSONManager
import CheckForTrainStation

# instantiate default values
ArgvList = []
StationName = ""
StationLocation = []
LinuxTime = 1
count = len(sys.argv)

Station = StationArguments.StationArguments()
Station.SetArguments(sys.argv, count)

# Generate the list of command line arguments
#ArgvList = Utilities.CheckCommandLineArgs(sys.argv)

# Set up the station and find its location
#StationName = arguments[0]
#RequestTime = arguments[-1]

#if (len(ArgvList) == 1):
	#StationName = ArgvList[0]

if (count == 3):
	StationName = Station.GetStation()
	RequestTime = Station.GetTime()
	LinuxTime = Utilities.TimeToDate(RequestTime)

if (count == 7):
	StationName = Station.GetStation()
	RequestTime = Station.GetTime()
	dayint = Station.GetDateInt()
	days = Station.GetDateString()
	daySpecifier = Station.GetDateDay()
	dayOfWeek = Station.GetDayOfWeek()
	dayOfWeek = dayOfWeek.title()
	date = Station.GetDate()
	LinuxTime = Utilities.TimeToDate(RequestTime, date, dayOfWeek)

#station = CheckForTrainStation.CheckForTrainStation(StationName)
StationLocation = Utilities.CheckForTrainStation(StationName)

# Check the length of the list. if empty exit. If full continue
if len(StationLocation) == 0:
	print "Station Not Found"
	sys.exit()
else:
	latitude = StationLocation[0]
	longitude = StationLocation[1]

# Strip the quote marks from the latitude and longitude
latitude = latitude[1:-1]
longitude = longitude[1:-2]
#RequestTime = Utilities.TimeToDate(RequestTime)

# Create the URL for the weather API
weatherURL = Utilities.CreateLink(latitude, longitude, LinuxTime)

# save the response of the url JSON for later use
JSON = JSONManager.JSONManager(weatherURL)

timezone = JSON.FindField("timezone")
currently = JSON.FindSection("currently")
#response = urllib2.urlopen(weatherURL);
#data = json.loads(response.read())

#Top Level Data Collection
#timezone = data['timezone']
#timezone = UtilitiesNew.JSONExtraction(data, "timezone")
#currently = data['currently']

# Currently Data Collection
#summary = UtilitiesNew.JSONExtraction(data, "summary", "currently")
#requestdate = UtilitiesNew.JSONExtraction(data, "time", "currently")
#temperature = UtilitiesNew.JSONExtraction(data, "temperature", "currently")
#apprenttemp = UtilitiesNew.JSONExtraction(data, "apparentTemperature", "currently")

summary = JSON.FindSectionField("summary", currently)
requestdate = JSON.FindSectionField("time", currently)
temperature = JSON.FindSectionField("temperature", currently)
apparentTemperature = JSON.FindSectionField("apparentTemperature", currently)

# Check there is a value for the Precipitation Type
# This value only exists if the intensity/probability
# is greater then 0
#try:
#	preciptype = UtilitiesNew.JSONExtraction(data, "precipType")
#	rainintensity = UtilitiesNew.JSONExtraction(data, "precipIntensity", "currently")
#	rainprobability = UtilitiesNew.JSONExtraction(data, "precipProbability", "currently")
#except KeyError:
#	preciptype = ""
#	rainintensity = ""
#	rainprobability = ""

try:
	preciptype = JSON.FindSectionField("precipType", currently)
	rainintensity = JSON.FindSectionField("precipIntensity", currently)
	rainprobability = JSON.FindSectionField("precipProbability", currently)
except KeyError:
	preciptype = ""
	rainintensity = ""
	rainprobability = ""

# Convert decimal response into an integer
temperature = int(Utilities.ConvertToDegrees(temperature))
apparentTemperature = int(Utilities.ConvertToDegrees(apparentTemperature))

# set the summary time for the requested details.
summaryTime = datetime.datetime.fromtimestamp(int(requestdate)).strftime('%Y-%m-%d %H:%M:%S')

# print out the details for the user.
print "Request Date: " + summaryTime
print "The weather for the selected station :" + StationName
print "Summary: " + summary
print "Rain Intensity: " + str(rainintensity) + " Rain Probability: " + str(rainprobability)
print "Precipitation Type: " + str(preciptype)
print "Temperature: " + str(temperature)
print "Apparent Temperature: " + str(apparentTemperature)