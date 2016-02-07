"""
www.datagenx.net
Atul Singh

Python OS Library
enable python to execute os commands

"""


import os

print "Importing OS library"


#Executing a shell command
print os.system('echo Atul')    

# printing current dir content
print os.listdir('.') 

# Returns the real process ID of the current process.
print os.getpid()     

# Creating a file test1.txt
os.system('echo "" > test1.txt')    

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# check if text2.txt is a dir or not
print os.path.isdir('./dir2')

# Delete file test2.txt
os.remove("test2.txt")

# Getting absolute path for countries.csv
path = os.path.abspath('countries.csv')
print path

# Getting basename
print os.path.basename(path)
print os.path.split(path)

# Creating a dir
if os.path.exists('./newdir'):
    pass
else:
    os.mkdir('./newdir')


# changing the current dir
os.chdir("newdir")

# checking current dir
print os.getcwd()

# changing the current dir
os.chdir("..")

# checking current dir
print os.getcwd()
print os.path.abspath('.')

# remvoing the newdir directory
os.rmdir('newdir')

# www.datagenx.net
# Atul Singh



