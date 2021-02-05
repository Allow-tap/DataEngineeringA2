import os
import json

filenames = ['tweets_0.txt',  'tweets_17.txt',  'tweets_4.txt',  'tweets_9.txt',
'tweets_12.txt',   'tweets_13.txt','tweets_18.txt',  'tweets_5.txt',
'tweets_1.txt',   'tweets_14.txt',  'tweets_19.txt',  'tweets_6.txt',
'tweets_10.txt',  'tweets_15.txt',  'tweets_2.txt',   'tweets_7.txt',
'tweets_11.txt','tweets_16.txt',  'tweets_3.txt',  'tweets_8.txt'] 
#filenames = ['tweets_0.txt', 'tweets_1.txt']
cl_data = []
for file in filenames:
		count = 0
		data = []
		
		with open(file) as f:
				for line in f: #for each line in our file
						if line.strip(): #skip the empty lines
				    			data.append(json.loads(line))
		print(len(data))
		for file in data:
			if not 'retweeted_status' in file:
					cl_data.append(file)
		print(len(cl_data))
		print(type(cl_data))	

with open("clean.json", "w") as outfile:  
    json.dump(cl_data, outfile) 
#with open('output.txt') as data:
#   objects = [json.loads(line) for line in data]
#for obj in objects:
#		print(obj)
#print(len(objects))

#filenames = 'tweets_0.txt'
#with open(filenames) as infile, open('output.txt', 'w') as outfile:
#    for line in infile:
#        if not line.strip(): continue  # skip the empty line
#        outfile.write(line)  # non-empty line. Write it to output 
