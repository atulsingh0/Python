

"""
Writing into File

www.datagenx.net
"""

import os

print "Welcome!"

filename=raw_input("Enter a file name to open to write: ")
mode='w'

# checking if file is existing 
if os.path.isfile(filename):
	print "this file in existing in current directory"
	print "If you want to overwrite(w) the file or want to open in append(a) mode"
	mode=raw_input("option w or a: ")
	

# Opening a file for writing
fhand = open(filename, mode)
print "Starting Writing or type END to stop: "

while True:
	input = raw_input("> ")
	if input == 'END': exit()
	fhand.write(input)
	fhand.write("\n")

#closing the file
fhand.close()


