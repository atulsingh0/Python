"""
Learning File - Reading files

www.datagenx.net
"""

# In below example we are going to read a file 
# Below are the assumptions, 
# the file is existing in the code directory

file_name = raw_input("Enter the file name:- ")        # asking for the file name
fhand = open(file_name)                                # opening a handler or pointer for input file

for line in fhand:                                     # reading each line from fhand
	print line										                       # print
	
print "\nWe are done with file reading"
