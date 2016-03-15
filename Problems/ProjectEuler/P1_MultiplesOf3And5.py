

print "Problem 1"
print "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23."
print "Find the sum of all the multiples of 3 or 5 below 1000."

No = int(raw_input("Enter a integer :"))
print "\n"

sum=0
for i in range(No):
	if i%3 == 0 or i%5 == 0:
		sum=sum+i
print sum
    


# Atul Singh
# www.datagenx.net
