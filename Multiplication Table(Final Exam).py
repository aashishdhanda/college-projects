#Porgramming
#Final_Exams
#Multiplication_Table


#First of all we will take input of Multiplier Value from user
multiplier_value=int(input("Please enter the Multiplier Value:- "))   #Taking Input of value for multipier_value(As asked in the Question) from the user
while multiplier_value < 2 or multiplier_value > 12:    #While loop for any non-valid input from user
    print("Oops! You have given the value outside the given range")
    start_value=int(input("Please enter the Multiplier Value(The value must be from 2-12):- "))  #Taking input of value for start_value(As asked in the Question) from the user Agaim

start_value=int(input("Please enter the Start Value(The value must be from 2-12):- "))  #Taking input of value for start_value(As asked in the Question) from the user
while start_value < 2 or start_value > 12: #While loop for any non-valid input from user
    print("Oops! You have given the values outside the given range")
    start_value=int(input("Please enter the Start Value(The value must be from 2-12):- "))  #Taking input of value for start_value(As asked in the Question) from the user Agaim
 
stop_value=int(input("Please enter the Stop Value:- "))  #Taking input of value for stop_value(As asked in the Question) from the user
while stop_value < 2 or stop_value > 12 or stop_value < start_value:  #While loop for any non-valid input from user
    print("Oops! You have given the values outside the given range or it is greater than the Start Value")
    stop_value=int(input("Please enter the stop Value(The value must be from 2-12 AND Greater than the Start Value):- "))  #Taking input of value for stop_value(As asked in the Question) from the user again


# Printing Data as per the format
print()   #This is for a empty line
print("Multiplication Table")
for i in range(start_value,stop_value+1):
    print(multiplier_value ,"x" ,i ,"=",multiplier_value*i)
                           
input("Press ENTER to Exit")   # this will promt user to press enter to terminate the programme. 


    
