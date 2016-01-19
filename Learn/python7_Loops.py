
"""
Learning Loops & Iteration
Loops are actually repeated steps

www.datagenx.net
"""

print "Hello! Welcome to Python 5 tutorial Script"
print "Learning Loops & Iteration"

# generate sequence range(start[,end, stride])
print range(4)    #0,1,2,3
print range(2,7)  #2,3,4,5,6
print range(2,15,2)  #2,4,6,8,10,12,14
print xrange(4)      #this is extended range which execute at runtime and can generate big no seq

#Every loop must need these 3 things one way or other to limit its execution
#initialization, check, next level

# REMEMBER there is no {} or () to bind the code as we do in C or C++
# In python indent is necessary to achieve the same

#while loop
#While loops are called “indefinite loops” because they keep going until a logical condition becomes False


no = 5  #initialization
while no>0:    # check
	print no
	no = no -1 # next level
	
#for loop
#for loops are called “definite loops” because they execute an exact number of times

# for loop (not recommended)
fruits = ['apple', 'banana', 'cherry', 'papaya','orange',]
for i in range(len(fruits)):        # i = iteration variable
    print fruits[i].upper()

# alternative for loop (recommended style)
for fruit in fruits:
    print fruit.upper()

# use xrange when iterating over a large sequence to avoid actually creating the integer list in memory
for i in xrange(10**6):
    pass
	
"""
# Infinite loop
# I've commented out this piece of code coz this is a example of infinite loop
# Put the below code piece in another file and tye to run and see the result
# Use Ctrl-C or Ctrl-Z to kill the process

n = 3
while n > 0 :
	print 'Atul’
	print 'Singh'
print 'The End'    #this statement is never gonna run as we missed the iteration step (increment or decrement)

"""

# iterate through two things at once (using tuple unpacking)
stu = {'name':'Priya', 'clas':'9', 'rollno':24}
for key, value in stu.items():
    print key, value

# use enumerate if you need to access the index value within the loop
for index, fruit in enumerate(fruits):
    print index, fruit

# for loop
print ""
for fruit in fruits:
    print "Got :",fruit  #this will print all the fruit we have gone through
    if fruit == 'banana':   #this loop will run for all the value 
        print "Found the banana!"

	

# Breaking out of a loop
# the break statement ends the current loop and move to statement which follow the loop
inp=2
while True:
	print inp
	if inp==5:  # this will check the value of inp var
		break   # this will break the current loop and move to next statement
	inp=inp+1
	
# for/else loop
print ""
for fruit in fruits:
    print "Got :",fruit  #this will print all the fruit we have gone through
    if fruit == 'banana':   #this will run until the banana is found 
        print "Found the banana!"
        break   # exit the loop and skip the 'else' block
else:
    # this block executes ONLY if the for loop completes without hitting 'break'
	print "Can't find the banana"

"""
# Put the below code piece in another file and tye to run and see the result
# Use Ctrl-C or Ctrl-Z to kill the process

while True:
	line = raw_input('Enter anything or done: ')
	if line == 'done' :
		break
	print line
print 'Done!'

"""


	
# Skipping the Iteration with continue
# The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
print ""
for fruit in fruits:
    print "Got :",fruit  #this will print all the fruit we have gone through
    if fruit <> 'banana':   #this will run until the banana is found 
        continue            #this statement is skip the next statement in this loop
    print "We are looking for a fruit Banana"


"""
# Put the below code piece in another file and tye to run and see the result
# Use Ctrl-C or Ctrl-Z to kill the process

while True:
	line = raw_input('Enter anything or # or done: ')
	if line[0] == '#' :
		continue
	if line == 'done' :
		break
	print line
print 'Done!'
"""
	
	
