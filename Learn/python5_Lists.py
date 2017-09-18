"""
Learning List
properties: ordered, iterable, mutable, can contain multiple data types

www.datagenx.net
"""

print "Hello! Welcome to Python 5 tutorial Script"
print "Learning List"

print "Creating list"
emp1 = list()
emp2 = []

print "Empty list:",emp1,emp2 

lis = [2,4,5,6,3,12,45,75,32,['a','b']]
print lis
print len(lis)   #print the length of list

print "\nlist are mutable, mean you can change the value of any index"
print "We can replace the list element by assigning it to new value"
lis[3] = "atul"
print lis

print "\ntraversing through list"
for item in lis:
	print item,
	
print "\n\nList opertation"
print "+ concat and * repeat"

lis2 = [1,3]
print lis2
print lis2 * 2
print lis + lis2

print "\n\nList Slicing"
print lis[:]     # print whole lis
print lis[2:]    # print from 2nd index to end 
print lis[3]     # print index 3 value
print lis[-2]    # print 2nd last element
print lis[::1]   # list[start : end : stride]
print lis[::2]   # print every 2nd element
print lis[::-2]   # print every 2nd element but from back
print lis[::-1]   # print list in reverse
print lis[2:-2]   # this will print from index2 till 2nd last elements
print lis[4:2:-1] # 

print "\n\nList Methods"
# sort - sort the elements
# len - give the total element
# push, pop, del 
# append - append a new element
# extent - append the new elements

print lis
print lis2
print lis2.append('append')            #this will print None as method is return None
print lis2
print lis2.extend(['extend','method']) #this will print None as method is return None
print lis2
print "we can achieve the same with concatenation but It is SLOWER than extend methog"
chk = lis2 + ['extend','method']
print chk
print lis2.extend(lis)                 #this will print None as method is return None
print lis2
print "Inserting any element at specific index"
# inserting 'Raj' at index 2
lis2.insert(2,'Raj')
print lis2

print "\n\nDeleting the elements with pop"
print lis2
x = lis2.pop()   # this will remove the last one
print "poped value is:",x
print lis2
x = lis2.pop(2)  # this will pop index 2 element
print "poped value is:",x
print lis2

# with pop, we can get the removed value
# if we dont need that we can use del method
print "\n\nDeleting the elements with del"
del lis2[3]
print lis2
# with del we can remove list slice
del lis2[2:4]
print lis2 

# if you dont know the index but value
print "\n\nDeleting the elements with remove"
lis2.remove(45)
print lis2

print "\nSorting the list"
lis2.sort()
print lis2
lis2.sort(reverse=True)
print lis2
lis2.reverse()  #another method to reverse the list
print lis2
#lis2.sort(key=len)
#print lis2

print "\nTotal element"
print len(lis2)
print "Max:", max(lis2)
print "Min:", min(lis2)

# Search element in list 
print "\n\nSearching atul in list"
print lis2.index('atul')    # this will give you the index of first instance
print lis2.count('atul')    # this will count the total occurance

# List and String
str = 'Python is awesome'
str2 = 'Atul'
print "\n\nstr=",str
print "str2=",str2

print "Converting string to list"
lstr2 = list(str2)
lstr = list(str)
print lstr,"\n",lstr2

print "breaking the sentence into word"
lstr3 = str.split()  # by default splitted by ' ' , can define the delimiter as split(del)
print lstr3
# join is the inverse of split
str3 = '-'.join(lstr3)
print "\nJoining with -",str3


# Aliasing
# When vars referencing the same object are called as aliased
print "\n\nObject Aliasing or creating reference"
var1 = [1,2,3]
var2 = var1         #var2 is referencing var1
var3 = [1,2,3]      #var3 and var2 or var1 is identical but not aliased
print var1, var2
print var2 is var1
print var3 is var1

# identical check
print var1 == var2
print var1 == var3

# by id function, you can check the object id, if id are same that means aliased
print id(var1)
print id(var2)
print id(var3)


# when object is aliased If we change anyone's value it will affect the others also
print ""
var2[0] = 'One'        #It will modify the both var1, var2  as both are aliased
print var2, var1
print var2 is var1     # True
var1[1] = 'Two'        #It will modify the both var1, var2  as both are aliased
print var2, var1
print var1 is var2     # True
var3[0] = 'NoOne'      #var3 is identical of var1, not aliased, so it will not affect var1
print var3, var1 
print var3 is var1     #False


# List comprehensions
# better way to create conditional list
lis_no = [2,5,1,9,8,4,7]
lis2 = [x**2 for x in lis_no]  
print lis2 #print no*no 
lis2 = [x**2 for x in lis_no if x%2==0]
print lis2 #print no*no if no is even


# Atul Singh
# www.datagenx.net


