

"""
Learning String
properties:  iterable, immutable
A String is a sequence of character.

www.datagenx.net

"""

print "Hello! Welcome to Python 6 tutorial Script"
print "Learning Strings"

st = "Atul is learning strings"
sNo = '432'
sAlp = 'Atul98'
print st, type(st)
print sNo, type(sNo)

# Check the data type
print type(st) == str
print isinstance(st, (str, unicode))
print type(st) == type(str())

# String Manipulation
# String is a character array in python so we can
# do some string manipulations like below (index access, start from 0, must be int)

print st[0]     # A
#print st[100]  # throw a error if try to print beyond the index 

# String Slicing like list
print st[:]      #Atul is learning strings
print st[4:]	 # is learning strings
print st[13:24]  #ing strings

# some methods to manipulate the string
print len(st)      # 24
print st.title()   # Atul Is Learning Strings   # every word is Captalized
print st.lower()   # atul is learning strings   # only work with str data type
print st.upper()   # ATUL IS LEARNING STRINGS   # only work with str data type
print st.startswith('A')   # returns True
print st.endswith('you')   # returns False
print st.isdigit()         # returns False (returns True if every character in the string is a digit)
print st.isalnum()         # returns False
print sAlp.isalpha()         # returns True
print st.islower()           
print st.isupper()
print st.istitle()
print st.find('is')      # returns index of first occurrence (2), but doesn't support regex
print st.find('i')			# index of first i
print st.find('i',6)        # index of first i after the index 6
print st.find('i',14,24)        # index of first i after the index 14 and before 24
print st.find('hate')      # returns -1 since not found
print st.replace('Atul','Rahul')    # replaces all instances of 'Atul' with 'Rahul'
print type(sNo), type(int(sNo))     # converting string to int

# split a string into a list of substrings separated by a delimiter
print st.split()          # return word list sep by space(default)
print st.split(' ')
st2 = "Python,is,easy"
stlist = st2.split(',')
print stlist

# join the word list with -
print '-'.join(stlist)

# Some advance manipulation on Strings
# concatenation - use +
word1 = 'Python'
word2 = 'Script'
print word1+word2    #PythonScript
print word1+" "+word2    #Python Script
# print word1 + 42        this will throw a error, all tokens should be converted into string type
print word1 + str(42)    #Python42

# in as a logical operator
print 'P' in word1			#True
print 'c' in word1			#False

# String comparison
print word1 > 'Python1'
print word1 < 'Python1'
print word1 == 'Python'


# remove whitespace from start and end of a string
line = '  Python and Me  '
print line.strip()          #Python and Me
print line.rstrip()          #  Python and Me    #right strip
print line.lstrip()          #Python and Me    #left strip

# normal strings versus raw strings
print 'first line\nsecond line'     # normal strings allow for escaped characters
print r'first line\nfirst line'     # raw strings treat backslashes as literal characters
print 'first line\\nfirst line'     # We can achive the same with \ which disable the special meaning of character

# String Looping
index = 0
while index < len(word1):
	print index, word1[index]
	index += 1

for letter in word1:
	print letter


