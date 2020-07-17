import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open('newfile.txt','w') as hand:
    pass
  timestamp = os.path.getmtime('newfile.txt')
  timestamp=datetime.datetime.fromtimestamp(timestamp)
  # Convert the timestamp into a readable format, then into a string
  
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}-{}-{}".format(timestamp.year,timestamp.month,timestamp.day))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd