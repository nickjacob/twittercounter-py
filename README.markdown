# twittercounter-py: 
	### simple wrapper for twittercounter.com API 
	### adds the ability to pass API a user's screen name instead of ID
	
## Usage:
	1. instantiate API
	
		import twittercounter
		
		api = twittercounter.API(api_key,{'consumer_key':your_key,'consumer_secret':consumer_secret})
		
	2. call_api passing a screen name (if twitter credentials provided) or user id
		
		data = api.call_api(user).data
		
		followers = data['followers_current']


		
	