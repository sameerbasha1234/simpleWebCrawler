import requests
from lxml.html import fromstring

class Spider:
	def __init__(self):
		self.xpathString = ""
		self.targetUrl = ""
		self.storage = None
	
	def GetTargetUrl(self,url):
		self.targetUrl = url
		print("\nTarget lock-on: \n[> " + self.targetUrl + " <]\n")
		return self.GetHtmlSource()

	def GetXPath(self,xpath):
		self.xpathString = xpath
		print("Got it!\n")

	def GetHtmlSource(self):
		print("Sending request...\n")
		res = requests.get(self.targetUrl,verify=False)
		if int(res.status_code) == 200:
			print("Success! Now we have the responde from server\n")
			print("#"*10 + "\n")
			print("Extracting source code...\n")
			self.spiderDent = fromstring(res.text)
		else:
			print("Error - HTTP " + str(res.status_code))
			print("Please check your URL")
			print ("Read README.txt for more detail\n")

	def XpathResult(self,string):
		try:
			res = self.spiderDent.xpath(string)
		except:
			print ("Error. Please check your xpath")
			print ("Read README.txt for more detail\n")
		return res[0]
	
	def DisplayResult(self):
		print("Result: \n " + self.XpathResult(self.xpathString) + " \n")
		print("[END]===============================================\n")


