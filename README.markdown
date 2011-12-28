# twittercounter-py: 
#### simple wrapper for twittercounter.com API 
* adds the ability to pass API a user's screen name instead of ID
* uses tweepy to access twitter API
	
## Usage:
1. instantiate API
	
		import twittercounter
		
		api = twittercounter.API(api_key,{'consumer_key':consumer_key,'consumer_secret':consumer_secret})
  .. or:
		api = twittercounter.API(api_key)
		api.set_twitter_credentials(consumer_key,consumer_secret)
  or to just use ID's:
		api = twittercounter.API(api_key)
		
2. call_api passing a screen name (if twitter credentials provided) or user id
		
		data = api.call_api(user).data
		
		followers = data['followers_current']

## Dependencies:
* tweepy
* simplejson
* urllib,urllib2

		
	