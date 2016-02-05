
"""
Learning File - Reading files
Some other methods - seek and file handler methods

www.datagenx.net
"""

# In below example we are going to read a file 
# Below are the assumptions, 
# the file is existing in the code directory

file_name = raw_input("Enter the file name:- ")        # asking for the file name
try:
	fhand = open(file_name) 	# opening a handler or pointer for input file
except:
	print "File is not existing. Please try again"
	exit()
	
count = 0	
for line in fhand:                                     # reading each line from fhand
	count += 1										   # print

print "total lines in file (1):",count	

# fhand is working as a pointer which move to next line.
# At this point if we want to use fhand we can't as pointer is at last line
# let's try

	
count = 0	
for line in fhand:                                     # reading each line from fhand
	count += 1										   # print

print "total lines in file (2):",count


# Resetting the file handler pointer
fhand.seek(0,0)                                        # seek(offset, from_which_location)
	
count = 0	
for line in fhand:                                     # reading each line from fhand
	count += 1										   # print

print "total lines in file (3):",count


# some file handler methods
print ""
print "Name of the file: ", fhand.name
print "Closed or not : ", fhand.closed
print "Opening mode : ", fhand.mode
print "Softspace flag : ", fhand.softspace	
	
	
print "\nWe are done with file reading"

#closing the file handle
fhand.close()

