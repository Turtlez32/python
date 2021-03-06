import sys, urllib2, json
import Utilities

def findStation(formData):
	
	stationTest = formData['stationName']
	stationList = stationTest.split(" ")
	
	stationTest = stationList[0]
	print stationTest
	
	requestHour = formData['timeHours']
	requestMinute = formData['timeMinutes']
	date = formData['date']
	ampmSelector = formData['AMPMSelector']
	dayOfWeek = formData['dayOfWeek']
	userName = formData['name']
	
	station = Utilities.CheckForTrainStation(stationTest)
	
	if len(station) == 0:
		print "Station Not Found"
		sys.exit()
	else:
		latitude = station[0]
		longitude = station[1]
		latitude = latitude[1:-1]
		longitude = longitude[1:-2]
		
	time = requestHour + ":" + requestMinute + ampmSelector
	
	urltime = Utilities.TimeToDate(time, date, dayOfWeek)
	
	weatherURL = Utilities.CreateLink(latitude, longitude, urltime)
	response = urllib2.urlopen(weatherURL);
	data = json.loads(response.read())
	
	timezone = data['timezone']
	currently = data['currently']
	summary = currently['summary']
	temperature = currently['temperature']
	realfeel = currently['apparentTemperature']
	
	try:
		preciptype = Utilities.JSONExtraction(data, "precipType")
		rainintensity = Utilities.JSONExtraction(data, "precipIntensity", "currently")
		rainprobability = Utilities.JSONExtraction(data, "precipProbability", "currently")
	except KeyError:
		preciptype = ""
		rainintensity = ""
		rainprobability = ""
	
	temperature = int((temperature - 32) * 5.0/9.0)
	realfeel = int((realfeel - 32) * 5.0/9.0)

	temperature = str(temperature)
	realfeel = str(realfeel)
	summary = str(summary)
	
	html = '<html> <head> </head> <body>'
	html += 'Hi '
	html += userName
	html += '<p>You have selected the station is: ' + stationTest
	html += '<p>The Current weather summary is: ' + summary
	html += '<table>'
	html += '<tr><td>Current Temp:</td><td>' + temperature + '</td></tr>'
	html += '<tr><td>Apparent Temp:</td><td>' + realfeel + '</td></tr>'
	html += '<tr><td>Rain Intensity:</td><td>' + rainintensity + '</tr><tr>'
	html += '<td>Rain Probability:</td><td>' + rainprobability + '</td></tr>'
	html += '</table>'
	
	return html