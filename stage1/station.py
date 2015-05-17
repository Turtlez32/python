# Importing System, Language Functions
import sys, urllib2, json, datetime
# Importing User Created Functions
import Utilities

# instantiate default values
arguments = []
station = []
urlTime = 1

# Generate the list of command line arguments
arguments = Utilities.CheckCommandLineArgs(sys.argv)

# Set up the station and find its location
#stationTest = arguments[0]
#time = arguments[-1]

if (len(arguments) == 1):
	stationTest = arguments[0]

if (len(arguments) == 2):
	stationTest = arguments[0]
	time = arguments[-1]
	urlTime = Utilities.TimeToDate(time)

if (len(arguments) == 6):
	stationTest = arguments[0]
	time = arguments[-1]
	dayint = arguments[1]
	days = arguments[2]
	daySpecifier = arguments[3]
	dayOfWeek = arguments[4]
	dayOfWeek = dayOfWeek.title()
	date = dayint + " " + days + " " + daySpecifier
	urlTime = Utilities.TimeToDate(time, date, dayOfWeek)

#station = CheckForTrainStation.CheckForTrainStation(stationTest)
station = Utilities.CheckForTrainStation(stationTest)

# Check the length of the list. if empty exit. If full continue
if len(station) == 0:
	print "Station Not Found"
	sys.exit()
else:
	latitude = station[0]
	longitude = station[1]

# Strip the quote marks from the latitude and longitude
latitude = latitude[1:-1]
longitude = longitude[1:-2]
#time = Utilities.TimeToDate(time)

# Create the URL for the weather API
weatherURL = Utilities.CreateLink(latitude, longitude, urlTime)

# save the response of the url JSON for later use
response = urllib2.urlopen(weatherURL);
data = json.loads(response.read())

#Top Level Data Collection
#timezone = data['timezone']
timezone = Utilities.JSONExtraction(data, "timezone")
currently = data['currently']

# Currently Data Collection
summary = Utilities.JSONExtraction(data, "summary", "currently")
requestdate = Utilities.JSONExtraction(data, "time", "currently")
temperature = Utilities.JSONExtraction(data, "temperature", "currently")
apprenttemp = Utilities.JSONExtraction(data, "apparentTemperature", "currently")

# Check there is a value for the Precipitation Type
# This value only exists if the intensity/probability
# is greater then 0
try:
	preciptype = Utilities.JSONExtraction(data, "precipType")
	rainintensity = Utilities.JSONExtraction(data, "precipIntensity", "currently")
	rainprobability = Utilities.JSONExtraction(data, "precipProbability", "currently")
except KeyError:
	preciptype = ""
	rainintensity = ""
	rainprobability = ""

# Convert decimal response into an integer
temperature = int(Utilities.ConvertToDegrees(temperature))
apprenttemp = int(Utilities.ConvertToDegrees(apprenttemp))

# set the summary time for the requested details.
summaryTime = datetime.datetime.fromtimestamp(int(requestdate)).strftime('%Y-%m-%d %H:%M:%S')

# print out the details for the user.
print "Request Date: " + summaryTime
print "The weather for the selected station :" + stationTest
print "Summary: " + summary
print "Rain Intensity: " + str(rainintensity) + " Rain Probability: " + str(rainprobability)
print "Precipitation Type: " + str(preciptype)
print "Temperature: " + str(temperature)
print "Apparent Temperature: " + str(apprenttemp)