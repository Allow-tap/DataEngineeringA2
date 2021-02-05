#Script merge all the twitter json files in one
# Creating a list of filenames 
filenames = ['tweets_12.txt',  'tweets_17.txt',  'tweets_4.txt',  'tweets_9.txt',
,'tweets_0.txt',   ,'tweets_13.txt','tweets_18.txt',  'tweets_5.txt',
,'tweets_1.txt',   'tweets_14.txt',  'tweets_19.txt',  'tweets_6.txt',
,'tweets_10.txt',  'tweets_15.txt',  'tweets_2.txt',   'tweets_7.txt',
,'tweets_11.txt','tweets_16.txt',  'tweets_3.txt',  'tweets_8.txt'] 
  
# Open file3 in write mode 
with open('allTweets.txt', 'w') as outfile: 
  
    # Iterate through list 
    for names in filenames: 
  
        # Open each file in read mode 
        with open(names) as infile: 
  
            # read the data from file1 and 
            # file2 and write it in file3 
            outfile.write(infile.read()) 
  
        # Add '\n' to enter data of file2 
        # from next line 
        outfile.write("\n") 
        
