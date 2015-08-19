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
def tweet_it():
	from time import sleep
	choice=raw_input("Do you want to tweet from a file?y/n")
	if choice=='y':
		t=input("Enter the time gap bwtween your tweets (in seconds)\n")
		f=raw_input("Enter the file name (make sure it's in the same ditectory as this script)")
		g=open(f,'r')
		for i in g:
			api.PostUpdates(i)
			sleep(t)
	elif choice=='n':
		tw=raw_input("Enter your tweet\n")
		api.PostUpdates(tw)
		print "done"
	else:
		print "invalid option, please enter valid option"
		tweet_it()



consumer_key1 = raw_input("Enter your Consumer key\n")
consumer_secret1 = raw_input("Enter your consumer secret key\n")
access_token1 = raw_input('Enter your access token\n')
access_secret1 = raw_input("Enter your access token secret\n")
api = twitter.Api(consumer_key = consumer_key1, consumer_secret= consumer_secret1, access_token_key = access_token1, access_token_secret= access_secret1)
handle = raw_input("Enter you're twitter handle (without'@')\n")
option = input("Enter your task\n 1> Fetch tweers \n 2> Fetch followers 3> tweet \n ");
if (option == 1):
	num = input("Enter the nm of tweets\n")
	print 'Tweets are logged in tweets.db'
	fetch_tweets(handle,num)
elif (option == 2):
	fetch_followers(handle)
elif option == 3:
	tweet_it()
else:
	print "invalid input, exiting..."
