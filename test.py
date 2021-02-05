from json import JSONDecoder
from functools import partial

filenames = ['tweets_0.txt',  'tweets_17.txt',  'tweets_4.txt',  'tweets_9.txt',
'tweets_12.txt',   'tweets_13.txt','tweets_18.txt',  'tweets_5.txt',
'tweets_1.txt',   'tweets_14.txt',  'tweets_19.txt',  'tweets_6.txt',
'tweets_10.txt',  'tweets_15.txt',  'tweets_2.txt',   'tweets_7.txt',
'tweets_11.txt','tweets_16.txt',  'tweets_3.txt',  'tweets_8.txt'] 
count = 0
def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
         buffer += chunk
         while buffer:
             try:
                 result, index = decoder.raw_decode(buffer)
                 yield result
                 buffer = buffer[index:].lstrip()
             except ValueError:
                 # Not enough data to decode, read more
                 break


for file in filenames:
	with open( file, 'r') as infh:
    		for data in json_parse(infh):
    						if not 'retweeted_status' in data:
    								count += 1
    								print(data['text'])
    								print(count)
