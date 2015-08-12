import twitter
def fetch_tweets(handle,num):
	statuses = api.GetUserTimeline(screen_name=handle)
	#print [s.text for s in statuses]
	tweet_file=open('tweets.db','w')
	for i in range(num):
		tweet_file.write(statuses[i].text.encode('utf-8')+"\n\n")
		print statuses[i].text + "\n\n"
	tweet_file.close()

def fetch_followers(handle):
	followers = api.GetFriendIDs(screen_name= handle,cursor=-1)
	for i in followers:
		users = api.GetUser(i)
		user_d = users.AsDict()
		print user_d['name']

consumer_key1 = raw_input("Enter your Consumer key\n")
consumer_secret1 = raw_input("Enter your consumer secret key\n")
access_token1 = raw_input('Enter your access token\n')
access_secret1 = raw_input("Enter your access token secret\n")


api = twitter.Api(consumer_key = consumer_key1, consumer_secret= consumer_secret1, access_token_key = access_token1, access_token_secret= access_secret1)
handle = raw_input("Enter you're twitter handle (without'@')\n")
option = input("Enter your task\n 1> Fetch tweers \n 2> Fetch followers \n ");
if (option == 1):
	num = input("Enter the nm of tweets\n")
	print 'Tweets are logged in tweets.db'
	fetch_tweets(handle,num)
else:
	fetch_followers(handle)
