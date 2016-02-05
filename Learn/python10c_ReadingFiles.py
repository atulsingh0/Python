
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
	
data = fhand.read()	               # reading the whole file with one statement read	
# Above statement read the file and store the whole data (including new line)
# as a string and stored into a variable called data

nol = data.count("\n")+1          # Counting the total \n char in data variable
print "Total line in file:",nol   # Printing the file data
	
print "\nWe are done with file reading"

#closing the file handle
fhand.close()

