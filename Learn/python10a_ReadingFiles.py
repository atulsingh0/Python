"""
Learning File - Reading files

www.datagenx.net
"""

# In below example we are going to read a file 
# Below are the assumptions, 
# the file is existing in the code directory

 # asking for the file name
file_name = raw_input("Enter the file name:- ") 
# opening a handler or pointer for input file
fhand = open(file_name)                                

count = 0
# reading each line from fhand
for line in fhand:                                     
	count = count+1				       
	
print "Total Lines:",count
print "\nWe are done with file reading"

#closing the file handle
fhand.close()


