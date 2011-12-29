# Simple wrapper for the twitter counter api
# uses tweepy & twitter API to get user_id of a screenname
# returns a python dict via simplejson that contains data fields
# described here: http://twittercounter.com/pages/api
#
# usage: http://github.com/nickjacob/twittercounter-py
######
from urllib2 import HTTPError,Request,urlopen,URLError
from urllib import urlencode
from simplejson import load
import twitter

class API:
	"""
	arguments:
		api_key - twittercounter.com API key
	usage:
		instantiate API, call it 
	"""
	def __init__(self,api_key):
		self.api_key = api_key 
		self.TC_URL = 'http://api.twittercounter.com/'
		self.calls = {} # storage for calls
	
	def gen_id(self,screen_name):
		""" returns the user id from twitter, to simplify calls to api
		"""
		if isinstance(screen_name,int): return scree_name
		api = twitter.Api()
		try:
			name = api.GetUser(screen_name).id
		except:
			name = 0
		return name
	
	def call_api(self,user):
		""" makes an API call. takes user_id by default, can accept
			screen name twitter counter instance is passed a dict as twitter =
			doesn't make a new call if it's for the same screenname to reduce
			API calls.
		"""
		u_id = self.gen_id(user) # convert if necessary
		# minimize API calls - check if you already looked
		if str(u_id) in self.calls: 
			self.data = self.calls[str(u_id)]
			return 
		if u_id == 0: # is it a valid ID?
			self.data = {'Error':'invalid username'}
			return 
		# now call the API
		self.data = load(urlopen((self.TC_URL +'?'+urlencode({
			'apikey':self.api_key,
			'twitter_id':u_id
		}))))
		# an error in accessing twittercounter will result in data with an error.
		if 'Error' in self.data: 
			print 'Error in Accessing TwitterCounter API: '+self.data['Error']
		self.calls[str(u_id)] = self.data

	
	def get_followers(self,screen_name):
		"""
		example of a method to extend basic wrapper:
		returns a dict of followers yesterday & now
		"""
		self.call_api(screen_name) 
		return {'yesterday': self.data['followers_yesterday'],'now':self.data['followers_current']}
	
