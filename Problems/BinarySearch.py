
"""
To check whether a word is in the word list by binary search
"""

# below word list is a example list
words=["a", "aah", "aahed", "aahing", "aahs", "aardvark", 
"aardvarks", "aardwolf", "ab", "abaci", "aback", "abacus", 
"abacuses", "abaft", "abalone"]

# word need to search
ser="swap"

# Binary search Recursion implementation
def bin_search(lst,sindex,lindex,ser):
	mindex = int((sindex+lindex)/2)
	if ser > lst[mindex+1]:
		return bin_search(lst,mindex+1,lindex,ser)
	elif ser < lst[mindex-1]:
		return bin_search(lst,sindex,mindex-1,ser)
	else:
		return mindex


# Binary search Iteration implementation
def bin_search2(lst,ser):
	max=len(lst)-1
	min = 0
	while min <= max:
		mid = int((min+max)/2.0)
		if lst[mid] == ser:
			return mid
		elif ser > lst[mid+1]:
			min = mid
		else:
			max = max-1



sindex=0
lindex=length=len(words)

print "Calling the func"

index=bin_search(words,sindex,lindex,ser)
print index, words[index]

index=bin_search2(words,ser)
print index, words[index]


