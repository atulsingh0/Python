

# Exceptions

var1 = 6

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
	

# Raising a exeception

try:
	raise ZeroDivisionError ("Somehitng")
except ZeroDivisionError:
	print "You can not deivide by zero"
finally:
	print "I've learnt about exeception"
	
	
