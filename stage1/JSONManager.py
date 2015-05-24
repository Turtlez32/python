import urllib2, json
class JSONManager(object):

	def __init__(self, URL):
		try:
			self.SetResponseURL(URL)
		except None:
			print "JSON response returned empty string"
	
	def SetResponseURL(self, URL):
		self.JSONData = urllib2.urlopen(URL)
		self.JSONResponse = self.GetResponseFile(self.JSONData)
	
	def GetResponseFile(self, JSON):
		self.response = json.loads(JSON.read())
		return self.response
	
	def FindSection(self, Section):
		self.ReturnData = self.JSONResponse[Section]
		return self.ReturnData
		
	def FindSectionField(self, Field, Section):
		self.FieldData = Section[Field]
		return self.FieldData
	
	def FindField(self, Field):
		self.FieldData = self.JSONResponse[Field]
		return self.FieldData