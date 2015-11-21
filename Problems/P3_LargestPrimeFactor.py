

print "Problem 3"
print "The prime factors of 13195 are 5, 7, 13 and 29."
print "What is the largest prime factor of the number 600851475143 ?"
print "\n"

no = 600851475143
prime=False
pf = []
fact = []

# Finding the factor of no
# To limit the factor list We are not finding all the factors but the factors of sq root of the no
# because no == sqrt(no)**2

for i in range(1, int(no**0.5)+1):

	if no%i == 0:
		fact.append(i)
		
		# Checking whether factor is a prime or not
		if i==2 or i==3:
			pf.append(i)
		else:
			for p in range(2,i):
				if i%p == 0:
					prime=False
					break
				else:
					prime=True
			
			if prime:
				pf.append(i)


print "All Factor of no %d is :" %(no), fact
print "All Prime Factor of no %d is :" %(no),pf
print "Max prime facor :",max(pf)
	
# Atul Singh
# www.datagenx.net

