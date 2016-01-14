
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
#while loop keep executing till the condition is TRUE
no = 5  #initialization
while no>0:    # check
	print no
	no = no -1 # next level
	
#for loop
#for loop keep executing till the condition is FALSE

# for loop (not recommended)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print fruits[i].upper()

# alternative for loop (recommended style)
for fruit in fruits:
    print fruit.upper()

# use xrange when iterating over a large sequence to avoid actually creating the integer list in memory
for i in xrange(10**6):
    pass

# iterate through two things at once (using tuple unpacking)
stu = {'name':'Priya', 'clas':'9', 'rollno':24}
for key, value in stu.items():
    print key, value

# use enumerate if you need to access the index value within the loop
for index, fruit in enumerate(fruits):
    print index, fruit

# for/else loop
for fruit in fruits:
    if fruit == 'banana':
        print "Found the banana!"
        break   # exit the loop and skip the 'else' block
else:
    # this block executes ONLY if the for loop completes without hitting 'break'
    print "Can't find the banana"
	

# Breaking out of a loop
# the break statement ends the current loop and move to statement which follow the loop

	
	
	
