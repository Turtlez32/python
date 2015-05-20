#!/usr/bin/python
# specify a list of routes for each combination of incoming 
# request and request type (GET or POST).
# This should direct to a valid module::functionname
# functions that are associated with POST request types should 
# expect to get a single parameter - a dictionary full of values
# filled in from the original form

#--------------------------------
#def routes():
#	return (('get', '/', 'responders::initialPage'),      
#			('post', '/', 'station::returnsomething'),
#			('post', '/processRequest', 'station::returnsomething')
#			)
			
def routes():
	return (('get', '/', 'responders::initialPage'),      
			('post', '/', 'stage3::findStation'),
			('post', '/processRequest', 'stage3::findStation')
			)


	
	
