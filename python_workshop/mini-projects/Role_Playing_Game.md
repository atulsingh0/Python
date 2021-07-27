### Who is the thief 

It involves four players—each player takes up the role of either the king, Minister , thief or soldier— and the Minister has to guess the identity of the thief.  
- Program will randomly assign the Role to Each Player. 
- Each Role has some points associated with it. King - 10, Minister - 8, Soldier - 5, thief - 0 
- It will display the Name of minister and ask the question who is the thief 
- If Answer is correct, Points will be assigned to Each Player 
- If the Answer is wrong, Minister & thief points will be switched ( Minister - 0, thief - 8) 
- Game will continue until the user does not enter (Y/N/y/n) 
- When User will enter (N/n), below point report should be displayed


Program will start as below - 
```
################ Welcome to Role Play ##################
Enter the Name of 4 Players seperated by comma (,) :  Adam, Lucy, Priya, Sid 

Round 1: 
Hey Adam, Can you guess who is the thief:  Lucy                 # Behind the scene roles was assigned as - Lucy - King, Sid - Thief, Adam - Minister, Priya - soldier 
No, You are wrong, Sid was the thief. 
Do you want to continue (Y/N) : Y 

Round 2:
Hey Sid, Can you guess who is the thief: Priya                  # Behind the scene roles was assigned as - Lucy - King, Priya - Thief, Sid - Minister, Adam - soldier 
Yes, You are correct. Priya was the thief. 
Do you want to coninue (Y/N) : n 

Thanks for Playing the Game. Below is the point table - 

Players   Points 
Adam      5                      # (0 and 5)      Thief (as the point was swapped with Sid) and Soldier
Lucy      20                     # (10 and 10)    Kind n King
Priya     5                      # ( 5 and 0)     soldier n thief
Sid       16                     # ( 8 and 8)     minister (as the point was swapped with Adam) and minister
```  

**Hint:** Program will use List, Dictionary, String formatting. Random assinment can be done by random library (https://www.w3schools.com/python/ref_random_shuffle.asp) . 

