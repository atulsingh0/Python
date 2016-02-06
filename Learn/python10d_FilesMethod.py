
"""
Learning File - Reading file in one go

File should be small enough to fit into your system memory
If file is missing, Handle it with try and except

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
	
data = fhand.read(140)	               # reading the first 140 char from file with one statement read	
# Above statement read the file and store the whole data (including new line)
# as a string and stored into a variable called data
print data
nol = data.count("\n")+1          # Counting the total \n char in data variable
print ""
print "Total line in file:",nol   # Printing the file data
print "Total char read:",len(data)
	

# readline methods read a line one at a time
# but this will read the file from the current file handler position
data = fhand.readline()	
print "\nLine read by readline method:", data
	


# readlines methods read all line and store as a list
# but this will read the file from the current file handler position
data = fhand.readlines()	
print "\nTotal Lines read by readlines method", len(data)	
	
print "\nWe are done with file reading"


# closing the file
fhand.close()



