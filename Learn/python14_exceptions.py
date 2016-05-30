

# Exceptions

import sys

var1 = 6


# Multiple Except Clauses
print "\ntry1"
try:
	var2 = raw_input("Enter a value : ")
	print var1/int(var2)
except ZeroDivisionError:
	print "You can not deivide by zero"
except TypeError:
	print "There is data type mismatch"
except ValueError:
	print "Invalid conversion"
except KeyboardInterrupt:
	print "\nCancel"
except:
	print "\nUnknown exeception"
	
print "\ntry2"
# Raising a exeception
# Cleanup try...finally
try:
	raise ZeroDivisionError ("Somehitng")
except ZeroDivisionError:
	print "You can not deivide by zero"
finally:
	print "I've learnt about exeception"
	
print "\ntry3"
# Combining Exceptions into one	
# Customized printing
try:
	var2 = raw_input("Enter a value : ")
	print var1/int(var2)
except ZeroDivisionError as (errno, err):
	print "You can not deivide by zero",errno
except (TypeError, ValueError):
	print "There is Type or Value error"
except KeyboardInterrupt:
	print "\nCancel"
except:
	print "\nUnknown exeception"	
	
	
print "\ntry4"
try:
	print 4/0
except:
	e = sys.exc_info()[1]
	f = sys.exc_info()[0]
	print f,e
	
