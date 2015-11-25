
"""
Problem 6  - Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""



# This function will calculate the no's sum and then return its square value
def SumSq(no):
	sum_no = no*(no+1)/2
	return sum_no**2

# This function will calculate the no's square and then return its summed value
def SqSum(no):
	sqlist=[]
	for i in range(1,no+1): 
		sqlist.append(i**2)
	return sum(sqlist)


def SqSum2(no):
	sum=0
	for i in range(1,no+1):
		sum=sum+i**2
	return sum

no=int(raw_input("Enter a no:"))

print SumSq(no) - SqSum(no)
print SumSq(no) - SqSum2(no)


# Atul Singh
# www.datagenx.net

