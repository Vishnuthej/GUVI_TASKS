"""1. Write a python program using a function to which will do the following 
a) The function will create a text file with the current timestamp 
b) The file content should have the content of the current timestamp

STEPS: 
1) Define a function to create a txt file named as timestamp.txt
  a)get the current time stamp
  b)assign the timestamp as file name
  c)open & write the file with timestamp as content in it
2)Make the content of the text file also the current time stamp"""

import datetime

def create_textdoc_with_timestamp():
    thetimenow = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"file_{thetimenow}.txt"
    
    wfile = open(filename, 'w')
    wfile.write(thetimenow)
    wfile.close()

create_textdoc_with_timestamp()
