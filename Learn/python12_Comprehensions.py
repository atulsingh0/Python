"""
Learning comprehensions
To do complecated thigs easily

www.datagenx.net
"""

#======================================================
from inspect import currentframe

# for this new code, I have used a function to get the line no of a particular print lno(),   statement
# So you will see the line no of code which output is that. Easy to relate with code

def lno():
    cf = currentframe()
    return str(cf.f_back.f_lineno)+"- "
#======================================================


## LIST comprehensions

lis = [1,2,3,4,5,6,7,9]
even =[]
odd =[]

for item in lis:
	print item,
print ""

# Example 1
for item in lis:
	if item%2==0:
		even.append(item)
	else:
		odd.append(item)
		
print lno(),   even
print lno(),   odd
	
# now in comprehension

even = []
odd = []
# equivalent list comprehension (using a ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
[even.append(item) if item%2==0 else odd.append(item) for item in lis]

print lno(),   even
print lno(),   odd


# Example 2

for item in lis:
	print lno(),   item**2

# in comprehension
# syntax: [expression for variable in iterable if condition]
print lno(),   [item**2 for item in lis] 
print lno(),   [item**2 for item in lis if item%2==0] 
print lno(),   [(item**2, item**3) for item in lis if item%2==0] 

# equivalent list comprehension
matrix = [[1,3],[2,4],[3,5]]
items = [item for row in matrix for item in row]      # [1, 3, 2, 4, 3, 5]
print lno(),   items

			  
## SET comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}   # {5, 6}

values = set(range(10))
print lno(),   values
print lno(),   [item for item in values]
print lno(),   [item for item in values if item%3==0]
print lno(),   [item if item%3==0 else 0 for item in values ]


## DICSTIONARY comprehensions
fruits = ['apple', 'banana', 'pineapple']
print lno(),   fruits

# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit:key for key, fruit in enumerate(fruits)} # {'apple': 0, 'banana': 1, 'cherry': 2}
fruit_revrs = {len:key for key, len in fruit_lengths.items()} # {'apple': 0, 'banana': 1, 'cherry': 2}

print lno(),   fruit_lengths
print lno(),   fruit_indices
print lno(),   fruit_revrs



# Thanks
# Atul Singh
# www.datagenx.net



