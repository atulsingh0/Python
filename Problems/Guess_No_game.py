

import random as r

print "Welcome to Lucky !!!"

melist = r.sample(range(0,20), 4)


ch='y'

count=0
while count<4:
	uno = int(raw_input("Enter a no: "))
	if uno in melist:
		print "Volla!! You Won the game"
		exit()
	else:
		print "Alas!! you missed it"
	count += 1
	
print melist
