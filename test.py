import json

with open('tweets_0.txt') as f:
	data = json.load(f)
	
for tweet in data['retweeted']:
	print(tweet)
