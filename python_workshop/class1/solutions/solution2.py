# 2. Write a program which ask User to Enter Amount, Interest Rate and Year and return the Total Interest calculated. 
# Interest Amount = Principal x Rate x NoYear / 100

print("Enter the principal amount:")
amt = float(input())

print("Enter the interest rate:")
rate = float(input())

print("Enter the total no of years:")
yr = float(input())

int_amt = amt * rate * yr / 100

print("Total Interest will be : "+str(int_amt))
