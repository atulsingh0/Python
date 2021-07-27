### Develop a program for Class Test Report
When program will be triggered, it will ask following information -    
- It will ask User to enter the Subjects (i.e - English, French, Math, Science, Art, Social-Science) 
- Once above steps is done, Next it will ask the Student Name to Enter the marks for them. 
- It will keep asking Student Name and Marks for Each Subject until User does not Enter "N" when asking continue question. 
- This will look like something below - 

```
####### Welcome to Marks Report ###############################    
Enter the name of all the subjects seperated by comma (,) :   English, French, Math, Science, Art, Social-Science 
Total No of Subjects entered : 6

Enter the Student Name : Adam
Enter Marks for Adam (English): 90
Enter Marks for Adam (French): 80
Enter Marks for Adam (Math): 75
Enter Marks for Adam (Science): 90
Enter Marks for Adam (Art): 75
Enter Marks for Adam (Social-Science): 90 
Do you want to want to continue (Y/N):  Y

Enter the Student Name : Lyle
Enter Marks for Lyle (English): 90
Enter Marks for Lyle (French): 80
Enter Marks for Lyle (Math): 75
Enter Marks for Lyle (Science): 90
Enter Marks for Lyle (Art): 75
Enter Marks for Lyle (Social-Science): 90 
Do you want to want to continue (Y/N):  N 

Thanks for Entering the marks. 
Please select the Report Type by entering associated Report no -  
* Enter 1 for Full detailed Report 
* Enter 2 for Conolidated Average Report
* Enter 3 for Ranking Report 
Please Enter your choice (1/2/3) : 1 

Here, it will display the particular report. 

############## END ###############################
``` 

Now, Reports must be something like below - 

**Report 1: Full Detailed Report**
```
Student Name:  Adam 
-------------------------
Subject   Marks
-------------------------
English   90
French    80 
.
.
.
Student Name: Lyle 
-------------------------
Subject   Marks
-------------------------
English   90
French    80 
.
.
.
```


**Report 2: Consolidated Average Report**
```
Student Name      Average Marks  (toal marks/No of subjects)
Adam              80
Lyle              80
Priya             75
Sam               70
.
.
.
```

**Report 3: Ranking Report**
```
Student Name      Rank
Adam              1
Lyle              1
Priya             2
Sam               3 
```

**Hint:** Program will use List, Dictionary, Functions, String formatting 

 