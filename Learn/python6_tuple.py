
"""
Learning tuple
properties: immutable, ordered, iterable, hashable, can contain multiple data types

www.datagenx.net


A tuple1 is a sequence of values much like a list. The values stored in a tuple can
be any type, and they are indexed by integers. The important difference is that
tuples are immutable. Tuples are also comparable and hashable so we can sort
lists of them and use tuples as key values in Python dictionaries (we will see this later).
"""

# Creating Tuples
print "\nCreating of tuple"
t1 = ()
t2 = tuple()

print "Empty tuple:",t1, t2

print "Create tuple with signle element "
t1 = (1,)
print t1

# Viewing tuple
t2 = (1,2,3,4, 2, 2)
print "Reading tuple :",t2

print "Reading tuple element one by one"
for ele in t2:
	print ele

# tuples are like list but immutable, 
print "Accessing tuple element by index"
print t2[2]             # print 3
print t2[0]             # print 1
	
# supports lot of list methods like min, max, sum etc
print max(t2), min(t2), sum(t2)           # max = 4, min = 1, sum = 10
print t2.count(2)                         # count of element 2 = 3
print t2.index(1)                         # print the index of element(first occurrence) 1


# can convert anything into tuple by below method
t3 = tuple('apple')
print t3          # (a,p,p,l,e)
	
	
print "tuple are immutable, we can not modify (same as strings) the element but can replace"
# t2[1]=5     this will throw a error
# t3[2]='P'   this will throw a error

t2 = ('A',) + t2[1:]
print t2

print "As we seen tuple supports lot of list methods but not all"
# print t2.sort()              # this will throw a error
# print t2.append('e')         # this will throw a error

print "Because both objects have diff"
l = list()
print "\nList methods\n", dir(l)      # ignore the one which start from _
print "\nTuple methods\n", dir(t2)    # ignore the one which start from _

# create a single tuple with elements repeated (also works with lists)
print "\n",(3, 4) * 2          # returns (3, 4, 3, 4)

# tuple supports multiple var assignment in one line
(a,b) = (5,6)
print a,b

val = (1,2,3)
(p,q,r) = val
print p, q, r 

# this is why we can swap the no quickly
print a, b
(a,b) = (b,a)
print a,b

# tuples are comparable, this is compare 1 by 1 element
val2 = (1,2,4)
print val > val2        # False, as 3 is not > 4
print (1,2,3) == val    # True

# sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
print sorted(tens)        # sorts by first element in tuple, then second element
                    #   returns [(10, 40), (20, 30), (20, 60)]

# Tuples and Dictionary
dict = {'a':5, 'd':2, 'c':3, 'b':8}
print dict

# use dictionary item method to get the element like tuple list
tupli = dict.items()
print tupli

# tuple is used to sort the dictionary by key or value columns
print "\nSorting the dictionary by key"
print dict
# convert the element to tuple
print tupli
tupli.sort() # sort the tuple

for k, v in tupli:
	print k, v
 
print "\nSorting the dictionary by value"
# revering the dictionary element (Key:value) to (value:key)
tupli2 = list()
for k,v in dict.items():
	tupli2.append((v,k))
print tupli2
tupli2.sort() # sort the tuple
print tupli2

for v, k in tupli2:
	print v, k
 
# A shorter version
print sorted( [ (v,k) for k,v in dict.items() ] )


