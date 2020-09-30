#Programming
# ZVIS CAR RENTAL
#    Information
# choice of car     car code    daily cost    Weekly cost
# Compact            1             $15            $90
# Mid size           2             $20            $120
# Full Size          3             $30            $180
# SUV                4             $35            $200

# Daily and weekly charges are increased by 10% for cars equipped with luxary package
# Flat fee of $25 is assessed if the customer requres the car to be equipped with GPS

# If insurance is requested, the following rates apply:-
# Age of Driver            Daily Coverage           Weekly Coverage
# 18-25                              $ 7                                $ 40
# 26-40                              $ 5                                $ 30
# Over 40                          $ 3                                $ 15

# There is a $ 10 fee to drop off the car at another location
# Add $5 for late return protection(LRP) .Allows customer to drop the car upto 3 hours late
# Without LRP, A full day is charged after one hour late
# Veterans and active members of the armed Services receive a 10% discount on total of the order
# AARP members receive 5% discount on order total
# Prompt for:---  Name, Age, Period etc (END OF THINKING CAPAPCITY <LOL>)

#Programming starts now :-)
#import os
#def clear():
#    _=os.system("cls")
def insurance_data():
    print("The insurance charges will be as follows:-")
    print("# Age of Driver            Daily Coverage           Weekly Coverage")
    print("# 18-25                              $ 7                                $ 40")
    print("# 26-40                              $ 5                                $ 30")
    print("# Over 40                          $ 3                                $ 15")
        
def all_input():
    for i in range(1):
        try:
            while 1:
                name=input("Please enter your name:-  ")
                if name == "":
                    print("Customer Name can't be blank , Please try Again !!!!")
                else:
                    break
        except:
            input("An error occured , Please press enter to close the programme")
            break
        
        try: 
            while 1:
                age=int(input("Please enter your age:- "))
                if age < 18 or age > 95:
                    print("Sorry, You are not eligible to book any car for rental , Minimum age is 18 and maximum is 95 !!!!!")
                else :
                    break
        except:
            input("An error occured , Please press enter to close the programme")
            break
        
        try:
        
            while 1:
                car=int(input("Please choose the car:- \n 1. Compact \n 2. Mid Size \n 3. Full Size \n 4.SUV \nPlease enter the number of the car , you wanna  select :-  "))
                if car <1  or car >4 :
                    print("Invalid Entry , Please enter number of any car( 1-4 ) ")
                else:
                    break
        except:
            input("An error occured , Please press enter to close the programme")
            break
        try:
            while 1:
                days=int(input("Please enter the rental period (Number Of Days):- "))
                if days < 1 or days > 180 :
                    print("Rental period can't be less than 1 or more than 180 Days,Please enter a valid rental period")
                else:
                    break
        except:
            input("An error occured , Please press enter to close the programme")
        try:
                
            while 1:
                pickup=int(input("Please enter the date of pickup (1-31) :- "))
                if pickup <1 or pickup >31 :
                    print("Invalid Entry, Please try Again :-| ")
                else :
                    break
        except:
            input("An error occured , Please press enter to close the programme")
            break
        
        try:
             while 1:
                dropoff=int(input("Please enter the date of dropoff (1-31) :- "))
                if dropoff <1 or dropoff >31 :
                    print("Invalid Entry, Please try Again :-| ")
                else:
                    break
        except:
            input("An error occured , Please press enter to close the programme")
            break
        try:
            while 1:
                luxury=input("Do you wanna take luxury package (i.e. will increase daily and weekly charges by 10%)\n Please enter 'y' for yes and 'n' for no:- ")
                if luxury == 'y' or luxury == 'Y' or luxury == 'n' or luxury == 'N' :
                   break
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")
            break
        try :
            while 1:
                insurance=input("Do you want to take insurance ,(y or n):- ")
                if insurance == 'y' or insurance == 'Y' or insurance == 'n' or insurance == 'N' :
                    
                    break
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")

        try:
            while 1:
                gps=input("Do you want your car to be equipped with GPS (i.e. will cost $25 extra to you) \n Please enter 'y' for yes and 'n' for no :- ")
                if gps == 'y' or gps == 'Y' or gps == 'n' or gps == 'N' :
                     break
                    
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")

        try:
            while 1:
                dropoff_option=input("Do you want your car to dropoff the car at another location (i.e. will cost $10 extra to you) \n Please enter 'y' for yes and 'n' for no :- ")
                if dropoff_option == 'y' or dropoff_option == 'Y' or dropoff_option == 'n' or dropoff_option == 'N' :
                     break
                    
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")
        try:
            while 1:
                late_protection=input("Do you want to add late return protection (i.e. will cost $5 extra to you)\n This allows You to drop off the car up to 3 hours late and not be charged a full day’s rate. \n Without this coverage, You will be charged a full day’s rate if the car is dropped off more than 1 hour late. \n Please enter 'y' for yes and 'n' for no :- ")
                if late_protection == 'y' or late_protection == 'Y' or late_protection == 'n' or late_protection == 'N' :
                     break
                    
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")

        try:
            while 1:
                membership=input("Are you a Veteran or Active member of Armed Forces !\n Please enter 'y' for yes and 'n' for no :- ")
                if membership == 'y' or membership == 'Y' or membership == 'n' or membership == 'N' :
                     break
                    
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")
        try:
            while 1:
                aarp=input("Are you a Member of AARP !\n Please enter 'y' for yes and 'n' for no :- ")
                if aarp == 'y' or aarp == 'Y' or aarp == 'n' or aarp == 'N' :
                     break
                    
                else:
                    print("Please enter a valid input, ('y' for yes ) and ('n' for no) ")
        except:
            input("An error occured , Please press enter to close the programme")


#def processing():
    # All processing will be done here

def output_frame():
    print("\t \t Zvis Car Rental Company")
    print("Preliminary Bill")
    print("Customer ", name,"\t", "Age ", age)
    
    
all_input()
output_frame()

#             WORK  VIEW
# firstly take all inputs and validate them
# Secondly , process all the data
# Verify and repair exception handling
# Make a frame for output
# Make it multi-User application
# Frame , background, text color etc
# compile to .exe file

# USED IDENTIFIERS
# name , age, car, days, pickup, dropoff, luxury, insurance, gps, dropoff_option, late_protection, membership, aarp

# USED FUNCTIONS
# insurance_data(), all_input(), processing()
