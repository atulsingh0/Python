

"""
Atul Singh
www.datagenx.net
"""

print "\n"
print "Welcome to Python point 3 - Comparison"
print "\n"

# Comparison : In mathematics we compare two or more than two values and give result
# whether it is TRUE or FALSE, YES or NO. The same we are goino learn in python ( or any programming language )

print "Comparison Operator"
print "Equal to (==)"
print "Not equal to (!=)"
print "Not equal to (<>)"
print "Less than (<)"
print "Less than or equal to (<=)"
print "Greater than (>)"
print "Greater than or equal to (>=)"
print "\n\n"


val1 = 5
val2 = -2
val3 = 0
val4 = 0.1

print 3 > 4         # False
print -3 < 2        # True
print 5 == -5       # False
print 3 <> 4        # True
print 4 >= 3        # True
print 4 != 5        # True
print 8 == 8.0      # True
print val3 > val4   # False
print val2 <= val4  # True

print "\n\nBoolean Operator"
print "It compare statements whether they are true or nor"
print "or - Return True if anyone is True"
print "and - Return True if and if only ALL are True else False"
print "not - Invert the current value, True if False"
print "Priority if mixed - Not, And , Or"
print "\n\n"


"""
OR table - 
True or True     ->    True
True or False    ->    True
False or True    ->    True
False or False   ->    False
"""
print 2 > 1 or 2 < 1         		# True,  True or False 
print 3 > 1 or 4 > 9                # True,  True or True


"""
AND table - 
True and True     ->    True
True and False    ->    False
False and True    ->    False
False and False   ->    False
"""
print 2 > 1 and 2 < 1         		 # False,  True or False 
print 3 > 1 and 4 > 9                # True,  True or True


"""
Not table - 
Not True   ->    False
Not False  ->    True
"""
print not 2 > 1         		# False, Not True  
print not 3 > 9                 # True,  Not False 


print "\nMixing Boolean Operator"
print (2>1) and (not 2> 4) or (7 == 7)       # True, True and (not False) or True



# Atul Singh
# www.datagenx.net


