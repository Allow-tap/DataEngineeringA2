import io
import sys
import string
import re
import json

for line in sys.stdin:
		keylist = ['han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'] #the words we are looking for
		data = json.loads(line) #load the line as type dictionary using json
		text = data['text'] #get the text, text is of type list
		words = re.split('[:",. ]',text) #split the words
		for word in words: #search all the words of each text
			word = word.lower() #case insensitive
			word = word.strip() #strip of trailings
			if word in keylist: #if the word is in the keylist
							print(word, 1)
							keylist.remove(word) #remove that word from the key list we only want to see if the tweet 
																	 #contains the keyword
