
print "www.datagenx.net"

print "Hello! Welcome to Python 2 tutorial Script"
print "We will see how to determine data type and Strings"

### DATA TYPES ###
##################

# determine the type of an object
print type(5)         # print 'int'
print type(5.0)       # print 'float'
print type('two')     # print 'str'
print type(False)      # print 'bool'
print type(None)      # print 'NoneType'

# check if an object is of a given type
name = 'Atul'
print isinstance(5.0, int)            		# print False
print isinstance(5.0, (int, float))   		# print True
print isinstance(name, (int, float, str))  	# print True


# convert an object to a given type
print float(5)
print int(5.3)
print int(5.9)
print str(5.3)

# zero, None, and empty containers are converted to False
print bool(0)
print bool(None)
print bool('')    # empty string
print bool([])    # empty list
print bool({})    # empty dictionary

# non-empty containers and non-zeros are converted to True
print bool(5)
print bool('two')
print bool([5])



####  Strings   ####
####################

# Creating String vairable
subject = "python"
code = "P101"

print subject
print code

print subject, code

# String is a character array in python so we can
# do some string manipulations like below (index access, start from 0)

print subject
print subject[2]    # print the 3rd char of string which is 't'
print subject[1:3]  # substring 2nd and 3rd char 


# some methods to manipulate the string
print len(subject)      # 6
print subject.lower()   # python   # only work with str data type
print subject.upper()   # PYTHON   # only work with str data type
print str(subject)      # convert input to string data type


# Some advance manipulation on Strings
# concatenation - use +

print subject
print code
print subject + code
print subject + " subject code is " + code

print "%s subject code is %s" %(subject, code)   # C style code


# Excape char \
# we can escape the char special meaning with \ 
# print "Hi, this is a double quote " "      # this line will throw a error
print "Hi, this is a double quote \" "       # Hi, this is a double quote "

print "Hi I am printing \
multi-line string \
to escape new line \
I am using escape char"


print "Thanks"
print "Atul Singh"
print "atul@datagenx.net"

