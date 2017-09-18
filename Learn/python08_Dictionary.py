

"""
Learning Dictionary
properties: unordered, iterable, mutable, can contain multiple data types
made up of key-value pairs
keys must be unique, and can be strings, numbers, or tuples
values can be any type

www.datagenx.net
"""

print "\nHello! Welcome to Python 7 tutorial Script"
print "Learning Dictionary"

print "\nCreating list"
emp1 = dict()
emp2 = {}

print "Empty Dictionary:", emp1, emp2

dic = {'one':1, 'two':2, 'three':3, 'four':4}
print dic

stu = dict(name='Priya', sub='Python', clas=9, roll=24)
print stu

# Working on a dictionary
print "\nExtracting Values/Keys from dict"
val = dic.values()     #this will return the values list
keys = dic.keys()		#this will return the keys list
keyval = dic.items()   # this will retunr a tuple list in key,value format
print "keys:", keys
print "Value:",val
print "Key,Value:",keyval
print "count:",len(dic)
print stu['name']      # Priya

print "Value assignment : dic[key]=value"
dic['five']=5
dic['six']=6
print dic,"\n"

# modify a dictionary (does not return the dictionary)
stu['gender'] = 'F'              # add a new entry
print stu
stu['name'] = 'Rahul'            # edit an existing entry
print stu
del stu['gender']                       # delete an entry
print stu
stu['friends'] = ['Divya', 'Ashish']       # value can be a list
print stu
stu.pop('friends')                       # removes an entry and returns the value ('homer')
print stu
stu.update({'stream':'science', 'school':'SGM', 'friends': ['Priya', 'Raj']})   # add multiple entries
print stu


# Added a key with default value
stu.setdefault('teachers',['Mr Principal']).append('Mr Gomez')
print stu['teachers']
stu.setdefault('friends',['Vivek']).append('Vibhav')
print stu['friends']
stu.setdefault('friends',['Vivek']).append('Swati')
print stu['friends']


# get method to default value
# accessing values more safely with 'get'
print stu['name']                       #Rahul
print stu.get('name')                   # same thing
#print stu['class-teacher']              # throws an error
print stu.get('class-teacher')               # None
print stu.get('class-teacher', 'not found')  # 'not found' (the default)


# accessing a list element within a dictionary
print stu['friends'][0]            # 'Priya'
stu['friends'].remove('Raj')       # removes 'Raj'
print stu['friends']

print "\nTraversing through dictionary:"
for key in dic:
	print key, dic[key]

print "\n"	
for key, val in dic.items():
	print key, val

print "\n"	
for index,key in enumerate(dic):
	print index,key


# Check if Key is existing in dictionary
print "\n",'seven' in dic
print '\nseven' not in dic

# Dictionary is not ordered, we can achieve this by sorting key list
dum = {7:'Seven',1:'Atul', 2:'Singh', 'three':'Char', 5:'Five', '6':'six'}
keylist = dum.keys()
keylist.sort()
print "\n"
for key in keylist:
	print key, dum[key]  # sorting order integer then strings
	
# Dictionary is mostly used in Counters
sente = "List all processes List state of a process List state of all processes in a job  List all locks  List locks held by a process \
List locks held by all processes in a job  Clear locks held by a process  Clear locks held by all processes in a \
job  Logout a process  Logout all processes in a job  Clear status file for a job"
print sente,"\n"

count = {}
words = sente.split()

for word in words:
	count[word] = count.get(word, 0) + 1
print count

	
	
