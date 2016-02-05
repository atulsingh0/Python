
"""
Learning File - Reading files
If file is missing, Handle it with try and except

www.datagenx.net
"""

# In below example we are going to read a file 
# Below are the assumptions, 
# the file is existing in the code directory

# asking for the file name
file_name = raw_input("Enter the file name:- ")        
try:
	# opening a handler or pointer for input file
	fhand = open(file_name) 	
except:
	print "File is not existing. Please try again"
	exit()
	
count = 0	

# reading each line from fhand
for line in fhand:                                     
	count += 1		

print "total lines in file:",count	
print "\nWe are done with file reading"

#closing the file handle
fhand.close()


