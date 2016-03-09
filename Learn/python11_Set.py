"""
Learning Set
 like dictionaries, but with keys only (no values)
 properties: unordered, iterable, mutable, can contain multiple data types
 made up of unique elements (strings, numbers, or tuples)

 www.datagenx.net

"""

#======================================================
from inspect import currentframe

# for this new code, I have used a function to get the line no of a particular print statement
# So you will see the line no of code which output is that. Easy to relate with code

def lno():
    cf = currentframe()
    return str(cf.f_back.f_lineno)+"- "
#======================================================


print ""
# create an empty set
empty_set = set()

# create a set
languages = {'python', 'r', 'java'}         # create a set directly
os = set(['linux', 'mac', 'python'])  # create a set from a list
lang = {'python'}

# examine a set
print lno(),  type(os)               # print lno(),  variable type

print lno(),  len(languages)              # returns 3
print lno(),  'python' in languages       # returns True

# set operations
print lno(),  languages & os          # returns intersection: {'python'}
print lno(),  languages.intersection({'fortran','python'})  # return intersection

print lno(),  languages | os          # returns union: {'linux', 'r', 'java', 'mac', 'python'}
print lno(),  languages.union({'fortran','perl'})  # return a new set without new element

print lno(),  languages - os          # returns set difference: {'r', 'java'}
print lno(),  languages.difference({'fortran','r'})  # return difference: {'python', 'java'}

print lno(),  os - languages          # returns set difference: {'linux', 'mac'}
print lno(),  {'fortran','r'}.difference(languages)  # return difference: {'fortran'}

print lno(),  'r' in languages            # return True if exists
  
print lno(), lang.issubset(languages)     # return True
print lno(), lang.issuperset(languages)   # return False



# modify a set (does not return the set)

# Sets are bags of unique values. If you try to add a value that already exists in the set, 
# it will do nothing. It won’t raise an error
# there are two methods to add - add and update

languages.add('sql')        # add a new element
print lno(),  languages
languages.add('r')          # try to add an existing element (ignored, no error)
print lno(),  languages

# update method add the multiple values into set but ignored the dups
languages.update('go', 'spark')   # add multiple elements (can also pass a list or set)
print lno(),  languages
languages.update({'C++', 'node.js'},{'C#','j3','dot net'},['C++','r','visualC++','cobol']) 
print lno(),  languages


# Removing items from set
# 3 ways - discard, remove, pop

languages.discard('C++')      # removes an element if present, but ignored otherwise
print lno(),  languages
languages.discard('C++')      #No error

languages.remove('java')      # remove an element
print lno(),  languages
#languages.remove('c')            # try to remove a non-existing element (throws an error)

# The pop() method removes a single value from a set and returns the value. 
# However, since sets are unordered, there is no “last” value in a set, 
# so there is no way to control which value gets removed. It is completely arbitrary.
print lno(),  languages.pop()             # removes and returns an arbitrary element
print lno(),  languages.clear()           # removes all elements

# get a sorted list of unique elements from a list
print lno(),  sorted(set([9, 0, 2, 1, 0]))    # returns [0, 1, 2, 9]

print ""



# Thanks
# Atul Singh
# www.datagenx.net

