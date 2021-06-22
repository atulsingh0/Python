
# 1. Write a program which ask 2 users and their Age and display the age difference 


# This is a welcome program 
print("Enter first User:")  # Pass any String value
user1 = input()   # input is a func which take user input 

print("Enter first User's age:")  
age1 = int(input())    


print("Enter seconds User:")  
user2 = input()   

print("Enter second User's age:")  
age2 = int(input()) 

age_diff = abs(age1 - age2)    # abs is a function to return absolute value, i.e - abs(-2) or abs(2) will return 2 

print("User1 " + user1 + " is " + str(age1) + " old.") 
print("User2 " + user2 + " is " + str(age2) + " old.") 
print("Age diff is " + str(age_diff) + ".")












