### Develop a program for Invoice Discount

1: When program will be triggered, it will ask following information -    
- It will ask User to enter the user type (R/r) for Regular User and (N/n) for New User
- Next, It will ask the Total Invoice Bill in $
- If User is regular, It will calculate 5% discount else 2% discount
- Print the generated Reciept at last.  

```
############################### Welcome to Food Mart ###############################    
------------------------------------------------------------------------------------
Kindly Enter the User Type (R/r/N/n) :  r 
Enter the Total Bill in $ : 200


############## Invoice ###########################
Total Bill:    200.00
Discount %5:    10.00

Amount to Pay:  190.00 

############## END ###############################
``` 


Once, you are done with above program, We are goind extend it by adding more functionality. 


2: When program will be triggered, it will ask following information -    
- It will ask User to enter the user type (R/r) for Regular User and (N/n) for New User
- Next, It will ask the Bill amount for these categories: Meat_n_Deli, Dairy, Fruit_n_Veg, Household_Products, Grocery, Beverages, Snacks, Baked_Items
- If User is regular, It will calculate the discount as % for each categories - 5, 4, 5, 2, 2, 2, 2, 4
- If User is new, It will calculate the discount as - 4, 3, 3, 0, 0, 1, 1, 2 
- Print the generated Reciept at last.  


```
############################### Welcome to Food Mart ###############################    
------------------------------------------------------------------------------------
Kindly Enter the User Type (R/r/N/n) :  r 
Enter the Bill amount for Meat_n_Deli in $ : 20
Enter the Bill amount for Dairy in $ : 0
Enter the Bill amount for Fruit_n_Veg in $ : 30
Enter the Bill amount for Household_Products in $ : 30
Enter the Bill amount for Grocery in $ : 10
Enter the Bill amount for Beverages in $ : 10
Enter the Bill amount for Snacks in $ : 20
Enter the Bill amount for Baked_Items in $ : 30


############## Invoice ###########################
Meat_n_Deli:    			20.00
Discount 5%:    			-1.00
Dairy:           			 0.00
Discount 4%:    			-0.00
Fruit_n_Veg:    			30.00
Discount 5%:    			-1.50
Household_Products: 		30.00
Discount 2%:    			-0.60
Grocery:        			10.00
Discount 2%:    			-0.20
Beverages:      			10.00
Discount 2%:    			-0.20
Snacks:         			20.00
Discount 2%:    			-0.40
Baked_Items:    			30.00
Discount 4%:    			-1.20  

Total Bill:    			   150.00
Total Discount :    		-5.10

Amount to Pay:  		 $ 144.90 

############## END ###############################
``` 
