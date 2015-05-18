#!/usr/bin/python

# this is suitable for a GET - it has no parameters
def initialPage(stop):	
	
	data = '<html><head><title>Demonstration of a webserver</title></head><body>\n'
	data += '<form action="http://127.0.0.1:43234/" method="POST">\n'
	data += '<label for="name">Name:</label>\n'
	data += '<input type="text" name="name" value="" size="" /><br>\n'
	data += '<label for="timeHours">Time Hours:</label>'
	data += '<input type="text" name="timeHours" value="" size="" /><br>\n'
	data += '<label for="timeMinutes">Time Minutes:</label>'
	data += '<input type="text" name="timeMinutes" value="" size="" /><br>\n'
	data += '<select name="stationName">'
	
	for s in stop:
		data += '<option value="'
		data += s
		data += '">'
		data += s
		data += '</option>'
		
	data += '</select>'
	data += '<select name="AMPMSelector">'
	data += '<option value="AM">AM</option>'
	data += '<option value="PM">PM</option>'
	data += '</select>'
	data += '<label for="date">Date:</label>'
	data += '<input type="text" name="date" value="" size="" /><br>\n'
	data += '<select name="dayOfWeek">'
	data += '<option value="Today">Today</option>'
	data += '<option value="Tomorrow">Tomorrow</option>'
	data += '<option value="Now">Now</option>'
	data += '<option value="Next Week">Next Week</option>'
	data += '<option value="Monday">Monday</option>'
	data += '<option value="Tuesday">Tuesday</option>'
	data += '<option value="Wednesday">Wednesday</option>'
	data += '<option value="Thursday">Thursday</option>'
	data += '<option value="Friday">Friday</option>'
	data += '<option value="Saturday">Saturday</option>'
	data += '<option value="Sunday">Sunday</option>'
	data += '</select>'
	data += '<input type="submit" value="Submit">\n'
	data += '</form>'
	data += '</body></html>'
	
	return data

# this is suitable for a POST - it has a single parameter which is 
# a dictionary of values from the web page form.

def respondToSubmit(formData):
	fieldNames = formData.keys()
	
	data = ""
	#for field in formData.fieldNames():
	#	data += "field is " + field + ", value is " + formData[field] + '<br>'

	for field in fieldNames:
		data += "field is " + field + ", value is " + formData[field] + '<br>'
	
	return data